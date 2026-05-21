# funcao simples que soma dois valores
def soma(a, b):
    return a + b

# funcao simples que subtrai dois valores
def sub(a, b):
    return a - b

somar = soma  # guarda a funcao soma em outra variavel
print(somar(3, 4))  # chama a funcao pela variavel

# recebe uma funcao e dois numeros, dps executa essa funcao
def operacao_aritmetica(fn, op1, op2):
    return fn(op1, op2)

# passa a funcao soma como parametro
resultado = operacao_aritmetica(soma, 13, 48)
print(resultado)

# passa a funcao sub como parametro
resultado = operacao_aritmetica(sub, 13, 48)
print(resultado)

# cria uma soma parcial, deixando o valor de 'a' ja guardado
def soma_parcial(a):
    # aqui seria um processamento demorado antes de criar a funcao final
    # processamento pesado 1 - 10s
    # processamento pesado 2 - 10s
    # processamento pesado 3 - 40s

    # essa funcao interna usa o 'a' que ficou salvo na funcao de fora
    def soma_b(b):
        return a + b
    return soma_b  # retorna a funcao pronta p/ usar dps

# exemplos de chamadas que poderiam repetir o mesmo processamento pesado
# r1 = soma_total(1, 2) => 1m10s
# r2 = soma_total(1, 3) => 1m10s
# r3 = soma_total(1, 4) => 1m10s

soma_1 = soma_parcial(1)  # cria uma funcao que sempre soma com 1
r1 = soma_1(2)  # 1 + 2
r2 = soma_1(3)  # 1 + 3
r3 = soma_1(4)  # 1 + 4

# tbm da pra chamar tudo direto em uma linha
resultado_final = soma_parcial(10)(12)
print(resultado_final, r1, r2, r3)
