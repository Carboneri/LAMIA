from functools import reduce  # importa reduce para reduzir varios valores em um

# recebe um valor delta e cria uma funcao que soma esse delta na nota
def somar_nota(delta):
    def calc(nota):
        return nota + delta 
    return calc

# funcao comum que soma 1.5 na nota
def mais_um_meio(nota):
    return nota + 1.5

notas = [6.4, 7.2, 5.4, 8.4]  # lista de notas

# usa map p/ somar 1.5 em cada nota
notas_finais1 = list(map(somar_nota(1.5), notas))

# usa map p/ somar 1.6 em cada nota
notas_finais2 = list(map(somar_nota(1.6), notas))

print(notas_finais1)
print(notas_finais2)

# funcao simples p/ somar dois valores
def somar(a, b):
    return a + b

# soma todas as notas usando reduce
total = reduce(somar, notas, 0)
print(total)

# aplica a funcao mais_um_meio em todas as notas
notas = list(map(mais_um_meio, notas))

# outro jeito de alterar a lista seria usando enumerate
# for i, nota in enumerate(notas):
#     notas[i] = nota + 1.5

# percorre pelo indice e soma mais 1.5 em cada nota
for i in range(len(notas)):
    notas[i] = notas[i] + 1.5

print(notas)
