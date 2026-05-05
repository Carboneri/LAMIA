print({1, 2, 3})  
# conjunto (set) -> n permite repetidos

print(type({1, 2, 3}))  # tipo set

conjunto = {1, 2, 3, 3, 3, 3}  
# repetidos sao ignorados automaticamente

#print(conjunto[1])  
# erro -> set n tem indice

print(conjunto)  
# mostra valores unicos

print(len(conjunto))  
# tamanho (quantidade de elementos unicos)