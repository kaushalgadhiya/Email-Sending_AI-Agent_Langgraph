import os
import requests
import sounddevice as sd
import scipy.io.wavfile as wav
import tempfile
from dotenv import load_dotenv
import streamlit as st

def capture_voice():
    """
    Transcribe speech using Google's speech recognition.
    """
    try:
        import speech_recognition as sr
        
        st.write("🎤 Using Google Speech Recognition...")
        recognizer = sr.Recognizer()
        
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            st.write("🎙️ Speak now...")
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)            
            text = recognizer.recognize_google(audio)
            st.write(f"📝 Transcribed with Google: {text}")
            return text
    except Exception as e:
        st.write(f"❌ Google speech recognition failed: {e}")
        return ""
