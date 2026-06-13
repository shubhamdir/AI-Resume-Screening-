# AI Resume Screening System

## Overview

AI Resume Screening System is a web application that analyzes a candidate's resume against a job description and provides ATS (Applicant Tracking System) compatibility scores, similarity scores, selection probability, and personalized recommendations.

The system helps job seekers understand how well their resume matches a job role and what improvements are needed to increase their chances of selection.

---

## Features

* Resume Upload (PDF)
* Resume Parsing
* Skill Extraction
* ATS Score Calculation
* Similarity Score Analysis
* Final AI Score
* Selection Probability Prediction
* Resume Improvement Recommendations
* Multi-Domain Support

  * IT
  * Finance
  * HR
  * Marketing
  * Content Writing
* FastAPI Backend
* Streamlit Frontend
* SQLite Database

---

## Tech Stack

### Frontend

* Streamlit

### Backend

* FastAPI

### Database

* SQLite
* SQLAlchemy

### NLP & ML

* Scikit-learn
* TF-IDF Vectorizer
* Cosine Similarity

### Resume Processing

* PyPDF2

---

## Project Workflow

1. User uploads resume.
2. Resume text is extracted from PDF.
3. Skills are identified from the resume.
4. User pastes a job description.
5. ATS score is calculated.
6. Similarity score is calculated using NLP.
7. Final AI score is generated.
8. Selection probability is estimated.
9. Recommendations are displayed.

---

## Installation

### Clone Repository

git clone YOUR_GITHUB_LINK

cd AI-Resume-Screening-System

### Install Dependencies

pip install -r requirements.txt

### Start Backend

uvicorn main:app --reload

### Start Frontend

streamlit run frontend/app.py

---

## API Endpoints

### Upload Resume

POST

/upload-resume

### Analyze Resume

POST

/analyze-direct

---

## Future Improvements

* PDF Report Generation
* Recruiter Dashboard
* Candidate Ranking
* Cloud Deployment
* AI Interview Preparation

---

## Author

Shubham Sangram Dash
