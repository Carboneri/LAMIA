# Crie um mini sistema de personagem usando heranca

from random import randint

# classe principal do jogo
# aqui eu coloco tudo que todo personagem vai ter em comum
class Personagem:
    def __init__(self, nome, vida, dano_min, dano_max, sanidade):
        # esse metodo roda quando eu crio um personagem
        # ele serve pra guardar as informacoes iniciais do personagem
        self.nome = nome
        self.__vida = vida
        self.vida_max = vida  # deixei a vida privada pra nao alterar direto fora da classe
        # dano minimo e maximo, pq o dano vai ser sorteado a cada ataque
        self.dano_min = dano_min 
        self.dano_max = dano_max 
        self.sanidade = sanidade  # usado pra resistir intimidacao

    # esse property serve pra eu conseguir ver a vida
    # mas sem mexer diretamente no atributo privado __vida
    @property 
    def vida(self):
        return self.__vida  

    def receber_cura(self, cura):
        self.__vida += cura  # soma a cura na vida

        if self.__vida > self.vida_max:
            self.__vida = self.vida_max  # n deixa passar da vida maxima

        print(f"{self.nome} recuperou {cura} de vida.")
        print(f"Vida atual: {self.__vida}/{self.vida_max}")


    def atacar(self):
    # metodo padrao de ataque 
        dano = randint(self.dano_min, self.dano_max)  # sorteia dano toda vez q ataca
        print(f"{self.nome} ataca e tira {dano} de vida!")
        return dano

    def receber_dano(self, dano):
        self.__vida -= dano  # tira vida

        if self.__vida <= 0:
            self.__vida = 0  # n deixa vida negativa
            print(f"{self.nome} foi derrotado!")
        else:
            print(f"{self.nome} recebeu {dano} de dano.")
            print(f"Vida restante: {self.__vida}/{self.vida_max}")

# classe Guerreiro
# ele herda de Personagem, entao reaproveita vida, ataque, dano e tudo mais
class Guerreiro(Personagem):
    def __init__(self, nome):
        # guerreiro tem bastante vida, dano bom e armadura
        super().__init__(nome, vida=120, dano_min=20, dano_max=40, sanidade=60)
        self.armadura = 10

    def receber_dano(self, dano):
        # a armadura diminui o dano recebido
        dano_reduzido = max(dano - self.armadura, 0)

        print(f"A armadura reduziu o dano de {dano} para {dano_reduzido}.")
        super().receber_dano(dano_reduzido)

# classe Mago
# tambem herda de Personagem, mas tem um ataque diferente
class Mago(Personagem):
    def __init__(self, nome):
        # mago tem pouca vida, mas dano alto
        super().__init__(nome, vida=80, dano_min=15, dano_max=60, sanidade=75)
        self.mana = 40

    def atacar(self):
        if self.mana >= 10:
            self.mana -= 10  # cada magia gasta mana

            dano = randint(self.dano_min, self.dano_max)  # sorteia o dano a cada ataque
            print(f"{self.nome} lanca uma bola de fogo e tira {dano} de vida!")
            print(f"Mana restante: {self.mana}")
            return dano

        else:
            print(f"{self.nome} esta sem mana e nao consegue usar magia!")
            return 0

#fadinha broken
# a fadinha bate pouco, mas consegue se curar
class Fadinha(Personagem):
    def __init__(self, nome):
        
        super().__init__(nome, vida=90, dano_min=10, dano_max=15, sanidade=90)
        self.cura_min = 15
        self.cura_max = 40

    def curar(self):
        cura = randint(self.cura_min, self.cura_max)  # sorteia cura toda vez q usa
        self.receber_cura(cura)


class Boss(Personagem):
    def __init__(self, nome="Oryx"):
        # boss tem bastante vida e dano medio
        super().__init__(nome, vida=150, dano_min=12, dano_max=30, sanidade=100)
        self.intimidacao_min = 1
        self.intimidacao_max = 100

    def tentar_intimidar(self, alvo):
        poder_intimidacao = randint(self.intimidacao_min, self.intimidacao_max)
        # sorteia intimidacao toda vez q o jogador tenta atacar

        print(f"\n\n{self.nome} tentou intimidar com poder {poder_intimidacao}.")
        print(f"Sanidade de {alvo.nome}: {alvo.sanidade}")

        if poder_intimidacao > alvo.sanidade:
            print(f"{alvo.nome} ficou intimidado e nao conseguiu atacar!")
            return True
        else:
            print(f"{alvo.nome} resistiu a intimidacao!")
            return False


# cria o personagem do jogador
while True:
    print("Crie seu personagem:")
    nome = input("Nome: ")

    print("\nEscolha a classe:")
    print("1. Guerreiro")
    print("2. Mago")
    print("3. Fadinha")

    try:
        escolha = int(input("Opcao: "))
    except ValueError:
        print("Digite apenas numeros.")
        continue

    if escolha == 1:
        personagem = Guerreiro(nome)

    elif escolha == 2:
        personagem = Mago(nome)

    elif escolha == 3:
        personagem = Fadinha(nome)

    else:
        print("Opcao invalida!")
        continue

    break


# cria o boss
boss = Boss()
print("\n-------------")
print("\nA luta comecou!")
print(f"{personagem.nome} VS {boss.nome}")


# loop principal da luta
while personagem.vida > 0 and boss.vida > 0:
    print("\n--- Seu turno ---")
    print(f"Sua vida: {personagem.vida}/{personagem.vida_max}")
    print(f"Vida do boss: {boss.vida}/{boss.vida_max}")

    print("\n1. Atacar")

    if isinstance(personagem, Fadinha):
        print("2. Curar")

    try:
        acao = int(input("Escolha sua acao: "))
    except ValueError:
        print("Acao invalida, perdeu o turno.")
        acao = 0

    if acao == 1:
        # toda vez q o jogador tenta atacar, o boss tenta intimidar antes
        intimidou = boss.tentar_intimidar(personagem)

        if not intimidou:
            dano = personagem.atacar()

            if dano > 0:
                boss.receber_dano(dano)

    elif acao == 2 and isinstance(personagem, Fadinha):
        personagem.curar()

    else:
        print("Acao invalida, perdeu o turno.")

    # se o boss morreu no turno do jogador, a luta acaba
    if boss.vida <= 0:
        print("\nVoce venceu!")
        break

    print("\n--- Turno do boss ---")

    # boss sempre ataca no turno dele
    dano = boss.atacar()

    if dano > 0:
        personagem.receber_dano(dano)

    # se o jogador morreu, a luta acaba
    if personagem.vida <= 0:
        print("\nVoce perdeu!")
        break