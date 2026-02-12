# Milestone 1 – Secure User Authentication System

## 📌 Project Title
TextMorph – Advanced Text Summarization and Paraphrasing

## 🎓 Internship
Infosys Springboard Internship 6.0 – Batch 13

---

## 🧾 Description

In Milestone 1, a secure User Authentication System was developed using Streamlit, JWT (JSON Web Token), and SQLite database.

This authentication module serves as the foundation for the TextMorph project and will later integrate text summarization and paraphrasing features.

The system ensures secure user registration, login authentication, dashboard access control, and password recovery using security questions.

---

## 🚀 Features Implemented

### 1️⃣ User Signup
- Username validation
- Email format validation
- Alphanumeric password validation (minimum 8 characters)
- Confirm password matching
- Security question selection
- Security answer storage
- JWT token generation after successful signup

### 2️⃣ Secure Login
- Email verification
- Password verification
- JWT-based session management
- Dashboard redirection after successful login

### 3️⃣ Dashboard
- Welcome message with username
- Sidebar with navigation
- Logout functionality
- Protected route using JWT validation

### 4️⃣ Forgot Password Flow
- Email verification
- Display stored security question
- Security answer validation
- Secure password reset functionality

### 5️⃣ JWT Authentication
- Token generation using HS256 algorithm
- Expiration-based token validation
- Automatic session expiry handling

---

## 🛠️ Technologies Used

- Python
- Streamlit
- JWT (PyJWT)
- SQLite Database
- Regular Expressions (Email Validation)

---

## 🗄️ Database Structure

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    email TEXT UNIQUE,
    password TEXT,
    security_question TEXT,
    security_answer TEXT
);
