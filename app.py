import google.generativeai as genai
import PyPDF2 as pdf
import os
from dotenv import load_dotenv
import json
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import re

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

app = Flask(__name__)
CORS(app)

def get_gemini_response(input_prompt):
    model = genai.GenerativeModel("gemini-2.0-pro-exp-02-05")
    response = model.generate_content(input_prompt)
    return response.text

def extract_text_from_pdf(file):
    reader = pdf.PdfReader(file)
    content = ""
    for page in reader.pages:
        content += page.extract_text()
    return content

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze_resume():
    try:
        jd = request.form.get("jd", "")
        resume_file = request.files.get("resume")
        
        if resume_file:
            resume_text = extract_text_from_pdf(resume_file)
        else:
            return jsonify({"error": "No resume uploaded"}), 400

        input_prompt = f"""
        You are an advanced ATS (Applicant Tracking System) with deep expertise in technology fields, including software engineering, data science, data analytics, and big data engineering. 

        Your task is to evaluate the given resume against the provided job description. Please return the response as a **strictly formatted JSON string** with the following structure:

        {{
            "JD Match": "percentage",
            "MissingKeywords": ["keyword1", "keyword2", ...],
            "Profile Summary": "summary text"
        }}

        Ensure that the response does not contain any extra characters or text before or after the JSON string.

        Resume: {resume_text}
        Job Description: {jd}
        """
        
        response = get_gemini_response(input_prompt)
        print("Raw Response:", response)

        # Clean the response to remove code block markers
        cleaned_response = re.sub(r"```json|```", "", response).strip()

        # Parse the cleaned response
        try:
            json_response = json.loads(cleaned_response)
            return jsonify(json_response)
        except json.JSONDecodeError:
            return jsonify({"error": "Invalid response format", "response": cleaned_response}), 500
            
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
