import speech_recognition as sr
import pyaudio
import webbrowser
import time
from gtts import gTTS
import playsound
import pyautogui
import pytesseract
import pygetwindow as gw 
import ctypes
from client import ask_openai
import sys
import os

# Set the path to tesseract.exe manually (update if your path is different)
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

# we use cttypes here to set our program to use window only in 100% scaling
ctypes.windll.user32.SetProcessDPIAware()

recognizer = sr.Recognizer()


wake_word = "alexa"

def speak(text):
    try:
        filename = "temp_voice.mp3"
        tts = gTTS(text=text, lang='en')
        tts.save(filename)
        playsound.playsound(filename)
        time.sleep(0.5)  # wait before deletion to avoid access issues
        os.remove(filename)
    except Exception as e:
        print("TTS Error:", e)
            
def focus_whatsapp():
    try:
        for window in gw.getWindowsWithTitle('WhatsApp'):
            if window.isMinimized:
                window.restore()
            window.activate()
            time.sleep(0.5)
            return True
        print("WhatsApp window not found.")
        return False
    except Exception as e:
        print("Error focusing WhatsApp:", e)
        return False

# Main chat logic
def chat():
    try:
        while True:
            print("taking screenshots") 
            screen_width, screen_height = pyautogui.size()

            left_crop_percent = 0.29
            left = int(screen_width * left_crop_percent)
            width = int(screen_width * (1 - left_crop_percent))
            top = 0
            height = screen_height

            screenshot = pyautogui.screenshot(region=(left, top, width, height))
            screenshot.save("cropped_screenshot.png")

            text = pytesseract.image_to_string(screenshot)
            print("Extracted Text:\n", text)
            time.sleep(5)

            if text.strip():
                response = AIprocess(text)
                print("AI Assistant:", response)
                time.sleep(1)

                # Focus WhatsApp before typing
                if not focus_whatsapp():
                    speak("Couldn't find WhatsApp window.")
                    return

                pyautogui.click(x=1198, y=1029)
                time.sleep(0.5)

                pyautogui.typewrite(response, interval=0.03)

                pyautogui.press("enter")
            else:
                print("No text detected.")
            time.sleep(5)
       
    except Exception as e:
        print("Error during chat processing:", e)

def listen_for_wake_word():
    with sr.Microphone() as source:
        print("adjusting background noise")
        print("listening for wake word")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio).lower()
            print(f"Listening for: '{wake_word}', Heard: '{command}'")
            print(f"command received: {command}")
            return command == wake_word
        except sr.UnknownValueError:
            return False

def listen_for_command():
    with sr.Microphone() as source:
        print("listening for command")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)
        except:
            speak("timed out")
            return

    try:
        command = recognizer.recognize_google(audio)
        print(f"Command received: {command}")
        speak(f"initializing command: {command}")

        if "open" in command.lower():
            site = command.replace("open ", "").strip()
            if "." not in site:
                site += ".com"
            url = "https://" + site
            webbrowser.open(url)

        elif "chat now" in command.lower():
            chat()
            
        elif "exit" in command.lower():
            speak("exiting program as per user request")
            sys.exit()

    except SystemExit:
           raise
    except:
        print("some error happened in recognizing")


def AIprocess(text):
    try:
        response = ask_openai(text)
        return response
    except Exception as e:
        speak("Some error happened in processing your request.")
        print("Error:", e)


# Main loop
while True:
    print("waiting for wake word")
    if listen_for_wake_word():
        speak("yes, how can I help?")
        listen_for_command()
        time.sleep(1)
