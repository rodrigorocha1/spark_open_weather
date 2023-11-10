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
        self.gravar_dados(self._extracao.run())
