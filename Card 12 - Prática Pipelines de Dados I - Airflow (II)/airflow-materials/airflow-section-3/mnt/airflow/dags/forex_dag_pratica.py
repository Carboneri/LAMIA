"""
EXERCICIO PRATICO - forex_dag_pratica

montei uma dag que confere, dentre uma lista de moedas estrangeiras
(USD, EUR, GBP, JPY, ARS), qual delas ta valendo MAIS em reais (BRL) hoje e
qual ta valendo MENOS, e no final avisa esse resultado no slack.

reaproveitando as mesmas ferramentas e as mesmas connections que ja
configurei no airflow durante a sessao 3:
  - HttpSensor pra confirmar que a api ta no ar (mesma connection forex_api)
  - FileSensor pra confirmar que o arquivo de moedas existe (mesma connection
    forex_path, só que apontando pra um csv novo que eu criei: moedas_brl.csv)
  - PythonOperator pra fazer a conta
  - BashOperator pra mostrar o resultado
  - SlackAPIPostOperator pra avisar no slack (reusando o token via env var)
"""

from airflow import DAG
from airflow.sensors.http_sensor import HttpSensor            # sensor que fica dando poke numa url ate a resposta ficar do jeito que eu quero
from airflow.contrib.sensors.file_sensor import FileSensor     # sensor que confere se um arquivo existe antes de seguir
from airflow.operators.python_operator import PythonOperator   # roda a funcao python que faz a comparacao das moedas
from airflow.operators.bash_operator import BashOperator       # so pra mostrar o resultado no log
from airflow.operators.slack_operator import SlackAPIPostOperator  # manda a msg final no slack
from datetime import datetime, timedelta

import csv       # ler o csv das moedas que eu quero comparar
import requests  # chamar a api de cambio
import os        # pegar o token do slack de uma env var (nao deixo hardcoded no arquivo)

# uso "or" com um valor fake de fallback pq o SlackAPIPostOperator confere se
# tem token la na hora de MONTAR o dag (nao só quando ele roda de verdade). se
# a env var SLACK_TOKEN nao existir o dag inteiro quebra ao carregar, entao
# deixo um valor fake so pra nao travar o parse (pra rodar de verdade precisa
# exportar SLACK_TOKEN com o token real antes de subir o airflow)
SLACK_TOKEN = os.environ.get("SLACK_TOKEN") or "xoxb-configure-SLACK_TOKEN-no-ambiente"

# caminhos dos arquivos (moram na mesma pasta files/ que o forex_currencies.csv
# da aula, que é pra onde a connection "forex_path" ja aponta)
CSV_PATH = '/usr/local/airflow/dags/files/moedas_brl.csv'
RESULTADO_PATH = '/usr/local/airflow/dags/files/resultado_cotacao.txt'

# argumentos default do dag, mesmo padrao usado em aula
default_args = {
    "owner": "airflow",
    "start_date": datetime(2019, 1, 1),
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "email": "youremail@host.com",
    "retries": 1,
    "retry_delay": timedelta(minutes=5)
}


# le a lista de moedas do csv, chama a api UMA vez só (com base=BRL) e calcula
# quanto vale 1 unidade de cada moeda em reais. no final acha a mais cara e a
# mais barata e escreve um resumo num arquivo txt
def comparar_moedas():
    with open(CSV_PATH) as arquivo:
        leitor = csv.DictReader(arquivo)
        moedas = [linha['moeda'] for linha in leitor]

    # pede a cotacao de tudo em relacao ao BRL numa chamada só (mais eficiente
    # que ficar chamando a api uma vez pra cada moeda, que nem fazia em aula)
    dados = requests.get('https://open.er-api.com/v6/latest/BRL').json()
    rates = dados['rates']  # ex: rates['USD'] = quantos USD da pra comprar com 1 BRL

    valores_em_brl = {}
    for moeda in moedas:
        # rates[moeda] é "quanto dessa moeda vale 1 BRL", entao pra saber
        # quanto vale 1 UNIDADE dessa moeda em reais é so inverter a conta
        valores_em_brl[moeda] = 1 / rates[moeda]

    mais_cara = max(valores_em_brl, key=valores_em_brl.get)
    mais_barata = min(valores_em_brl, key=valores_em_brl.get)

    # salva um resumo em txt pra proxima task (bash) so mostrar
    with open(RESULTADO_PATH, 'w') as saida:
        saida.write('cotacao de hoje (1 unidade de cada moeda em reais):\n')
        for moeda, valor in valores_em_brl.items():
            saida.write(f'  1 {moeda} = R${valor:.2f}\n')
        saida.write(f'\nmoeda mais cara hoje: {mais_cara}\n')
        saida.write(f'moeda mais barata hoje: {mais_barata}\n')


# monta o dag: roda 1x por dia, sem catchup
with DAG(dag_id="forex_dag_pratica", schedule_interval="@daily", default_args=default_args, catchup=False) as dag:

    # 1 - confere se a api de cambio ta respondendo antes de seguir
    is_forex_rates_available = HttpSensor(
        task_id="is_forex_rates_available",
        method="GET",
        http_conn_id="forex_api",   # mesma connection configurada em aula
        endpoint="v6/latest/BRL",
        response_check=lambda response: "rates" in response.text,
        poke_interval=5,
        timeout=20
    )

    # 2 - confere se o csv com a lista de moedas ta no lugar certo
    is_moedas_file_available = FileSensor(
        task_id="is_moedas_file_available",
        fs_conn_id="forex_path",   # mesma connection tipo File da aula
        filepath="moedas_brl.csv",
        poke_interval=5,
        timeout=20
    )

    # 3 - roda a funcao que compara as moedas e gera o resumo
    comparando_moedas = PythonOperator(
        task_id="comparando_moedas",
        python_callable=comparar_moedas
    )

    # 4 - so mostra o resultado no log (cat no arquivo gerado)
    mostrar_resultado = BashOperator(
        task_id="mostrar_resultado",
        bash_command=f'cat {RESULTADO_PATH}'
    )

    # 5 - avisa no slack que a comparacao do dia rodou
    sending_slack_notification = SlackAPIPostOperator(
        task_id="sending_slack",
        token=SLACK_TOKEN,
        username="airflow",
        text="cotacao do dia calculada, confere o log da task mostrar_resultado pra ver qual moeda ta mais cara/barata",
        channel="#airflow-exploite"
    )

    # ordem de execucao das tasks
    is_forex_rates_available >> is_moedas_file_available >> comparando_moedas >> mostrar_resultado >> sending_slack_notification
