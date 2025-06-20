# 💻 PromptPilot AI

PromptPilot AI is an intelligent desktop command assistant that transforms your natural language instructions into executable Python code for controlling your laptop. Powered by Google's Gemini AI and built with Streamlit, PromptPilot AI lets you automate common tasks, launch apps, and manage files with ease—all through a beautiful, secure web interface.

![PromptPilot AI Banner](https://raw.githubusercontent.com/hardik0501/Prompt_ai/main/assets/banner.png)

---

## 🚀 Features

- **Natural Language Commands**: Tell PromptPilot what you want—no code required!
- **Gemini AI-Powered**: Converts your instructions directly into safe, executable Python commands.
- **App Launcher**: Open Notepad, Calculator, Chrome, YouTube, Spotify, WhatsApp Web, and more.
- **File Operations**: Create/delete folders and files, show current directory contents.
- **YouTube Integration**: Play any song directly on YouTube.
- **Command History**: View a complete log of your executed commands and their results.
- **OTP-Based Secure Login**: Protect your data with two-step authentication.
- **Simple UI**: Clean, modern interface powered by Streamlit with custom styling.
- **Easy User Management**: Register new users and manage credentials securely.

---

## ✨ Demo

> ![PromptPilot AI Demo](https://raw.githubusercontent.com/hardik0501/Prompt_ai/main/assets/demo.gif)

---

## 🛠️ Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/hardik0501/Prompt_ai.git
   cd Prompt_ai
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Gemini API Key**
   - Replace `"your api "` in `app.py` with your actual [Google Gemini API key](https://ai.google.dev/).

4. **Run the App**
   ```bash
   streamlit run app.py
   ```

---

## 📝 Usage

- **Login/Register**: Use the sidebar to register or log in (OTP is simulated for demo purposes).
- **Enter Commands**: Type a natural language instruction (e.g., "open Notepad", "create a folder named Projects", "play Despacito on YouTube").
- **View Results**: Check the output and command history right in the app.

---

## 🔒 Security

- User credentials are stored in a local JSON file (`users.json`).
- OTP authentication adds a second layer of security (simulated email delivery).
- All code executed is generated by Gemini AI, but **always review code before running in production environments**.

---

## 🖼️ Screenshots

| Login & OTP Flow | Main Command Page |
|------------------|------------------|
| ![](assets/login.png) | ![](assets/command.png) |

---

## 🌟 Customization

- **Styling**: Modify the Streamlit markdown styles in `app.py` to change colors or background.
- **Command Set**: Expand the `SYSTEM_PROMPT` in the code to support more apps or actions.
- **Authentication**: Integrate with real email/SMS gateways for production OTP delivery.

---

## 🤖 Powered By

- [Streamlit](https://streamlit.io/)
- [Google Generative AI (Gemini)](https://ai.google.dev/)
- [Python Standard Libraries](https://docs.python.org/3/library/)

---

## 🙏 Acknowledgements

Special thanks to the open-source community and all contributors.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 👤 Author

- **Hardik Shah**  
  [GitHub](https://github.com/hardik0501) | [LinkedIn](https://linkedin.com/in/hardik0501) | [Twitter](https://twitter.com/hardik0501)

---

> “Turn your thoughts into commands. Let your laptop obey your words.”
