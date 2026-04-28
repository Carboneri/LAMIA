lockdown = False
grana = 30
status = 'em casa' if lockdown and grana <= 100  else 'uhuuu'

print(status)