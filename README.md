# 🧠 TextMorph  
### AI-Powered Content Simplification, Summarization & Paraphrasing Suite  
Transforming complex content into clear, concise, and accessible communication.

---

## 🔗 Quick Links

| Category | Link |
|----------|------|
| 📽️ Demo Video | https://drive.google.com/file/d/11BptchXlwkf57GmHGy3VI_m-XZZkZXcp/view |
| 🧩 Source Code | This Repository |
| 🐳 Docker Support | Coming Soon |
| 🧠 AI Models | Pegasus · BART · FLAN-T5 |

---

## 📌 Table of Contents
- About the Project
- Problem Statement & Motivation
- Key Features
- Architecture
- Tech Stack
- Models Used
- Installation & Setup
- Usage Guide
- Admin Controls
- Datasets & Evaluation
- Screenshots
- Team
- License

---

## 📖 About the Project
TextMorph is an advanced AI tool designed to enhance reading accessibility and content quality using NLP, readability science, and transformer-based language models.

It offers:
- Summarization  
- Paraphrasing  
- Readability scoring  
- Admin dashboard  

📌 Built as part of Infosys Springboard Internship Final Project  
📌 Target users: Students, educators, researchers, bloggers, media professionals  

---

## 🎯 Problem Statement & Motivation
Millions of people struggle to understand complex written content. Manual simplification takes time and expertise.

🔹 Our solution uses AI to:
- Improve readability  
- Shorten lengthy content  
- Rewrite content at different complexity levels  
- Help users learn faster  

---

## 🚀 Key Features

### 👤 User Features

| Feature | Description |
|--------|------------|
| 🔐 Secure JWT Authentication | Login, registration, OTP recovery |
| 📊 Readability Analyzer | Flesch, SMOG, Gunning Fog, graphs |
| ✂️ Summarization | Short / Medium / Long |
| 🔁 Paraphrasing | Simple / Neutral / Advanced |
| 👥 Comparison View | Original vs Generated |
| ⭐ Feedback System | Ratings |
| 🕘 History Log | Save & download |
| 🧑 Profile Management | Secure password update |

---

### 🛠 Admin Features 
- User management (add/remove/promote)  
- Usage analytics & reports  
- Feedback monitoring  
- Global search system  
- Full audit logs  
- Lock/Unlock
---

## 🧩 Architecture
Monolithic deployment with secure database and ML model integration  

📌 Architecture Diagram 
<img width="1024" height="1536" alt="ChatGPT Image Mar 23, 2026, 08_14_41 AM" src="https://github.com/user-attachments/assets/73bfb727-8c50-4c1d-98b2-2f9f2fd42e52" />

---

## 🛠 Tech Stack

| Layer | Technology |
|------|------------|
| Frontend | Streamlit |
| Backend | Python |
| NLP Models | Hugging Face Transformers |
| Database | Postgresql |
| Security | JWT, bcrypt |
| Deployment | Docker |

---

## 🤖 Models Used

| Model / Tool | Purpose                                                                        |
| ------------ | ------------------------------------------------------------------------------ |
| Pegasus      | Abstractive text summarization (especially long documents, news articles)      |
| BART         | Text summarization, rewriting, and text generation (denoising autoencoder)     |
| FLAN-T5      | Paraphrasing, question answering, translation, and instruction-based NLP tasks |
| NLTK         | Text preprocessing (tokenization, stemming, POS tagging, etc.)                 |
| textstat     | Readability scoring (Flesch Reading Ease, Grade Level, etc.)                   |

---

📝 Usage Guide

 1.Register / Login
<img width="1908" height="890" alt="Screenshot 2026-03-18 154726" src="https://github.com/user-attachments/assets/58ad0227-5abf-4546-8171-70df13e8b02e" />
 2.Input text or upload file
<img width="1909" height="894" alt="Screenshot 2026-03-18 160515" src="https://github.com/user-attachments/assets/8f97831c-51cc-4e8e-a616-104d5ef2738f" />
3.Select feature (summarization/paraphrasing)
<img width="1909" height="886" alt="Screenshot 2026-03-18 160645" src="https://github.com/user-attachments/assets/3fdce1f2-beaf-4e69-85fb-0f3700252e88" />
4.Adjust settings
<img width="1917" height="959" alt="Screenshot 2026-03-23 102005" src="https://github.com/user-attachments/assets/2e77174a-4a15-4c8d-89b8-efc15e0f8b7a" />
5.Generate result
<img width="1912" height="963" alt="image" src="https://github.com/user-attachments/assets/a901818d-0b24-459a-aca3-d1820286f59d" />
6.History
<img width="1911" height="960" alt="image" src="https://github.com/user-attachments/assets/7592ea85-3b14-4c68-9c20-db8c687ea680" />

📊 Datasets & Evaluation
Used for testing and model improvement:
Dataset
Usage
WikiAuto
Text simplification
Newsela
Grade-level rewriting
ASSET
Paraphrasing benchmark


👥 Team 

| Name              | Role                 | Responsibilities                          |
|-------------------|----------------------|-------------------------------------------|
| 1. Ch. Bhavana    | Project Lead         | Project design, coordination, and deployment, UI/UX |
| 2. K. Akshara       | ML Engineer          | Model tuning, optimization, and evaluation | 
| 3. A. Lavanya       | Backend Developer    | API development and database management    | 
| 4. N. Raja  | Full Stack Developer | Built the entire application, AI integration | 
