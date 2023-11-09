from typing import Dict
from hooks.openweaterhook import OpenWeatherHook
from operators.openweatheroperator import OpenWeatherOperator
from src.dados.iinfra_dados import IinfraDados
from src.dados.infra_json import InfraJson


class PrevisaoCincoDiasOperator(OpenWeatherOperator):

    template_fields = [
        'camada_data_lake',
        'path_extracao',
        'municipio',
        'metricas',
        'caminho_save_arquivos'
        'extracao'
    ]

    def __init__(
            self, camada_data_lake: str, path_extracao: str,
            municipio: str, metricas: str,
            caminho_save_arquivos: IinfraDados, extracao: OpenWeatherHook, **kwargs
    ):
        super().__init__(camada_data_lake, path_extracao, municipio,
                         metricas, caminho_save_arquivos, extracao, **kwargs)

    def execute(self, context):
        for json_reponse in self._extracao.run():
            self.gravar_dados(json_reponse)


if __name__ == '__main__':

    from airflow.models import DAG
    from datetime import datetime

    municipio = 'Ribeirão Preto'

    with DAG(dag_id='tempo_agora_teste', start_date=datetime.now()) as dag:
        to = PrevisaoCincoDiasOperator(
            camada_data_lake='bronze',
            path_extracao='extracao_dia_2023_11_09',
            caminho_save_arquivos='/home/rodrigo/Documentos/projetos/spark_open_weather/data/bronze'
            extracao=InfraJson(
                extracao=''
            )

        )
