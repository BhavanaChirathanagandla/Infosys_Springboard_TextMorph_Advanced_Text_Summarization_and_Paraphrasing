# 🧠 TextMorph (Colab Implementation)
AI-Powered Content Simplification, Summarization & Paraphrasing Suite

This repository contains the complete implementation of the **TextMorph project using Google Colab notebooks**, divided into 4 milestones as per Infosys Springboard Internship.


## 🔗 Quick Links

| Category        | Link                  |
|-----------------|-----------------------|
| 📽️ Demo Video   | Coming Soon           |
| 🧩 Source Code  | This Repository       |
| 🐳 Docker Support | Yes                 |
| 🧠 AI Models    | Pegasus · BART · FLAN-T5 |


---

## 📌 Project Overview
TextMorph is an AI-based application designed to:
- Simplify complex text
- Generate summaries
- Paraphrase content
- Improve readability using NLP models

The project is implemented step-by-step across **4 milestones using Google Colab (.ipynb files)**.

---

## 📁 Milestone Structure
TextMorph/
│── Milestone1_Authentication.ipynb
│── Milestone2_TextProcessing.ipynb
│── Milestone3_AIModels.ipynb
│── Milestone4_FinalIntegration.ipynb
│── README.md

---

## 🚀 Milestone 1 – User Authentication System

### 🔐 Objective
To build a secure authentication system using:
- Streamlit UI
- JWT Authentication
- Database (SQLite/MySQL)

### ✅ Features Implemented
- User Signup with validation
- Login system
- JWT token generation
- Dashboard after login
- Forgot Password (Security Question)
- Ngrok deployment

### ▶️ How to Run in Colab
1. Open `Milestone1_Authentication.ipynb`
2. Run all cells sequentially
3. Start Streamlit app
4. Use Ngrok link to access UI

---

## ✂️ Milestone 2 – Text Processing Module

### 🎯 Objective
To implement core NLP preprocessing and readability analysis.

### ✅ Features Implemented
- Text cleaning (stopwords, punctuation removal)
- Tokenization
- Lemmatization
- Readability metrics:
  - Flesch Reading Ease
  - Gunning Fog Index
  - SMOG Index
  - Coleman-Liau Index

### ▶️ How to Run
1. Open `Milestone2_TextProcessing.ipynb`
2. Run all cells
3. Input sample text to test preprocessing

---

## 🤖 Milestone 3 – AI Models Integration

### 🎯 Objective
To integrate transformer-based NLP models.

### ✅ Models Used
- Pegasus → Summarization
- BART → Summarization & rewriting
- FLAN-T5 → Paraphrasing

### ✅ Features Implemented
- Text summarization (short/medium/long)
- Paraphrasing with style control
- Model loading via Hugging Face Transformers

### ▶️ How to Run
1. Open `Milestone3_AIModels.ipynb`
2. Install required libraries
3. Run model cells
4. Provide input text for generation

---

## 🧩 Milestone 4 – Final Integration

### 🎯 Objective
To combine all modules into a complete system.

### ✅ Features Implemented
- Integrated authentication + NLP + models
- Streamlit UI
- User dashboard
- History tracking
- Feedback system
- Admin panel

### ▶️ How to Run
1. Open `Milestone4_FinalIntegration.ipynb`
2. Run all cells
3. Launch Streamlit app
4. Access via Ngrok public URL

---

## 🛠 Tech Stack

| Component | Technology |
|----------|-----------|
| Frontend | Streamlit |
| Backend | Python |
| Database | SQLite / MySQL |
| Security | JWT |
| NLP | NLTK |
| Models | Hugging Face Transformers |
| Deployment | Google Colab + Ngrok |

---

## ⚙️ Setup Instructions (Colab)

### Step 1: Install Dependencies
!pip install streamlit pyngrok transformers nltk bcrypt python-jose
## ⚙️ Setup Instructions (Colab)

### Step 2: Setup Ngrok

from pyngrok import ngrok
ngrok.set_auth_token("YOUR_NGROK_AUTH_TOKEN")



### Step 3: Run Streamlit

!streamlit run app.py &
public_url = ngrok.connect(8501)
print(public_url)

## 📝 Usage Guide

1. Register/Login  
2. Enter text  
3. Choose:
   - Summarization  
   - Paraphrasing  
4. View results  
5. Analyze readability  
6. Save history & feedback

 ## 📊 Datasets & Evaluation

### Datasets
- WikiAuto  
- Newsela  
- ASSET  

### Metrics
- ROUGE-L  
- BLEU  
- Readability Score Improvement

## 📸 Screenshots

- Signup Page  
- Login Page  
- Dashboard  
- NLP Processing Output  
- Summarization Results  
- Admin Panel

## 🔮 Future Enhancements

- Multilingual support  
- Voice input/output  
- Mobile app  
- Browser extension  
- Real-time collaboration

## 👥 Team

| Name        | Role                 |
|-------------|----------------------|
| Your Name   | ML Engineer          |
| Your Name   | Backend Developer    |
| Your Name   | Frontend Developer   |
| Your Name   | Documentation        |
