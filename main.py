import hashlib
from fastapi import FastAPI, HTTPException
import requests
import json
import datetime

app = FastAPI(title="API Marcação de Pixel",
    description="Esta é uma API para processar dados e enviar eventos para o Pixel da Meta. Criado por Jhonnatan Santana",
    version="1.0")

@app.post("/processar_dados")
def marcar_pixel(nome: str, telefone: str, email: str, nomeevento: str, tokenmeta: str, idpixel: str, fonte: str):
    if not (nome and telefone and email):
        raise HTTPException(status_code=400, detail='Erro: Nome, telefone e email são campos obrigatórios.')
    
    # Calcular hashes SHA-256
    nome_hash = hashlib.sha256(nome.encode()).hexdigest()
    telefone_hash = hashlib.sha256(telefone.encode()).hexdigest()
    email_hash = hashlib.sha256(email.encode()).hexdigest()

    if nome_hash and telefone_hash and email_hash:
        url = f"https://graph.facebook.com/v18.0/{idpixel}/events?&access_token={tokenmeta}"

        agora = datetime.datetime.now()
        data_hora_formatada = agora.isoformat()
   
        dados = {
        "data": [
        {   
            "action_source": "website",
            "event_name": nomeevento,
            "event_time": data_hora_formatada,
            "user_data": {
                "em": email_hash,
                "ph": telefone_hash,
                "fn": [
                    nome_hash
                ]
            },
            "custom_data": {
                "content_name": fonte
            }
        }
    ]
}


        dados_json = json.dumps(dados)
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, data=dados_json, headers=headers)

        if response.status_code == 200:
           return response.status_code
        else:
            raise HTTPException(status_code=response.status_code, detail='Erro: ao enviar info ao facebook')

@app.post("/teste")
def teste_pixel(id_test: str, nome: str, telefone: str, email: str, nomeevento: str, tokenmeta: str, idpixel: str, fonte: str):
    if not (nome and telefone and email):
        raise HTTPException(status_code=400, detail='Erro: Nome, telefone e email são campos obrigatórios.')
    
    # Calcular hashes SHA-256
    nome_hash = hashlib.sha256(nome.encode()).hexdigest()
    telefone_hash = hashlib.sha256(telefone.encode()).hexdigest()
    email_hash = hashlib.sha256(email.encode()).hexdigest()

    if nome_hash and telefone_hash and email_hash:
        url = f"https://graph.facebook.com/v18.0/{idpixel}/events?&access_token={tokenmeta}"

        agora = datetime.datetime.now()
        data_hora_formatada = agora.isoformat()
   
        dados = {
        "data": [
        {   
            "action_source": "website",
            "event_name": nomeevento,
            "event_time": data_hora_formatada,
            "user_data": {
                "em": email_hash,
                "ph": telefone_hash,
                "fn": [
                    nome_hash
                ]
            },
            "custom_data": {
                "content_name": fonte
            }
        }
    ],
    "test_event_code": id_test
}


        dados_json = json.dumps(dados)
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, data=dados_json, headers=headers)

        if response.status_code == 200:
           return response.status_code
        else:
            raise HTTPException(status_code=response.status_code, detail='Erro: ao enviar info ao facebook')
