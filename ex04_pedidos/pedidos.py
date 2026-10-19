pedidos = [
    {"id": 1, "cliente": "Miguel", "valor": 200, "status": "pago"},
    {"id": 2, "cliente": "Rodson", "valor": 175, "status": "pendente"},
    {"id": 3, "cliente": "Hernandes", "valor": 150, "status": "cancelado"},
    {"id": 4, "cliente": "Miguel", "valor": 125, "status": "pago"}
]

def buscar_pedido(pedidos,id_pedido):
    for pedido in pedidos:
        if pedido["id"] == id_pedido:
            return pedido
    raise ValueError("Pedido não encontrado")

def total_por_status(pedidos, status):
    total = 0
    for pedido in pedidos:
        if pedido["status"] == status:
            total += pedido["valor"]
    return total

def atualizar_status(pedidos, id_pedido, novo_status):
    if novo_status not in ["pago", "cancelado", "pendente"]:
        raise ValueError("Pedido inválido")
    pedido = buscar_pedido(pedidos, id_pedido)
    if pedido["status"] == "cancelado":
        raise ValueError("Pedido já cancelado")
    pedido["status"] = novo_status

def total_por_cliente(pedidos):
    total = {}
    for pedido in pedidos:
        if pedido["cliente"] in total:
            total[pedido["cliente"]] += pedido["valor"]
        else:
            total[pedido["cliente"]] = pedido["valor"]
    return total

print(buscar_pedido(pedidos, 1))

try:
    print(buscar_pedido(pedidos, 10))
except ValueError as e:
    print(e)

print(total_por_status(pedidos, "pago"))

(atualizar_status(pedidos, 2, "pago"))
print(buscar_pedido(pedidos, 2))

try:
    atualizar_status(pedidos, 2, "invalido")
except ValueError as e:
    print(e)

try:
    atualizar_status(pedidos, 3, "cancelado")
except ValueError as e:
    print(e)

print(total_por_cliente(pedidos))