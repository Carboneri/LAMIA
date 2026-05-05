# Crie um programa que cadastre alunos e calcule a situacao deles.

alunos = []

while(True):

    print("1 - Procurar aluno")
    print("2 - Mostrar todos os alunos")
    print("3 - Cadastrar aluno")
    print("4 - Situacao do aluno")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        nome = input("Digite o nome do aluno: ")
        for aluno in alunos:
            if aluno['nome'] == nome:
                print(aluno)
                break
        else:
            print("Aluno não encontrado.")
    elif opcao == '2':
        for aluno in alunos:
            print(aluno)
        print(len(alunos), "alunos cadastrados.")
    elif opcao == '3':
        print("Cadastrando aluno...")
        nome = input("Digite o nome do aluno: ")
        nota1 = float(input("Digite a nota 1 do aluno: "))
        ativo = input("O aluno está ativo? (s/n): ") == 's'
        alunos.append({
            'nome': nome,
            'nota1': nota1,
            'ativo': ativo,
            'situacao': 'aprovado' if nota1 >= 7 else 'reprovado' 
        })
    elif opcao == '4':
        nome = input("Digite o nome do aluno: ")
        
        for aluno in alunos:
            if aluno['nome'] == nome:
                print(f"Situação do aluno {aluno['nome']}: {aluno['situacao']}")
                break
        else:
            print("Aluno não encontrado.")
    elif opcao == '5':
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")
