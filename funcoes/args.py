# *args recebe varios valores posicionais em forma de tupla
def soma(*args):
    resultado = 0  # comeca a soma em zero

    # percorre todos os numeros recebidos
    for numero in args:
        resultado += numero  # soma cada numero no resultado

    return resultado

# **kwargs recebe valores nomeados em forma de dicionario
def resultado_final(**kwargs):
    # verifica a nota e define se passou ou nao
    status = 'aprovado(a)' if kwargs['nota'] >= 7 else 'reprovado(a)'

    # monta uma mensagem usando nome, status e nota
    return f'{kwargs["nome"]} está {status} com nota {kwargs["nota"]}'
