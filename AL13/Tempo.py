from datetime import datetime

def hora_atual():
    hora = datetime.now().hour
    minutos = datetime.now().minute
    if minutos < 10:
        minutos = f'0{minutos}'
    return f'{hora}:{minutos}'

def data_atual():
    meses = [
        "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
        "Julho", "Agosto", "Setembro", "Outubo", "Novembro", "Dezembro"
    ]

    agr = datetime.now()
    dia = agr.day
    mes = meses[agr.month - 1]
    ano = agr.year
     
    return {
        "Dia": dia,
        "Mês": mes,
        "Ano": ano
    }