try:
    import os
    import sys
    sys.path.insert(0, os.path.abspath(os.curdir))
except:
    pass
from typing import Dict
from hooks.tempo_agora_hook import TempoAgoraHook
from operators.openweatheroperator import OpenWeatherOperator
from hooks.openweaterhook import OpenWeatherHook
from src.dados.iinfra_dados import IinfraDados


class PrevisaoCincoDiasOperator(OpenWeatherOperator):

    template_fields = [
        'municipio',
        'caminho_save_arquivos',
        'extracao'
    ]

    def __init__(self, municipio: str, caminho_save_arquivos: IinfraDados, extracao: OpenWeatherHook, **kwargs):
        super().__init__(
            municipio=municipio,
            caminho_save_arquivos=caminho_save_arquivos,
            extracao=extracao,
            **kwargs
        )

    def execute(self, context):
        for json_reponse in self._extracao.run():
            self.gravar_dados(json_reponse)


if __name__ == '__main__':

    from airflow.models import DAG, TaskInstance
    from datetime import datetime
    from src.dados.infra_json import InfraJson

    municipio = 'Ribeirão Preto'

    with DAG(dag_id='tempo_agora_teste', start_date=datetime.now()) as dag:
        to = PrevisaoCincoDiasOperator(
            municipio=municipio,
            caminho_save_arquivos=InfraJson(
                diretorio_datalake='bronze',
                path_extracao='extracao_dia_2023_11_09',
                municipio=municipio,
                nome_arquivo='req_temp_atual',
                metricas='previsao_atual'
            ),
            extracao=TempoAgoraHook(
                municipio=municipio,
                conn_id='id_ribeirao_preto'
            )
        )
        ti = TaskInstance(task=to)
        to.execute(ti.task_id)
