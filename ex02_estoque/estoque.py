

class Produto:
    def __init__(self, nome, preco):
        if not nome:
            raise ValueError("O produto está sem nome")
        if preco <= 0:
            raise ValueError("O produto está com o preço invalido")
        self.nome = nome
        self.preco = preco
    def aplicar_desconto (self, desconto):
        if desconto < 0 or desconto > 50:
            raise ValueError("Desconto invalido")
        desconto = desconto / 100
        aplicar = desconto * self.preco
        valor = self.preco - aplicar
        self.preco = valor
class Estoque:
    def __init__(self):
        self.lista = []
    def adicionar(self, produto):
        for itens in self.lista:
            if produto.nome == itens.nome:
                raise ValueError("Ja existe um produto com esse nome")
        self.lista.append(produto)
    def buscar(self, nome):
        for itens in self.lista:
            if itens.nome == nome:
                return itens
        raise ValueError(f"O nome {nome} não encontrado")
    def valor_total(self):
        valor_total = 0
        for itens in self.lista:
            valor_total += itens.preco
        return valor_total

estoque = Estoque()
estoque.adicionar(Produto("Bota", 300))
estoque.adicionar(Produto("Tenis", 200))
estoque.adicionar(Produto("Chinelo", 100))
try:
    estoque.adicionar(Produto("Chinelo", 100))
except ValueError as e:
    print(e)


print(estoque.valor_total())
item = estoque.buscar("Bota")
print(item.nome, item.preco)
try:
    item = estoque.buscar("Sandalia")
except ValueError as e:
    print(e)
