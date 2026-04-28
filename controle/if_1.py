nota = float(input('Digite a nota: '))
comportado = True if input('Comportado? (s/n)') == 's' else False
if(nota >= 9 and comportado):
    print('parabéns!')
    print('quadro de honra')
elif(nota >= 7):
    print('aprovado')
elif(nota >= 5.5):
    print('recuperação')
elif(nota >= 3.5):
    print('recuperacao + trabalho')
else:
    print('reprovado') 

print(nota)