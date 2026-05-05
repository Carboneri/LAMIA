lockdown = False
grana = 30

status = 'em casa' if lockdown and grana <= 100 else 'uhuuu'
# operador ternario (if em 1 linha)
# se condicao for True -> 'em casa'
# senao -> 'uhuuu'

print(status)  
# como lockdown = False -> cai no else -> 'uhuuu'