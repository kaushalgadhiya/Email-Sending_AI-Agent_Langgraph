import os
import requests
import sounddevice as sd
import scipy.io.wavfile as wav
import tempfile
from dotenv import load_dotenv

def capture_voice():
    """
    Transcribe speech using Google's speech recognition.
    """
    try:
        import speech_recognition as sr
        
        print("🎤 Using Google Speech Recognition...")
        recognizer = sr.Recognizer()
        
        with sr.Microphone() as source:
            print("🎙️ Speak now...")
            audio = recognizer.listen(source, timeout=5)
            
            text = recognizer.recognize_google(audio)
            print(f"📝 Transcribed with Google: {text}")
            return text
    except Exception as e:
        print(f"❌ Google speech recognition failed: {e}")
        return ""
