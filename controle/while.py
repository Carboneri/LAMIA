# comeca o total das notas em 0
total=0.0

# conta qtas notas foram digitadas
qtde= 0

# nota comeca em 0 so pra entrar no while
nota= 0

# repete enquanto a nota for diferente de -1
while nota != -1:
    nota = float(input('informe o numero ou -1 para sair: '))

    # se nao for -1, soma a nota e aumenta a quantidade
    if nota != -1:
        qtde += 1
        total += nota

# calcula e mostra a media
print(f'a media da turma eh {total/qtde}')
