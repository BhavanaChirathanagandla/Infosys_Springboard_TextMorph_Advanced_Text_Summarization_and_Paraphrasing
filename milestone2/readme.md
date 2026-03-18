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

<img width="1919" height="1050" alt="Screenshot 2026-03-18 085507" src="https://github.com/user-attachments/assets/75f876cc-dfcf-4030-afb9-4613312db7d5" />

<img width="1904" height="1079" alt="Screenshot 2026-03-18 085611" src="https://github.com/user-attachments/assets/c2a52513-80f1-4bf9-b854-00466bc1e9b2" />

<img width="1918" height="1059" alt="Screenshot 2026-03-18 085619" src="https://github.com/user-attachments/assets/3b23f313-3b4e-4825-83d0-f8225d2bba4a" />

<img width="1914" height="961" alt="Screenshot 2026-03-18 085658" src="https://github.com/user-attachments/assets/aae77794-033e-4508-ac91-c37e0186972f" />

<img width="1912" height="1061" alt="Screenshot 2026-03-18 085755" src="https://github.com/user-attachments/assets/001fed35-d1fe-45d7-8a71-3725f0ad21d0" />
<img width="1918" height="1073" alt="Screenshot 2026-03-18 085813" src="https://github.com/user-attachments/assets/155313b3-4424-45b4-9b35-c450e160868b" />
<img width="1919" height="283" alt="Screenshot 2026-03-18 085824" src="https://github.com/user-attachments/assets/ad1f1466-79df-491b-a550-1f56eaf5c64a" />

<img width="1919" height="1079" alt="Screenshot 2026-03-18 085848" src="https://github.com/user-attachments/assets/7c995c4a-b30f-4212-bf78-9a47117bc3d5" />

<img width="1919" height="1079" alt="Screenshot 2026-03-18 085859" src="https://github.com/user-attachments/assets/5c912fd6-0495-464c-9eef-9faf2d63a55f" />

<img width="839" height="441" alt="Screenshot 2026-03-18 085927" src="https://github.com/user-attachments/assets/d1262b38-eb7a-4316-9ea1-58007e25809e" />

<img width="1915" height="1079" alt="Screenshot 2026-03-18 085957" src="https://github.com/user-attachments/assets/81e94949-7280-4389-a016-4ba0fc917129" />

<img width="1917" height="1069" alt="Screenshot 2026-03-18 090021" src="https://github.com/user-attachments/assets/428a4caa-a9f3-48b0-8e95-fdef35fedae4" />


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
