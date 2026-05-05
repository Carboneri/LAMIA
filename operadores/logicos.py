b1 = True
b2 = False
b3 = True

print(b1 and b2 and b3)  
# and -> so eh True se TODOS forem True (aqui da False)

print(b1 or b2 or b3)  
# or -> basta um True (aqui da True)

print(b1 != b2)  
# diferente -> True pq True != False

print(not b1)  
# inverte -> vira False

print(not b2)  
# inverte -> vira True

print(b1 and not b2 and b3)  
# True and True and True -> True

x = 3
y = 4

print(b1 and not b2 and b3 and x < y)  
# mistura logico + relacional
# x < y (3 < 4) = True -> tudo vira True