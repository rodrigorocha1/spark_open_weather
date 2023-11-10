from typing import Dict
from hooks.openweaterhook import OpenWeatherHook
from operators.openweatheroperator import OpenWeatherOperator
from src.dados.iinfra_dados import IinfraDados


class TempoAgoraOperator(OpenWeatherOperator):

    ttemplate_fields = [
        'municipio',
        'caminho_save_arquivos',
        'extracao'
    ]

    def __init__(
            self,
            municipio: str,
            caminho_save_arquivos: IinfraDados,
            extracao: OpenWeatherHook, **kwargs
    ):
        super().__init__(municipio, caminho_save_arquivos, extracao, **kwargs)

    def execute(self, context):
        for json_reponse in self._extracao.run():
            self.gravar_dados(json_reponse)


if __name__ == '__main__':

    from airflow.models import DAG, TaskInstance
    from hooks.tempo_agora_hook import TempoAgoraHook
    from datetime import datetime
    from src.dados.infra_json import InfraJson

    municipio = 'Ribeirão Preto'

    with DAG(dag_id='tempo_agora_teste', start_date=datetime.now()) as dag:
        to = TempoAgoraOperator(
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
