# pede a nota e transforma em numero decimal
nota = float(input('Digite a nota: '))

# pergunta se o aluno foi comportado
# se digitar 's', comportado vira True, senao vira False
comportado = True if input('Comportado? (s/n)') == 's' else False

# se a nota for maior ou igual a 9 E o aluno for comportado
if(nota >= 9 and comportado):
    print('parabens!')
    print('quadro de honra')

# se nao entrou no if de cima, mas a nota for pelo menos 7
elif(nota >= 7):
    print('aprovado')

# se a nota for pelo menos 5.5, vai pra recuperacao
elif(nota >= 5.5):
    print('recuperacao')

# se a nota for pelo menos 3.5, vai pra rec + trabalho
elif(nota >= 3.5):
    print('recuperacao + trabalho')

# se nao caiu em nenhuma condicao, esta reprovado
else:
    print('reprovado') 

# mostra a nota no final
print(nota)
