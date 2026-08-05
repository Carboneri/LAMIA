import pytest

# testes do dag estoque_pratica, mesma ideia do test_dag_validation.py e do
# test_tst_dag_definition.py da aula. usa o fixture "dagbag" que ja ta
# definido no conftest.py dessa pasta (nao precisei criar de novo)


def test_estoque_pratica_importa_sem_erro(dagbag):
    # confere que o arquivo nao deu erro nenhum ao ser importado pelo airflow
    # (mesma logica do test_import_dags, so que filtrando so pro meu arquivo)
    caminho = '/usr/local/airflow/dags/praticas/estoque_pratica.py'
    erro = dagbag.import_errors.get(caminho)
    assert erro is None, f"deu erro ao importar o estoque_pratica: {erro}"


def test_estoque_pratica_tem_default_args_certo(dagbag):
    # confere se retries, retry_delay e email tao preenchidos (boa pratica
    # dessa sessao, que nem o test_default_args_* da aula cobra)
    dag = dagbag.get_dag('estoque_pratica')
    assert dag.default_args.get('retries') is not None
    assert dag.default_args.get('retry_delay') is not None
    assert dag.default_args.get('email') is not None


def test_estoque_pratica_gera_uma_task_por_produto(dagbag):
    # o csv (estoque.csv) tem 5 produtos, entao tem que ter:
    # inicio + zerando_resultado + 5 tasks de produto + somar_total + mostrar_resultado = 9
    dag = dagbag.get_dag('estoque_pratica')
    assert len(dag.tasks) == 9, "esperava 9 tasks (a task dinamica nao bateu com o csv)"


def test_task_inicio_nao_depende_de_ninguem(dagbag):
    # a task "inicio" tem que ser a primeira, sem nada rodando antes dela
    dag = dagbag.get_dag('estoque_pratica')
    task = dag.get_task('inicio')
    assert task.upstream_task_ids == set()
