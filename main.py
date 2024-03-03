import hashlib
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/processar_dados")
def calcular_hash(nome: str, telefone: str, email: str):
    if not (nome and telefone and email):
        raise HTTPException(status_code=400, detail='Erro: Nome, telefone e email são campos obrigatórios.')
    
    # Calcular hashes SHA-256
    nome_hash = hashlib.sha256(nome.encode()).hexdigest()
    telefone_hash = hashlib.sha256(telefone.encode()).hexdigest()
    email_hash = hashlib.sha256(email.encode()).hexdigest()

    # Retornar os hashes como resposta
    resposta = {
        'nome_hash': nome_hash,
        'telefone_hash': telefone_hash,
        'email_hash': email_hash
    }

    return resposta
