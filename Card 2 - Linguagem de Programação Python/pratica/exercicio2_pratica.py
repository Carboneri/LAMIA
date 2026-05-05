# Crie um sistema de produtos e desconto de uma loja usando classe.

class Produto:
    def __init__(self, nome, preco, desconto):
        self.nome = nome
        self.__preco = preco
        self.desconto = desconto

    @property
    def preco(self):
        # getter -> retorna preco formatado (string)
        return f'{self.__preco:.2f}'
    
    @preco.setter
    def preco(self, novo_preco):
        # setter -> controla alteracao do preco
        if novo_preco < 0:
            print('preco n pode ser negativo')  # validacao
        else:
            self.__preco = novo_preco

    @property
    def preco_final(self):
        # calcula preco com desconto
        return self.__preco * (1 - self.desconto)
    

produtos = [Produto("Mouse", 100.0, 0.1), Produto("Teclado", 200.0, 0.2)]

for produto in produtos:
    print(f"Nome: {produto.nome}, Preço: {produto.preco}, Desconto: {produto.desconto}, Preço Final: {produto.preco_final:.2f}")
    valor = 'Barato' if produto.preco_final < 150 else 'Caro'
    print(f"Valor: {valor}")