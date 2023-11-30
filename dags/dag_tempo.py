try:
    import sys
    import os
    sys.path.insert(0, os.path.abspath(os.curdir))
except ModuleNotFoundError:
    pass
from municipios_sp.municipios_sp import obter_municipio_sp
from airflow.models import DAG
from airflow.utils.task_group import TaskGroup
from airflow.operators.empty import EmptyOperator
from operators.tempoagoraoperator import TempoAgoraOperator
from hooks.tempo_agora_hook import TempoAgoraHook
from hooks.previsaocincodias import PrevisaoCincoDiasHook
from operators.previsaocincodiasoperator import PrevisaoCincoDiasOperator
from src.dados.infra_json import InfraJson
import pendulum


data_atual = pendulum.now('America/Sao_Paulo').to_iso8601_string()
data_atual = pendulum.parse(data_atual)
data_atual = data_atual.strftime('%Y-%m-%d')


with DAG(
    dag_id='dag_extracao_tempo',
    schedule_interval=None,
    catchup=False,
    start_date=pendulum.datetime(2023, 11, 29, tz='America/Sao_Paulo')
) as dag:

    task_inicio = EmptyOperator(
        task_id='task_inicio_dag',
        dag=dag
    )

    with TaskGroup('task_tempo_municipios_sp', dag=dag, ) as tg_mun:
        lista_task_tempo = []
        for municipio in obter_municipio_sp():
            extraca_api_tempo = TempoAgoraOperator(
                task_id=f'municipio_{municipio[0]}',
                municipio=municipio[1],
                caminho_save_arquivos=InfraJson(
                    diretorio_datalake='bronze',
                    path_extracao=f'extracao_dia_{data_atual}',
                    municipio=municipio[1],
                    nome_arquivo='req_temp_atual.json',
                    metricas='previsao_atual'
                ),
                extracao=TempoAgoraHook(
                    municipio=municipio[1],
                )
            )
            lista_task_tempo.append(extraca_api_tempo)

    # with TaskGroup('task_previsao_cinco_dias', dag=dag) as tg_mun:
    #     lista_task_previsao = []
    #     municipios = [(1, 'Ribeirão Preto'), (2, 'Cravinhos')]
    #     for municipio in obter_municipio_sp():
    #         extracao_previsao = PrevisaoCincoDiasOperator(
    #             task_id=f'id_previsao_{municipio[0]}',
    #             municipio=municipio[1],
    #             caminho_save_arquivos=InfraJson(
    #                 diretorio_datalake='bronze',
    #                 path_extracao=f'extracao_dia_{data_atual}',
    #                 municipio=municipio[1],
    #                 nome_arquivo='req_temp_atual.json',
    #                 metricas='previsao_atual'
    #             ),
    #             extracao=PrevisaoCincoDiasHook(
    #                 municipio=municipio[1],

    #             )
    #         )
    #         lista_task_previsao.append(extracao_previsao)

    task_fim = EmptyOperator(
        task_id='task_fim_dag',
        dag=dag,
        trigger_rule='all_done'
    )

    task_inicio >> tg_mun >> task_fim
