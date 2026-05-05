# listas usadas nos exemplos
pessoas = ['gui', 'rebeca']
adjs = ['linda', 'inteligente']

# for dentro de for: junta cada pessoa com cada adjetivo
for pessoa in pessoas:
    for adj in adjs:
        print(f'{pessoa} eh {adj}')

# pass nao faz nada, serve so pra deixar o bloco vazio sem erro
for i in [1,2,3]:
    pass

# mostra so os pares de 1 a 10
for i in range(1, 11):
    # se for impar, pula pro prox numero
    if i % 2:
        continue
    print(i)

# para o loop quando chegar no 5
for i in range(1, 11):
    if i == 5:
        break
    print(i)

print('fim')
