# Resume Analyzer with ATS Integration

## Project Overview

This project is a web-based Resume Analyzer that leverages Google's Gemini language model to analyze resumes against job descriptions (JDs) and provide insights. It uses an advanced Applicant Tracking System (ATS) approach to evaluate resumes and return results in a structured JSON format. The application is built using Flask and supports PDF resume uploads.

## Features

- Analyze resumes against job descriptions to calculate a match percentage.
- Identify missing keywords that could improve resume relevancy.
- Generate a profile summary from the resume content.
- Supports PDF file uploads.
- Real-time analysis with fast response times.
- CORS enabled for cross-origin support.

## Technologies Used

- Python
- Flask
- Google Generative AI (Gemini)
- PyPDF2 for PDF text extraction
- dotenv for environment variable management
- Flask-CORS for cross-origin support
- JSON for structured output

## Setup and Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up the environment variables in a `.env` file:
   ```bash
   GOOGLE_API_KEY=<your_google_api_key>
   ```
5. Run the application:
   ```bash
   python app.py
   ```

## Usage

1. Open your browser and go to `http://localhost:5000`.
2. Upload a PDF resume and enter the job description.
3. Click the analyze button to get the results.
