
# 🤖 Alexa – The WhatsApp Chatbot

A voice-controlled WhatsApp assistant built with Python. Say the wake word **"Alexa"**, and let your bot open WhatsApp Web, read messages using OCR, and reply intelligently via OpenAI. All hands-free.

---

## 📌 Features

- 🔊 Wake-word activation using **"Alexa"**
- 🌐 Automatically opens WhatsApp Web
- 📸 Uses screenshots + OCR to read received messages
- 🧠 Uses OpenAI to generate replies to those messages
- ⌨️ Automatically types and sends replies in the chat
- 🎙️ Text-to-speech feedback for commands and responses

---

## 🛠️ Technologies Used

- `speech_recognition` – Voice recognition
- `pyaudio` – Microphone input
- `webbrowser` – Open WhatsApp Web
- `gTTS` & `playsound` – Text-to-speech responses
- `pyautogui` – UI automation (typing and clicking)
- `pytesseract` – OCR to extract text from WhatsApp chat
- `pygetwindow` – Focusing on WhatsApp window
- `ctypes` – DPI awareness for accurate UI positioning
- `openai` – Natural language response generation
- `os`, `sys`, `time`

---

## ⚙️ Setup Instructions

### 1. Install Python Dependencies

```bash
pip install speechrecognition pyaudio gtts playsound pyautogui pytesseract pygetwindow openai
```

### 2. Install Tesseract OCR

Download and install from: https://github.com/tesseract-ocr/tesseract

> After installation, update the path in the script:
```python
pytesseract.pytesseract.tesseract_cmd = "C:\Program Files\Tesseract-OCR\tesseract.exe"
```

### 3. Setup OpenAI API

- You'll need an OpenAI API key.
- Store and use it in your `ask_openai()` function (via `client.py`).

---

## 🚀 How to Use

1. **Run your Python script.**
2. Say **"Alexa"** to activate the assistant.
3. Say **"Open WhatsApp"** – it will open [https://web.whatsapp.com](https://web.whatsapp.com)
4. Manually open a chat with the person you want to message.
5. Say **"Alexa"** again to reinitialize listening.
6. Say **"Chat now"** – the bot will:
   - Take a screenshot of the chat window.
   - Extract the latest message using OCR.
   - Get a smart reply using OpenAI.
   - It will type and send the reply on your behalf.
7. Say **"Exit"** anytime to close the program.

---

## 📌 Notes

- Keep screen scaling to **100%** (DPI-aware mode enabled via `ctypes`)
- The bot uses **hardcoded mouse coordinates**:
  ```python
  pyautogui.click(x=1198, y=1029)
  ```
  You may need to adjust these based on your screen size.
- It works best on **desktop/laptop** screens with standard WhatsApp Web layout.
- Ensure mic access permissions are enabled.

---

## 🚧 To-Do / Future Plans

- Detect and select a contact using voice
- Improve error handling and retry logic
- Make screen position detection dynamic
- Add GUI toggle to start/stop bot


Thank you
