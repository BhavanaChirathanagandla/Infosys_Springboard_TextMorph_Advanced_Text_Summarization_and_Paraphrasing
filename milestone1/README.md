# Milestone 1 – Secure User Authentication System

## Project Title
TextMorph – Advanced Text Summarization and Paraphrasing

## Internship
Infosys Springboard Internship 6.0 – Batch 13

## Description

In Milestone 1, a secure User Authentication System was developed using Streamlit, JWT (JSON Web Token), and SQLite database.

This authentication module serves as the foundation for the TextMorph project and will later integrate text summarization and paraphrasing features.

The system ensures secure user registration, login authentication, dashboard access control, and password recovery using security questions.

##  Features Implemented

### 1️. User Signup
- Username validation
- Email format validation
- Alphanumeric password validation (minimum 8 characters)
- Confirm password matching
- Security question selection
- Security answer storage
- JWT token generation after successful signup

<img width="1313" height="859" alt="signup_page" src="https://github.com/user-attachments/assets/ec4feaa6-e460-47fd-ae6a-b2e23efa569a" />


### 2️. Secure Login
- Email verification
- Password verification
- JWT-based session management
- Dashboard redirection after successful login

<img width="1207" height="911" alt="Dashboard_page" src="https://github.com/user-attachments/assets/482c85a5-913a-4f2b-a9c9-ec444ebdd865" />


### 3️. Dashboard
- Welcome message with username
- Sidebar with navigation
- Logout functionality
- Protected route using JWT validation



### 4️. Forgot Password Flow
- Email verification
- Display stored security question
- Security answer validation
- Secure password reset functionality

<img width="1872" height="504" alt="Forgot_pwd page1" src="https://github.com/user-attachments/assets/8dec82ad-93ed-4053-a6e1-12b6de7a7799" />

<img width="1837" height="681" alt="Forgot_pwd page2" src="https://github.com/user-attachments/assets/479f400e-cab0-42de-b46d-2939084f7ff3" />

<img width="1853" height="688" alt="Reset_pwd page" src="https://github.com/user-attachments/assets/acfc1bd6-16d2-4b98-9624-de323819d7e8" />




### 5️. JWT Authentication
- Token generation using HS256 algorithm
- Expiration-based token validation
- Automatic session expiry handling

##  Technologies Used

- Python
- Streamlit
- JWT (PyJWT)
- SQLite Database
- Regular Expressions (Email Validation)

##  Database Structure

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    email TEXT UNIQUE,
    password TEXT,
    security_question TEXT,
    security_answer TEXT
);
