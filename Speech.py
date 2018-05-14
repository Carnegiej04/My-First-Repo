import win32com.client as wincl
import speech_recognition as sr
import webbrowser as wb

speak = wincl.Dispatch("SAPI.SpVoice")

r = sr.Recognizer()
with sr.Microphone() as source:
    speak.speak("Hi Carnegie, what video do you want to watch?")
    print("Listening...")
    audio = r.listen(source)
    print("Thinking...")

try:
    words = r.recognize_google(audio)
    Speak.Speak("Ok Carnegie let's look for " + r.recognizer_google(audio) + " on Google.")
    wb.open("https://www.google.com/search?q=" + words)

except sr.UnknownValueError:
    print("Can't understand audio")
except sr.RequestError as e:
    print("Could not request results from google speech recognition service; {0}". format(e))
    

    
    
