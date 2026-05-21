# conta de 0 ate 9
for i in range(10):
    print(i)

# conta de 1 ate 10
for i in range(1, 11):
    print(i)

# conta de 1 ate 99, pulando de 7 em 7
for i in range(1, 100, 7):
    print(i)

# conta de 20 ate 1, diminuindo de 3 em 3
for i in range(20, 0, -3):
    print(i)

# lista com alguns numeros
nums = [2,4,6,8]

# percorre cada numero da lista
for n in nums:
    print(n, end=' ')

# texto tbm pode ser percorrido letra por letra
texto = 'python eh muito massa'
for letra in texto:
    print(letra)

# percorre um conjunto de numeros
for n in {1,2,3,4,5}:
    print(n, end=' ')

# dicionario com infos de um produto
produtos = {
    'nome': 'Caneta',
    'preco': 2.5,
    'desconto': 0.5
}

# percorre as chaves do dict e pega o valor de cada uma
for atrib in produtos:
    print(atrib, produtos[atrib])

# percorre chave e valor ao msm tempo
for atrib, valor in produtos.items():
    print(atrib, '->', valor)

# percorre so os valores
for valor in produtos.values():
    print(valor, end=' ')

# percorre so as chaves
for atrib in produtos.keys():
    print(atrib, end=' ')
