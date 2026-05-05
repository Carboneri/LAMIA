a = 3 
b = 4.4

print(a+b)  
# soma int + float -> resultado float

texto = "sua idade é: "
idade = 18

print(texto + str(idade))  
# concatena convertendo pra string

print(f"{texto} {idade}")  
# f-string (forma mais moderna)

saudacao = "bom dia"
print(saudacao * 3)  
# repete string 3x

PI = 3.14

raio = float(input("informe o raio da circunferência: "))  
# input sempre vem como texto -> converte pra float

area = PI * raio ** 2  
# formula area circulo

print(f"A área da circunferência é: {area}")