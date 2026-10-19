estoque = {
    "Botas": {"Chelsea": 112},
    "Tenis": {"Air Force": 193},
    "Chinelo": {"Havaianas": 120}
}
def adicionar_estoque(estoque, categoria, modelo, qtd):
    if qtd <= 0:
        raise ValueError("Quantidade invalida")
    if categoria not in estoque:
        estoque[categoria] = {}
    if modelo in estoque[categoria]:
        estoque[categoria][modelo] += qtd
    else:
        estoque[categoria][modelo] = qtd

def remover_estoque(estoque, categoria, modelo, qtd):
    if qtd <= 0:
        raise ValueError("Quantidade invalida")
    if categoria not in estoque:
        raise ValueError("Categoria inexistente")
    if modelo not in estoque[categoria]:
        raise ValueError("Modelo inexistente")
    if qtd > estoque[categoria][modelo]:
        raise ValueError("Quantidade invalida")
    estoque[categoria][modelo] -= qtd

adicionar_estoque(estoque, "Crocs", "Foam Runner", 90)
remover_estoque(estoque, "Crocs", "Foam Runner", 30)

try:
    adicionar_estoque(estoque, "Crocs", "Foam Runner", 0)
except ValueError as e:
    print(e)


try:
    remover_estoque(estoque, "Crocs", "Foam Runner", 100)
except ValueError as e:
    print(e)

try:
    remover_estoque(estoque, "Crocs", "Havaiana", 100)
except ValueError as e:
    print(e)


for categoria, modelos in estoque.items():
    for modelo, qtd in modelos.items():
        print(f"Categoria = {categoria} | Modelos = {modelo} | Quantidades = {qtd}")





