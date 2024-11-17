<div align="center">

# AI Data Extraction Dashboard

<p align="center">
  <img src="![image](https://github.com/user-attachments/assets/49ac5ca2-4c1a-4dfa-a026-52d94fee7848)
"/>
</p>

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Google Sheets](https://img.shields.io/badge/Google%20Sheets-34A853?style=for-the-badge&logo=google-sheets&logoColor=white)](https://www.google.com/sheets/about/)
[![OpenAI](https://img.shields.io/badge/Groq-412991?style=for-the-badge&logo=openai&logoColor=white)](https://groq.com/)
[![SerpAPI](https://img.shields.io/badge/SerpAPI-0A83F0?style=for-the-badge&logo=google&logoColor=white)](https://serpapi.com/)


Automated data extraction powered by AI - From spreadsheets to intelligent insights in seconds.

</div>

## Table of Contents
- [Project Description](#-project-description)
- [Setup Instructions](#-setup-instructions)
- [Usage Guide](#-usage-guide)
- [API Keys and Environment Variables](#-api-keys-and-environment-variables)
- [Optional Features](#optional-features)
- [Quick Start](#-quick-start)
- [Troubleshooting](#troubleshooting)
- [Demo Video](#-demo-video)

## 🛠️ Tech Stack

| Category | Technologies |
|----------|-------------|
| Frontend | ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=Streamlit&logoColor=white) |
| Backend | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) |
| Data Processing | ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white) |
| APIs | ![Google Sheets](https://img.shields.io/badge/Google%20Sheets-34A853?style=flat-square&logo=google-sheets&logoColor=white) ![Groq](https://img.shields.io/badge/Groq-412991?style=flat-square&logo=openai&logoColor=white) ![SerpAPI](https://img.shields.io/badge/SerpAPI-000000?style=flat-square&logo=serpapi&logoColor=white) |

## 📜 Project Description

The **AI Data Extraction Dashboard** is a cutting-edge tool designed to automate data extraction and analysis. It enables users to efficiently process data from multiple sources, including CSV files and Google Sheets, while integrating web scraping and AI-powered insights. This dashboard leverages advanced technologies to transform raw data into actionable intelligence in seconds, offering:

- **Multi-Source Input**: Seamless integration with local files and cloud-based spreadsheets.
- **AI-Powered Search**: Automates web data retrieval using APIs like SerpAPI.
- **Smart Processing**: Leverages Groq's AI models to extract meaningful insights from complex data.
- **Export-Ready Output**: Easily download results or sync them with external platforms.

With a user-friendly interface built on Streamlit, this project empowers data analysts, researchers, and businesses to make informed decisions effortlessly.

---
## 🛠️ Setup Instructions

### Step 1: Load Data
- **From CSV:** Upload your CSV file directly through the dashboard interface.
- **From Google Sheets:**
  1. Enter the URL of the Google Sheets document.
  2. Ensure your [Google API credentials](https://developers.google.com/sheets/api/quickstart) (`credentials.json`) are properly set up.

### Step 2: Perform Search Queries
- Use the dashboard to input search terms.
- The tool integrates with [SerpAPI](https://serpapi.com/) to automatically fetch relevant data.

### Step 3: AI-Powered Data Processing
- Extract meaningful insights from raw data using Groq's AI models.
- View summaries and prepare the data for further analysis.

### Step 4: Export Results
- Download the output as a CSV file.
- Sync the processed data back to a Google Sheet for easy sharing.

---
## 📋 Usage Guide

The **AI Data Extraction Dashboard** is designed to be user-friendly and intuitive. Below are the step-by-step instructions for using the dashboard, connecting Google Sheets, and setting up search queries.

### 1. **Running the Dashboard**

Once you’ve installed all dependencies and set up the project (refer to the Setup Instructions above), you can start the dashboard by running the following command:

```bash
streamlit run app.py
```
This will open the dashboard in your default web browser.

## Setup & Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/ai-dashboard.git

# Install dependencies
npm install
```

## Connecting Google Sheets

1. Create a Google Sheets document
2. Set up Google Sheets API credentials:
   - Visit the Google Cloud Console
   - Create a new project and enable Google Sheets API
   - Download `credentials.json`
3. Place `credentials.json` in project root
4. Enter Google Sheets URL in dashboard
5. Authorize API access when prompted

## Uploading CSV Files

To upload a CSV file:

### Step 1: 
Click on the "Upload CSV" button in the dashboard.
### Step 2: 
Select the file from your local directory.
### Step 3: 
The CSV will be uploaded, and the data will appear in the dashboard for further processing.

## Search Queries

The dashboard allows you to perform web searches using AI-powered search capabilities. To set up a search query:

### Step 1: 
Navigate to the search section of the dashboard.

### Step 2: 
Enter the search query in the text input field.

For example:

If you want to search for a particular product or service, type something like: "Best data visualization tools for 2024".
If you want to extract specific information, be more specific: "Top Python libraries for data analysis".
### Step 3: 
Click the "Search" button, and the dashboard will retrieve data using SerpAPI.
### Step 4: 
Once the search is complete, the results will be processed by the AI model (Groq), which will extract relevant insights and display them in a structured format.

### Example Queries
- `"Identify the Country in which the Names called Ferrell LLC, Mckinney, Riley and Day, Hester Ltd , Holder-Sellers , Mayer Group are Located"`

### Supported Formats
- CSV
- Google Sheets (automatic sync)

### 🔗 API Keys and Environment Variables
### Step 1: Create the .env file
In your project’s root directory (the same level as your app.py), create a new file called .env.
Inside the .env file, store your API keys and other necessary environment variables in the following format:
```bash
SERPAPI_KEY=
GOOGLE_CREDS_PATH=
GROQ_API_KEY=
```
### Step 2: Access the variables in your Python code
To access these environment variables in your Python code, you’ll need to use the python-dotenv package, which allows Python to load environment variables from the .env file.
Install python-dotenv: Add python-dotenv to your requirements.txt file, or install it directly via pip:
```bash
pip install python-dotenv
```
Load the environment variables (Testing) in your app.py or other Python files where you need the keys:
```bash
# Import the required libraries
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Access the variables
SERPAPI_KEY = os.getenv("SERPAPI_KEY")
GOOGLE_CREDS_PATH = os.getenv("GOOGLE_CREDS_PATH")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Use these variables in your code
print(SERPAPI_KEY, GOOGLE_CREDS_PATH, GROQ_API_KEY)
```

### Optional Features
- Real-time data filtering
- Custom sorting options
- Export capabilities
- Google Sheets synchronization
  
## 🚀 Features

- **Multi-Source Data Input**: CSV & Google Sheets integration
- **AI-Powered Search**: Automated web scraping with SerpAPI
- **Smart Processing**: LLM-based data extraction via Groq
- **Export Ready**: Download results or sync with Google Sheets

## Troubleshooting

### Common Issues
- Missing API keys
- Invalid credentials
- Google Sheets API access errors
- Permission denied errors

## Contributing

1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Create Pull Request

---

## ⚡ Quick Start

```bash
# Clone repo
git clone https://github.com/shashankmutyala/ai-data-extraction-dashboard.git

# Install dependencies
pip install -r requirements.txt

# Run dashboard
streamlit run app.py
```
## 🎥 Demo Video

Watch the demo video on Loom:

[Watch the Loom Video](https://www.loom.com/share/d503652089364b00882a870e97b6264a?sid=143ac111-2cd3-431f-831f-b1a65489c18a)

## License
-Mutyala Shashank
