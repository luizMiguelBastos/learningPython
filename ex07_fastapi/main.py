from fastapi import FastAPI, HTTPException
from ex06_api.cotacao import buscar_cotacao, converter

app = FastAPI()

@app.get("/")
def health_check():
    return {"status": "ok"}

@app.get("/converter")
def transformar(reais: float):
    try:
        cotacao_atual = buscar_cotacao()
    except ValueError:
        raise HTTPException(status_code=502, detail=("Serviço de cotação indisponível"))
    try:
        valor_convertido = converter(reais, cotacao_atual)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    resposta = {"reais": reais, "cotacao_atual": cotacao_atual, "valor_convertido": round(valor_convertido, 2)}
    return resposta





