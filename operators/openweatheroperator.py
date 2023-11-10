from abc import ABC, abstractmethod
from typing import Dict
from airflow.models import BaseOperator
from src.dados.iinfra_dados import IinfraDados
from hooks.openweaterhook import OpenWeatherHook


class OpenWeatherOperator(BaseOperator, ABC):

    ttemplate_fields = [
        'municipio',
        'caminho_save_arquivos',
        'extracao'
    ]

    def __init__(
        self,
            municipio: str,
            caminho_save_arquivos: IinfraDados,
            extracao:  OpenWeatherHook,
            **kwargs
    ):
        """Operator Base

        Args:
            municipio (str): municipiop
            caminho_save_arquivos (IinfraDados): caminho para salvar arquivo
            extracao (OpenWeatherHook): tipo de extração
        """

        self._municipio = municipio
        self._caminho_save_arquivos = caminho_save_arquivos
        self._extracao = extracao
        super().__init__(**kwargs)

    def gravar_dados(self, req: Dict):
        self._caminho_save_arquivos.salvar_dados(req=req)

    @abstractmethod
    def execute(self, context):
        pass
