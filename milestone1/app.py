
# ---------------- DATABASE CONNECTION ----------------
import sqlite3 # Added import statement
conn = sqlite3.connect("users.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    email TEXT UNIQUE,
    password TEXT,
    security_question TEXT,
    security_answer TEXT
)
''')
conn.commit()

import streamlit as st
import jwt
import datetime
import time
import re
if 'page' not in st.session_state:
    st.session_state['page'] = 'login'

# --- Configuration ---
SECRET_KEY = "super_secret_key_for_demo"  # In production, use environment variable
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
# --- JWT Utils ---
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
# --- Validation Utils ---
def is_valid_email(email):
    # Regex for standard email format
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    try:
        if re.match(pattern, email):
            return True
    except:
        return False
    return False
def is_valid_password(password):
    # Alphanumeric check and min length 8
    if len(password) < 8:
        return False
    if not password.isalnum():
        return False
    return True
# --- Session State Management ---
if 'jwt_token' not in st.session_state:
    st.session_state['jwt_token'] = None
if 'page' not in st.session_state:
    st.session_state['page'] = 'login'
# Mock Database (In-memory for demo)
# Structure: {email: {'password': password, 'username': username, ...}}
# Also store usernames separately for quick check: {username: email}
if 'users' not in st.session_state:
    st.session_state['users'] = {}
if 'usernames' not in st.session_state:
    st.session_state['usernames'] = set()
# --- Styling ---
st.set_page_config(
    page_title="Infosys SpringBoard Intern",
    page_icon="🤖",
    layout="wide"
)


st.markdown('''
    <style>
        .stApp {
            background-color: #0E1117;
        }
        h1 {
            text-align: center;
            color: #4F8BF9;
            font-family: 'Inter', sans-serif;
            margin-bottom: 0.5rem;
        }
        h3 {
            text-align: center;
            color: #FAFAFA;
            font-weight: 300;
            margin-top: 0;
            font-size: 1.2rem;
        }
        .stButton>button {
            width: 100%;
            border-radius: 8px;
            height: 3em;
            background-color: #4F8BF9;
            color: white;
            font-weight: bold;
            border: none;
        }
        .stButton>button:hover {
            background-color: #3b6ccf;
        }
        div[data-testid="stSidebar"] {
            background-color: #262730;
        }
        .error-box {
            background-color: #ffcccc;
            color: #cc0000;
            padding: 10px;
            border-radius: 5px;
            margin-bottom: 10px;
        }
        /* Chat message styling */
        .user-msg {
            text-align: right;
            background-color: #262730;
            color: white;
            padding: 10px;
            border-radius: 10px;
            margin: 5px;
            display: inline-block;
            max-width: 80%;
            float: right;
            clear: both;
        }
        .bot-msg {
            text-align: left;
            background-color: #4F8BF9;
            color: white;
            padding: 10px;
            border-radius: 10px;
            margin: 5px;
            display: inline-block;
            max-width: 80%;
            float: left;
            clear: both;
        }
    </style>
''', unsafe_allow_html=True)
# --- Views ---
def login_page():
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.title("Infosys SpringBoard Intern")
        st.markdown("<h3>Please sign in to continue</h3>", unsafe_allow_html=True)

        with st.form("login_form"):
            email = st.text_input("Email Address")
            password = st.text_input("Password", type="password")
            submitted = st.form_submit_button("Sign In")

            if submitted:
                if email in st.session_state['users'] and                    st.session_state['users'][email]['password'] == password:

                    username = st.session_state['users'][email]['username']
                    token = create_access_token({"sub": email, "username": username})
                    st.session_state['jwt_token'] = token
                    st.success("Login successful!")
                    time.sleep(0.5)
                    st.rerun()
                else:
                    st.error("Invalid email or password")

        st.markdown("---")

        # ✅ MOVE BUTTONS INSIDE CENTER COLUMN
        c1, c2 = st.columns(2)

        with c1:
            if st.button("Forgot Password?"):
                st.session_state['page'] = 'forgot'
                st.rerun()

        with c2:
            if st.button("Create an Account"):
                st.session_state['page'] = 'signup'
                st.rerun()

def signup_page():
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.title("Create Account")

        with st.form("signup_form"):
            username = st.text_input("Username (Required)")
            email = st.text_input("Email Address (@domain.com required)")
            password = st.text_input("Password (min 8 chars, alphanumeric)")
            confirm_password = st.text_input("Confirm Password", type="password")
            security_question = st.selectbox(
              "Select Security Question",
              [
                "What is your pet name?",
                "What is your mother’s maiden name?",
                "What is your favorite movie?"
              ]
            )

            security_answer = st.text_input("Security Answer (Required)")

            submitted = st.form_submit_button("Sign Up")

            if submitted:
                errors = []

                # Username Validation
                if not username:
                    errors.append("Username is mandatory.")
                elif username in st.session_state['usernames']:
                    errors.append(f"Username '{username}' is already taken.")

                # Email Validation
                if not email:
                    errors.append("Email is mandatory.")
                elif not is_valid_email(email):
                    errors.append("Invalid Email format (e.g. user@domain.com).")
                elif email in st.session_state['users']:
                    errors.append(f"Email '{email}' is already registered.")

                # Password Validation
                if not password:
                    errors.append("Password is mandatory.")
                elif not is_valid_password(password):
                    errors.append("Password must be at least 8 characters long and contain only alphanumeric characters.")

                # Confirm Password
                if password != confirm_password:
                    errors.append("Passwords do not match.")
                # Security Answer Validation
                if not security_answer:
                  errors.append("Security Answer is mandatory.")


                if errors:
                    for error in errors:
                        st.error(error)
                else:
                    # Success
                    st.session_state['users'][email] = {
    'password': password,
    'username': username,
    'security_question': security_question,
    'security_answer': security_answer.lower()
}

                    st.session_state['usernames'].add(username)

                    # Auto-login after signup
                    token = create_access_token({"sub": email, "username": username})
                    st.session_state['jwt_token'] = token
                    st.success("Account created successfully!")
                    time.sleep(1)
                    st.rerun()

        st.markdown("---")
        if st.button("Back to Login"):
            st.session_state['page'] = 'login'
            st.rerun()
def forgot_password_page():
    st.title("Forgot Password")

    email = st.text_input("Enter your registered email")

    if email:
        if email in st.session_state['users']:

            security_question = st.session_state['users'][email]['security_question']
            st.write("Security Question:")
            st.info(security_question)

            answer = st.text_input("Enter your answer")

            if st.button("Verify Answer"):
                correct_answer = st.session_state['users'][email]['security_answer']

                if answer.lower() == correct_answer:
                    st.session_state['reset_email'] = email
                    st.session_state['verified'] = True
                    st.success("Answer verified! Set new password.")
                else:
                    st.error("Incorrect answer.")

        else:
            st.error("Email not found.")

    # Reset password section
    if st.session_state.get('verified'):

        new_password = st.text_input("New Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")

        if st.button("Reset Password"):
            if new_password == confirm_password:
                st.session_state['users'][st.session_state['reset_email']]['password'] = new_password
                st.success("Password reset successful!")
                st.session_state['verified'] = False
            else:
                st.error("Passwords do not match.")

    st.markdown("---")
    if st.button("Back to Login"):
        st.session_state['page'] = 'login'
        st.rerun()

def dashboard_page():
    token = st.session_state.get('jwt_token')
    payload = verify_token(token)

    if not payload:
        st.session_state['jwt_token'] = None
        st.warning("Session expired or invalid. Please login again.")
        time.sleep(1)
        st.rerun()
        return
    username = payload.get("username", "User")

    with st.sidebar:
        st.title("🤖 LLM")
        st.markdown("---")
        if st.button("➕ New Chat", use_container_width=True):
             st.info("Started new chat!")

        st.markdown("### History")
        st.markdown("- Project analysis")
        st.markdown("- NLP")
        st.markdown("---")
        st.markdown("### Settings")
        if st.button("Logout", use_container_width=True):
            st.session_state['jwt_token'] = None
            st.rerun()
    # Main Content - Chat Interface
    st.title(f"Welcome, {username}!")
    st.markdown("### How can I help you today?")

    # Chat container (Simple simulation)
    chat_placeholder = st.empty()

    with chat_placeholder.container():
        st.markdown('<div class="bot-msg">Hello! I am LLM. Ask me anything about LLM!</div>', unsafe_allow_html=True)
        # Assuming we might store chat history in session state later

    # User input area at bottom
    with st.form(key='chat_form', clear_on_submit=True):
        col1, col2 = st.columns([6, 1])
        with col1:
            user_input = st.text_input("Message LLM...", placeholder="Ask me anything about LLM...", label_visibility="collapsed")
        with col2:
            submit_button = st.form_submit_button("Send")

        if submit_button and user_input:
             # Just append messages visually for demo
             st.markdown(f'<div class="user-msg">{user_input}</div>', unsafe_allow_html=True)
             st.markdown('<div class="bot-msg">I am a demo bot. I received your message!</div>', unsafe_allow_html=True)
# --- Main App Logic ---
token = st.session_state.get('jwt_token')
if token:
    if verify_token(token):
        dashboard_page()
    else:
        st.session_state['jwt_token'] = None
        st.session_state['page'] = 'login'
        st.rerun()
else:
    if st.session_state['page'] == 'signup':
        signup_page()

    elif st.session_state['page'] == 'forgot':
        forgot_password_page()

    else:
        login_page()

