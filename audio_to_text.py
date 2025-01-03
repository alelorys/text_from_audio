import speech_recognition as sr 
import whisper
from os import path

def audio_to_text(audio):
    model = whisper.load_model("medium")
    result = model.transcribe(audio)
    return result["text"]
