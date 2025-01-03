from gtts import gTTS
import os

def text_to_audio(text, lang):
    print("Convert text to speech")
    return gTTS(text=text, lang=lang)
