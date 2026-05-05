from functools import reduce  # importa reduce p/ juntar varios valores

# lista de alunos com nome e nota
alunos = [
    {'nome': 'gui', 'nota': 7.2},   
    {'nome': 'brano', 'nota': 8.1},
    {'nome': 'claudia', 'nota': 8.7},   
    {'nome': 'Pedro', 'nota': 6.4},
    {'nome': 'rafael', 'nota': 6.7},
]

# lambda que verifica se o aluno foi aprovado
aluno_aprovado = lambda aluno: aluno['nota'] >= 7

# filtra a lista, mantendo so os alunos aprovados
alunos_aprovados = filter(aluno_aprovado, alunos)

# lambda que pega so a nota do aluno
# aluno_honra = lambda aluno: aluno['nota'] >= 9
obter_nota = lambda aluno: aluno['nota']

# lambda simples p/ somar dois valores
somar = lambda a, b: a + b

# filtra dnv os alunos aprovados
alunos_aprovados = filter(aluno_aprovado, alunos)

# transforma os alunos aprovados em uma lista/iterador so com as notas
notas_alunos_aprovados = map(obter_nota, alunos_aprovados)

# soma todas as notas dos aprovados
total = reduce(somar, notas_alunos_aprovados, 0)

# exemplos de testes que foram deixados comentados
# print(obter_nota(alunos[2]))
# print(alunos)
# print(list(alunos_aprovados))
# print(list(notas_alunos_aprovados))
# print(total)

# mostra a media dos aprovados
# obs: em python 3, filter nao tem len direto; precisaria converter p/ lista antes
print(total / len(alunos_aprovados))
