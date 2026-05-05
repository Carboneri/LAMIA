from functools import reduce  # importa o reduce, usado p/ juntar varios valores em um so

# lista de alunos, cada um com nome e nota
alunos = [
    {'nome': 'gui', 'nota': 7.2},   
    {'nome': 'brano', 'nota': 8.1},
    {'nome': 'claudia', 'nota': 8.7},   
    {'nome': 'Pedro', 'nota': 6.4},
    {'nome': 'rafael', 'nota': 6.7},
]

somar = lambda a, b: a + b  # funcao curta p/ somar dois valores

# pega so os alunos com nota maior ou igual a 7
alunos_aprovados = [aluno for aluno in alunos if aluno['nota'] >= 7]

# pega apenas as notas dos alunos aprovados
notas_alunos_aprovados = [aluno['nota'] for aluno in alunos_aprovados]

# soma todas as notas dos aprovados, comecando do zero
total = reduce(somar, notas_alunos_aprovados, 0)

# mostra a media dos alunos aprovados
print(total / len(alunos_aprovados))
