from typing import Literal
from pydantic import BaseModel, Field
from fastapi import FastAPI, HTTPException

app = FastAPI()

class Pedido(BaseModel):
    id: int = Field(gt=0)
    nome: str = Field(min_length=1)
    valor: float = Field(gt=0)
    status: Literal ["pendente", "pago", "cancelado"]

lista_pedidos = []

@app.get("/pedidos")
def pedidos():
    return lista_pedidos

@app.post("/pedidos", status_code=201)
def adcionar_pedido(pedido: Pedido):
    for item in lista_pedidos:
        if item.id == pedido.id:
            raise HTTPException(status_code=409, detail="Id inválido")
    lista_pedidos.append(pedido)
    return pedido
