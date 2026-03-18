# Milestone 2 – AI Readability Analysis & Dashboard

## Project Title  
TextMorph – Advanced Text Summarization and Paraphrasing  

## Internship  
Infosys Springboard Internship 6.0 – Batch 13  

## Description  

In Milestone 2, the project was enhanced by integrating AI-powered readability analysis and dashboard features into the existing authentication system.

This milestone focuses on analyzing user-provided text and PDFs using NLP-based readability metrics. It also introduces a user-friendly dashboard for visualization and interaction.

The module builds on Milestone 1 and prepares the system for advanced features like text summarization and paraphrasing in future milestones.

## Features Implemented  

### 1. Text Readability Analysis  
- Input text manually for analysis  
- Calculates readability metrics using textstat  
- Metrics include:
  - Flesch Reading Ease  
  - Grade Level  
  - Sentence Count  
  - Word Count  
  - Syllable Count  
  - Complex Words  

### 2. PDF Text Extraction  
- Upload PDF files  
- Extract text using PyPDF2  
- Perform readability analysis on extracted content  

### 3. Interactive Dashboard  
- Clean Streamlit UI  
- Displays analysis results clearly  
- Visualization using Plotly charts  
- Easy navigation via sidebar  

### 4. User Session Integration  
- Works with JWT authentication from Milestone 1  
- Only logged-in users can access analysis features  
- Secure dashboard access  

### 5. Data Visualization  
- Graphical representation of readability scores  
- Enhances user understanding of text complexity  

## Technologies Used  

- Python  
- Streamlit  
- Textstat (Readability Analysis)  
- PyPDF2 (PDF Processing)  
- Plotly (Visualization)  
- JWT (Authentication from Milestone 1)  
- SQLite Database  

## Database Structure  

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    email TEXT UNIQUE,
    password TEXT,
    security_question TEXT,
    security_answer TEXT
);
