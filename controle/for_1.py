for i in range(10):
    print(i)
for i in range(1, 11):
    print(i)
for i in range(1, 100, 7):
    print(i)
for i in range(20, 0, -3):
    print(i)

nums = [2,4,6,8]

for n in nums:
    print(n, end=' ')

texto = 'python eh muito massa'
for letra in texto:
    print(letra)

for n in {1,2,3,4,5}:
    print(n, end=' ')

produtos = {
    'nome': 'Caneta',
    'preco': 2.5,
    'desconto': 0.5
}
for atrib in produtos:
    print(atrib, produtos[atrib])
for atrib, valor in produtos.items():
    print(atrib, '->', valor)
for valor in produtos.values():
    print(valor, end=' ')
for atrib in produtos.keys():
    print(atrib, end=' ')