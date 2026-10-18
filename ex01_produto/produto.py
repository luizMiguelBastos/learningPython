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



Bota = Produto("Bota", 100.50)
Bota.aplicar_desconto(10)
print(f"Produto: {Bota.nome}, Valor: {Bota.preco}")
try:
    Bota.aplicar_desconto(80)
except ValueError as e:
    print(e)
print(f"Produto: {Bota.nome}, Valor: {Bota.preco}")
