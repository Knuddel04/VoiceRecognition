from re import T
import speech_recognition as sr
from gtts import gTTS
import os
import playsound
import webbrowser

r = sr.Recognizer()


def erkennung():
    global text, audio
    with sr.Microphone() as source:
        print("Listening...")
        
        audio = r.listen(source)
        text = r.recognize_google(audio, language="en_US")
        print(text)

def music():
    if text == "play music":
        musi = "your music is playing"
        tts = gTTS(musi)
        if os.path.exists(r"C:\Users\hg04\Documents\Programmieren\AA_Python\Projekte\Voice-erkennung\sprache.mp3"):
            os.remove(r"C:\Users\hg04\Documents\Programmieren\AA_Python\Projekte\Voice-erkennung\sprache.mp3")
        filename = r"C:\Users\hg04\Documents\Programmieren\AA_Python\Projekte\Voice-erkennung\sprache.mp3"
        tts = tts.save(filename)
        playsound.playsound(filename)
        

def light():
    if text == "turn the lights on":
        webbrowser.open("https://www.bleiben-sie-sicher.de/wp-content/uploads/2016/12/EswerdeLicht-800x480.png")
        lights = "lights are on now"
        tts = gTTS(lights)
        if os.path.exists(r"C:\Users\hg04\Documents\Programmieren\AA_Python\Projekte\Voice-erkennung\sprache.mp3"):
            os.remove(r"C:\Users\hg04\Documents\Programmieren\AA_Python\Projekte\Voice-erkennung\sprache.mp3")
        filename = r"C:\Users\hg04\Documents\Programmieren\AA_Python\Projekte\Voice-erkennung\sprache.mp3"
        tts = tts.save(filename)
        playsound.playsound(filename)

def yt():
    if text == "YouTube":
        webbrowser.open("https://www.youtube.com/?gl=DE")
        yot = "opened youtube"
        tts = gTTS(yot)
        if os.path.exists(r"C:\Users\hg04\Documents\Programmieren\AA_Python\Projekte\Voice-erkennung\sprache.mp3"):
            os.remove(r"C:\Users\hg04\Documents\Programmieren\AA_Python\Projekte\Voice-erkennung\sprache.mp3")
        filename = r"C:\Users\hg04\Documents\Programmieren\AA_Python\Projekte\Voice-erkennung\sprache.mp3"
        tts = tts.save(filename)
        playsound.playsound(filename)

def google():
    if text == "Google":
        webbrowser.open("https://www.google.com")
        gog = "opened google"
        tts = gTTS(gog)
        if os.path.exists(r"C:\Users\hg04\Documents\Programmieren\AA_Python\Projekte\Voice-erkennung\sprache.mp3"):
            os.remove(r"C:\Users\hg04\Documents\Programmieren\AA_Python\Projekte\Voice-erkennung\sprache.mp3")
        filename = r"C:\Users\hg04\Documents\Programmieren\AA_Python\Projekte\Voice-erkennung\sprache.mp3"
        tts = tts.save(filename)
        playsound.playsound(filename)

while True:
    erkennung()
    music()
    light()
    yt()
    google()