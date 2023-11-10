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
