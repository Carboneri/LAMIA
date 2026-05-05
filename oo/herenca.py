class carro:
    def __init__(self):
        self.__velocidade = 0  # atributo privado (so a classe mexe direto)

    @property
    def velocidade(self):
        return self.__velocidade  # getter pra acessar sem mexer direto

    def acelerar(self):
        self.__velocidade += 5  # aumenta velocidade de 5 em 5
        return self.__velocidade

    def frear(self):
        self.__velocidade -= 5  # diminui velocidade
        return self.__velocidade


class Uno(carro):
    pass  # herda tudo de carro, sem alterar nada


class Ferrari(carro):
    def acelerar(self):
        super().acelerar()         # chama acelerar da classe pai
        return super().acelerar()  # chama dnv -> acelera 2x mais rapido


# criando objs
c1 = carro()
c2 = Uno()
c3 = Ferrari()

# testando comportamento da ferrari (polimorfismo na pratica)
print(c3.acelerar())  # vai somar 10 (5 + 5)
print(c3.acelerar())
print(c3.acelerar())
print(c3.frear())
print(c3.velocidade)  # acessa via property