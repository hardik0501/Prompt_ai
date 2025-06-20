import os
import json
import random
import streamlit as st
import google.generativeai as genai

# Directly set Gemini API key here
GEMINI_API_KEY = "your api "
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

SYSTEM_PROMPT = """
You are SmartCommand AI, an expert assistant for controlling laptops using Python.
Your job is to convert the user's instruction into a valid Python command using os or webbrowser modules.
Supported commands:
- open notepad, calculator, or any common app
- open Chrome or websites like YouTube, Spotify, WhatsApp Web
- create or delete folders/files
- play a song on YouTube
- show current folder files
Only return executable Python code. No explanation. No extra text. Just the code.
"""

USER_FILE = "users.json"
command_history = []


def load_users():
    if not os.path.exists(USER_FILE):
        with open(USER_FILE, "w") as f:
            json.dump({}, f)
    with open(USER_FILE, "r") as f:
        return json.load(f)


def save_users(users):
    with open(USER_FILE, "w") as f:
        json.dump(users, f, indent=2)


def request_otp(username, password):
    users = load_users()
    if username in users and users[username] == password:
        otp = str(random.randint(100000, 999999))
        st.session_state["otp_user"] = username
        st.session_state["otp_code"] = otp
        st.session_state["otp_requested"] = True
        st.success(f"✅ OTP sent to your email (simulated). OTP is: {otp}")
    else:
        st.error("❌ Invalid credentials")


def verify_otp(otp_input):
    if st.session_state.get("otp_code") == otp_input:
        st.session_state["logged_in"] = True
        st.session_state["username"] = st.session_state.get("otp_user", "")
        st.session_state["otp_requested"] = False
        return True
    return False


def register_user(username, password):
    users = load_users()
    if username in users:
        return "⚠️ Username already exists."
    users[username] = password
    save_users(users)
    return "✅ Registered successfully!"


def get_command(user_input):
    try:
        response = model.generate_content([SYSTEM_PROMPT, user_input])
        code = response.text.strip().strip("`").replace("python", "").strip()
        try:
            exec(code)
            result = f"✅ Command executed:\n\n{code}"
        except Exception as e:
            result = f"⚠️ Error executing:\n{code}\n\nError: {e}"
    except Exception as e:
        result = f"⚠️ Gemini Error: {e}"
    command_history.append(f"> {user_input}\n{result}\n")
    return result, "\n---\n".join(command_history[::-1])


st.set_page_config(page_title="PromptPilot AI", page_icon="💻")

st.markdown("""
    <style>
        body {
            background: linear-gradient(-45deg, #0f2027, #203a43, #2c5364);
            color: white;
        }
        .stTextInput > div > div > input {
            color: #00ffcc;
            background: rgba(255,255,255,0.05);
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #00fff7;'>💻 PromptPilot AI</h1>", unsafe_allow_html=True)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "otp_requested" not in st.session_state:
    st.session_state.otp_requested = False

if not st.session_state.logged_in:
    with st.expander("🔐 Login / Register", expanded=True):
        tab1, tab2 = st.tabs(["🔓 Login", "🆕 Register"])

        with tab1:
            user = st.text_input("Username")
            pwd = st.text_input("Password", type="password")
            if not st.session_state.otp_requested:
                if st.button("Login (OTP Required)"):
                    request_otp(user, pwd)
            else:
                otp = st.text_input("Enter OTP")
                if st.button("Verify OTP"):
                    if verify_otp(otp):
                        st.success("✅ Login successful!")
                    else:
                        st.error("❌ Invalid OTP")

        with tab2:
            new_user = st.text_input("New Username")
            new_pwd = st.text_input("New Password", type="password")
            if st.button("Register"):
                result = register_user(new_user, new_pwd)
                st.info(result)
else:
    st.success(f"👋 Welcome, {st.session_state['username']}")

    if st.button("🚪 Logout"):
        st.session_state.logged_in = False
        st.experimental_rerun()

    st.markdown("### 🧠 Type your natural command below")
    user_input = st.text_input("🗨️ Command", placeholder="e.g., open Notepad")
    if st.button("⚡ Run"):
        result, hist = get_command(user_input)
        st.text_area("🤖 Result", result, height=150)
        st.text_area("📜 Command History", hist, height=300)
