pessoas = ['gui', 'rebeca']
adjs = ['linda', 'inteligente']

for pessoa in pessoas:
    for adj in adjs:
        print(f'{pessoa} é {adj}')

for i in [1,2,3]:
    pass
for i in range(1, 11):
    if i % 2:
        continue
    print(i)
for i in range(1, 11):
    if i == 5:
        break
    print(i)
print('fim')