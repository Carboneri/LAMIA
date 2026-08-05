"""
dag que le um csv de estoque e calcula o valor de cada produto e o total.

"""

from airflow import DAG
from airflow.operators.python_operator import PythonOperator  # roda as funcoes python (zerar arquivo, calcular cada produto, somar total)
from airflow.operators.bash_operator import BashOperator      # so pra mostrar o resultado final no log
from airflow.operators.dummy_operator import DummyOperator    # marca o inicio do pipeline, nao faz nada de verdade

from datetime import datetime, timedelta
import csv  # ler o csv do estoque, separado por ; que nem o forex_currencies.csv da sessao 3


# caminhos do csv de entrada e do arquivo onde vou empilhando os resultados
CSV_PATH = '/usr/local/airflow/dags/praticas/files/estoque.csv'
RESULTADO_PATH = '/usr/local/airflow/dags/praticas/files/resultado_estoque.txt'


# default_args com retries, retry_delay e email = boa pratica que essa sessao
# ensina (e que o test_dag_validation.py da aula cobra em teste)
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'email': ['owner@test.com'],
    'retries': 2,                          # tenta rodar de novo 2x se der erro
    'retry_delay': timedelta(minutes=3)    # espera 3 min entre as tentativas
}


# zera o arquivo de resultado antes de comecar. se nao fizer isso ele fica
# empilhando resultado de execucao antiga em cima da nova toda vez que roda
def zerar_resultado():
    open(RESULTADO_PATH, 'w').close()


# calcula o valor de UM produto só (essa funcao vai virar varias tasks, uma
# por produto, la embaixo). os parametros vem via op_kwargs de cada task
def calcular_produto(produto, quantidade, preco_unitario):
    valor = quantidade * preco_unitario
    print(f'{produto}: {quantidade} un x R${preco_unitario} = R${valor:.2f}')

    # cada task escreve a propria linha no arquivo (modo append, "a")
    with open(RESULTADO_PATH, 'a') as saida:
        saida.write(f'{produto};{valor:.2f}\n')


# le tudo que as tasks de produto escreveram e soma pra saber o valor total do estoque
def somar_total():
    total = 0
    with open(RESULTADO_PATH) as arquivo:
        for linha in arquivo:
            produto, valor = linha.strip().split(';')
            total += float(valor)

    with open(RESULTADO_PATH, 'a') as saida:
        saida.write(f'TOTAL;{total:.2f}\n')

    print(f'valor total do estoque: R${total:.2f}')


# monta o dag: roda 1x por dia, sem catchup
with DAG(dag_id='estoque_pratica', schedule_interval='@daily', default_args=default_args, catchup=False) as dag:

    # 1 - task boba so pra marcar o comeco do pipeline no grafo do airflow
    inicio = DummyOperator(
        task_id='inicio'
    )

    # 2 - limpa o arquivo de resultado antes das tasks de calculo comecarem
    zerando_resultado = PythonOperator(
        task_id='zerando_resultado',
        python_callable=zerar_resultado
    )

    # le o csv AQUI FORA das tasks (na hora que o airflow monta o dag) só pra
    # saber quantos produtos tem e gerar 1 task pra cada um
    with open(CSV_PATH) as arquivo_csv:
        produtos = list(csv.DictReader(arquivo_csv, delimiter=';'))

    # 3 - gera dinamicamente uma PythonOperator pra cada produto do csv
    tasks_produtos = []
    for linha in produtos:
        task_produto = PythonOperator(
            task_id=f"calcular_{linha['produto']}",   # ex: calcular_teclado, calcular_mouse...
            python_callable=calcular_produto,
            op_kwargs={                                 # manda os parametros pra funcao calcular_produto
                'produto': linha['produto'],
                'quantidade': int(linha['quantidade']),
                'preco_unitario': float(linha['preco_unitario'])
            }
        )
        tasks_produtos.append(task_produto)

    # 4 - depois que todas as tasks de produto rodaram, soma tudo
    total = PythonOperator(
        task_id='somar_total',
        python_callable=somar_total
    )

    # 5 - mostra o resultado final (todas as linhas + o total) no log via bash
    mostrar_resultado = BashOperator(
        task_id='mostrar_resultado',
        bash_command=f'cat {RESULTADO_PATH}'
    )

    # dependencia usando uma LISTA de tasks no meio (tasks_produtos), mesma
    # ideia do "task_1 >> task_2 >> tasks >> task_6" que tinha no tst_dag.py.
    # todas as tasks_produtos rodam depois do zerando_resultado e antes do total
    inicio >> zerando_resultado >> tasks_produtos >> total >> mostrar_resultado
""