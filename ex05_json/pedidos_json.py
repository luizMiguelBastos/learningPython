import json

def carregar(caminho):
    with open(caminho, 'r') as f:
        return json.load(f)

def salvar(caminho, pedidos):
    with open(caminho, 'w') as f:
        json.dump(pedidos, f, indent=2)

def adicionar_pedido(lista_pedidos, pedido):
    for itens in lista_pedidos:
        if itens['id'] == pedido['id']:
            raise ValueError("Id invalido")
    if pedido['valor'] <= 0:
        raise ValueError("Valor invalido")
    if pedido['status'] not in ['pendente', 'pago', 'cancelado']:
        raise ValueError("Status invalido")
    lista_pedidos.append(pedido)

pedidos = carregar('pedidos.json')
novo_pedido = {'id': 4, 'cliente': 'Matheus', 'valor': 200, 'status': 'pendente'}
adicionar_pedido(pedidos, novo_pedido)
salvar('pedidos.json', pedidos)
pedidos = carregar('pedidos.json')

for itens in pedidos:
    print(itens['id'], itens['cliente'], itens['valor'], itens['status'])


try :
    pedido_invalido = {'id': 5, 'cliente': 'Pablo', 'valor': 0, 'status': 'pendente'}
    adicionar_pedido(pedidos, pedido_invalido)
except ValueError as e:
    print(e)







