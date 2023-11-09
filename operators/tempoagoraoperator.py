from typing import Dict
from hooks.openweaterhook import OpenWeatherHook
from operators.openweatheroperator import OpenWeatherOperator
from src.dados.iinfra_dados import IinfraDados


class TempoAgoraOperator(OpenWeatherOperator):

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
