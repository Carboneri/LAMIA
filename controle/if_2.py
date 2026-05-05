# aqui a variavel 'a' recebe varios valores diferentes
# cada linha troca o valor anterior de 'a'

a = 'valor'
a = 0
a = -0.00001
a = " "
a = '  '
a = []
a = {}

# o if verifica se a tem algum valor considerado verdadeiro
# string vazia, lista vazia, dict vazio e zero dao False
if a:
    print('existe')
else:
    print('nao existe ou zero ou vazio...')
