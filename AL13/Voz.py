import pyttsx3
import random as rd

def falar(fala):
    txt_speech.say(str(fala))
    print(str(fala))
    txt_speech.runAndWait()

def setRate(rate = 150):
    txt_speech.setProperty('rate', rate)

txt_speech = pyttsx3.init()
voices = txt_speech.getProperty('voices')
rand = rd.randint(0, 100)

txt_speech.setProperty('voice', voices[0].id)
setRate()