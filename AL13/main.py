from Voz import falar, setRate
from Tempo import data_atual, hora_atual
import pause
import os
import webbrowser
import speech_recognition as sr
import parselmouth
from random import randint
from Api import *

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
                setRate(100)
                saud = "Boa Noite! Vamo querer dormir?"
            case 2:
                setRate(100)
                saud = "Que sono cara, hoje eu não tô afim não."
    falar(saud)
    setRate()

def escutar_mic(pergunta = "Aguardando Sua Fala..."):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            falar(pergunta)
            r.pause_threshold = 1
            try:
                audio = r.listen(source, timeout=5)
                falar("Processando...")
                comando = r.recognize_google(audio, language="pt-BR")
                print(f"Comando: {comando}")
            except sr.UnknownValueError:
                falar("Desculpe, não entendi.")
                continue
            else:
                return comando.lower()

if __name__ == "__main__":
    boas_vindas()
    while True:
        fala = escutar_mic()
        if any(finalizar in fala for finalizar in comandoFinalizar):
            falar("Até.")
            break
        else:
            if any(abrir in fala for abrir in comandoAbrir):
                while True:
                    if "navegador" in fala:
                        pesquisa = escutar_mic("O que você deseja pesquisar no navegador?")
                        if "no" in pesquisa:
                            pesquisa.split("no")
                            pesq = pesquisa[0].strip()
                            site = pesquisa[1].strip()
                            if site.lower() in sitesNavegador:
                                webbrowser.open(f"https://www.{site}.com/search?q=f{pesq}")
                        else:
                            webbrowser.open(f"https://www.google.com/search?q={pesquisa.replace(" ", "+")}")
                    if any(musica in fala for musica in comandoMusica):
                        app = escutar_mic("Qual aplicativo de música eu devo abrir?").lower()
                        try: 
                            os.system(f"{app}.exe")
                        except:
                            falar("Ocorreu um erro ao abrir esse aplicativo")
                        else:
                            resp = escutar_mic("Quer que eu pesquise alguma música?")
                            if not any(negar in resp for negar in comandoNegar):
                                if any(aceitar in resp for aceitar in comandoAceitar):
                                    resp = escutar_mic("Qual música?")
                                os.system(f"start spotify:search:{resp.replace(" ", "%20")}")
                    
                    if any(explorador in fala for explorador in comandoExplorador):
                        os.system("explorer")
                    if any(nota in fala for nota in comandoNotas):
                        os.system("notepad")
                    else: 
                        fala = escutar_mic("O que você deseja abrir?")
                        if "nada" in fala: break
                        continue
                    break
            if any(negar in escutar_mic("Mais alguma coisa?") for negar in comandoNegar): 
                falar("Ok, até mais tarde.")
                exit()
            else:
                falar("O que você deseja?")
