from Voz import falar, setRate
from Tempo import data_atual, hora_atual
import pause
import os
import speech_recognition as sr
import parselmouth
from random import randint

def boas_vindas():
    data = data_atual()
    hora = int(hora_atual().split(":")[0])
    minutos = int(hora_atual().split(":")[1])
    intsaud = randint(0, 2)
    saud = ""
    if 12 <= hora <= 18:
        match intsaud:
            case 0:
                saud = "Boa Tarde! Que bom ter você de volta!"
            case 1:
                saud = "Boa Tarde! Já Voltou?"
            case 2:
                saud = "Eai, tarde boa?"
    elif hora < 12: 
        match intsaud:
            case 0:
                saud = "Bom Dia! O que temos para hoje?!"
            case 1:
                saud = "Bom Dia, muitos pedidos hoje?!"
            case 2:
                saud = "Hoje é só 'Dia'."
    else: 
        match intsaud:
            case 0:
                saud = "Buenas Noches! Como estás?"
            case 1:
                setRate(50)
                saud = "Boa Noite! Vamo querer dormir?"
            case 2:
                saud = "Que sono cara, hoje eu não tô afim não."
    falar(saud)
    setRate()

def escutar_mic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        falar("Aguardando Sua Fala...")
        r.pause_threshold = 1
        try:
            audio = r.listen(source)
            falar("Processando...")
            comando = r.recognize_google(audio, language="pt-BR")
            falar(f'Você Disse "{comando}"?')
        except sr.UnknownValueError:
            falar("Desculpe, não entendi.")

if __name__ == "__main__":
    boas_vindas()
