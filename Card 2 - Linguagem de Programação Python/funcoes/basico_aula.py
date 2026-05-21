# funcao com valores padrao, caso nada seja informado
def saudacao(nome='pessoa', idade=20):
    print(f'bom dia {nome}! \nvc nem parece ter {idade} anos')

# faz uma conta usando soma e multiplicacao
def soma_e_mult(a, b, x):
    return a + b * x

# esse bloco so roda qnd o arquivo eh executado diretamente
if __name__ == '__main__':
    saudacao('gui', idade=18)  # chama a funcao passando nome e idade
