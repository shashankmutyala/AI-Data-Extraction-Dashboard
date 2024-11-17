import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
import time
from dotenv import load_dotenv
import requests

# Load environment variables
load_dotenv()

# Initialize and validate API keys
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
SERPAPI_KEY = os.getenv("SERPAPI_KEY")
GOOGLE_CREDS_PATH = os.getenv("GOOGLE_CREDS_PATH")


def validate_api_keys():
    """Validate required API keys are present."""
    missing_keys = []
    if not SERPAPI_KEY:
        missing_keys.append("SERPAPI_KEY")
    if not GROQ_API_KEY:
        missing_keys.append("GROQ_API_KEY")
    if not GOOGLE_CREDS_PATH or not os.path.exists(GOOGLE_CREDS_PATH):
        missing_keys.append("GOOGLE_CREDS_PATH")

    if missing_keys:
        st.error(f"Missing API keys: {', '.join(missing_keys)}")
        st.stop()


class DataManager:
    """Handles data loading from different sources."""

    @staticmethod
    def load_csv(file) -> pd.DataFrame:
        """Load data from a CSV file."""
        try:
            df = pd.read_csv(file)
            st.success("CSV file loaded successfully,Thank You for providing Data.")
            return df
        except Exception as e:
            st.error(f"Error loading CSV: {str(e)}")
            return None

    @staticmethod
    def load_gsheet(url: str, creds_path: str) -> pd.DataFrame:
        """Load data from a Google Sheet."""
        try:
            scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
            creds = ServiceAccountCredentials.from_json_keyfile_name(creds_path, scope)
            client = gspread.authorize(creds)
            sheet = client.open_by_url(url).sheet1
            df = pd.DataFrame(sheet.get_all_records())
            st.success("Google Sheet loaded successfully,Thank You for providing Data.")
            return df
        except Exception as e:
            st.error(f"Error loading Google Sheet: {str(e)}")
            return None


class WebSearcher:
    """Handles web searches using SerpAPI."""

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://serpapi.com/search"
        self.rate_limit_delay = 1  # seconds between requests

    def test_api_key(self) -> bool:
        """Test if the SerpAPI key is valid."""
        try:
            params = {"engine": "google", "q": "test", "api_key": self.api_key}
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            st.success("SerpAPI connected successfully.")
            return True
        except requests.exceptions.RequestException:
            st.error("Invalid SerpAPI key. Please check your configuration.")
            return False

    def search(self, query: str) -> dict:
        """Perform a web search."""
        try:
            params = {"engine": "google", "q": query, "api_key": self.api_key}
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            time.sleep(self.rate_limit_delay)  # Rate limiting
            return response.json()
        except Exception as e:
            st.warning(f"Search error for query '{query}': {str(e)}")
            return {"error": str(e)}


class GroqProcessor:
    """Handles interactions with Groq's API."""

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.api_base = "https://api.groq.com/openai/v1/chat/completions"  # Adjusted the correct endpoint

    def test_api_key(self) -> bool:
        """Test if the Groq API key is valid."""
        try:
            headers = {"Authorization": f"Bearer {self.api_key}"}
            response = requests.post(self.api_base, headers=headers)  # Use POST to test the endpoint
            st.write("Groq API Test Response:", response.json())  # Log the response for debugging
            response.raise_for_status()
            return True
        except requests.exceptions.RequestException as e:
            st.error(f"Groq API key test failed: {str(e)}")  # Log the error for debugging
            return False

    def process_results(self, query: str, context: str) -> str:
        """Process search results using Groq's API."""
        try:
            headers = {"Content-Type": "application/json", "Authorization": f"Bearer {self.api_key}"}
            data = {
                "model": "llama3-8b-8192",
                "messages": [{"role": "user", "content": f"Identify the Country in which the Name called {query} is Located"}],
            }
            response = requests.post(self.api_base, headers=headers, json=data)
            st.write("Groq API Process Response:", response.json())  # Log the response for debugging
            response.raise_for_status()
            return response.json().get("choices", [{}])[0].get("message", {}).get("content", "No response")
        except requests.exceptions.RequestException as e:
            return f"Groq processing error: {str(e)}"


class Dashboard:
    """Main dashboard class that handles the UI and processing logic."""

    def __init__(self):
        st.set_page_config(page_title="Shashank's AI Data Extraction Dashboard", layout="wide")

        validate_api_keys()

        self.data_manager = DataManager()
        self.searcher = WebSearcher(SERPAPI_KEY)
        self.groq = GroqProcessor(GROQ_API_KEY)

        self.data = None
        self.setup_ui()

    def setup_ui(self):
        """Set up the main user interface."""
        st.title("Mutyala Shashank's AI Data Extraction Dashboard")

        st.header("1. Data Input")
        data_source = st.radio("Select Data Source:", ["CSV Upload", "Google Sheets"])

        if data_source == "CSV Upload":
            uploaded_file = st.file_uploader("Upload CSV file", type="csv")
            if uploaded_file:
                self.data = self.data_manager.load_csv(uploaded_file)
        else:
            sheet_url = st.text_input("Enter Google Sheets URL")
            if sheet_url:
                self.data = self.data_manager.load_gsheet(sheet_url, GOOGLE_CREDS_PATH)

        if self.data is not None:
            self.show_data_processing_options()

    def show_data_processing_options(self):
        """Display data processing options once data is loaded."""
        st.header("2. Data Configuration")
        st.dataframe(self.data.head())
        selected_columns = st.multiselect("Select columns(entity) for processing:", self.data.columns.tolist())

        if selected_columns:
            st.subheader("3. Extract Information")
            query_template = st.text_input("Enter search query :")

            if st.button("Extract Information"):
                results = []
                for _, row in self.data.iterrows():
                    entity = row[selected_columns[0]]
                    query = query_template.format(entity=entity)
                    search_results = self.searcher.search(query)
                    if "error" not in search_results:
                        context = " ".join(result.get("snippet", "") for result in search_results.get("organic_results", []))
                        response = self.groq.process_results(entity, context)
                        results.append({"Entity": entity, "Response": response})
                    else:
                        results.append({"Entity": entity, "Response": search_results["error"]})

                results_df = pd.DataFrame(results)
                st.dataframe(results_df)

                # Provide option to download results
                st.download_button("Download CSV", results_df.to_csv(index=False).encode(), "extracted_data.csv", "text/csv")

                # Option to update Google Sheet (if loaded from Google Sheets)
                if st.button("Update Google Sheet") and "Google Sheets URL" in self.data.columns:
                    # Add logic to update Google Sheets here
                    st.write("Google Sheet update functionality coming soon!")


# Run the Dashboard
if __name__ == "__main__":
    dashboard = Dashboard()
