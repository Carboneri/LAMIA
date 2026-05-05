class produto:
    def __init__(self, nome, preco=1.99, desc=0):
        self.nome = nome
        self.__preco = preco  # atributo privado (protecao)
        self.desc = desc      # desconto 

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
        return self.__preco * (1 - self.desc)


# criando objs
p1 = produto("Caneta", 10, 0.1)
p2 = produto("caderno", 14, 0.5)

# alterando preco com setter
p1.preco = 70
p2.preco = 17.90
#python super seguro como podemos ver
p3 = p1
p3._produto__preco = 100

# exibindo dados
print(p1.nome, p1.preco, p1.desc, p1.preco_final)
print(p2.nome, p2.preco, p2.desc, p2.preco_final)


