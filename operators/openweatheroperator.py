from abc import ABC, abstractmethod
from typing import Dict
from src.dados.iinfra_dados import IinfraDados
from hooks.openweaterhook import OpenWeatherHook
from airflow.models import BaseOperator


class OpenWeatherOperator(BaseOperator, ABC):
    template_fields = [
        'camada_data_lake',
        'path_extracao',
        'municipio',
        'metricas',
        'caminho_save_arquivos'
        'extracao'
    ]

    def __init__(
        self,
            camada_data_lake: str,
            path_extracao: str,
            municipio: str,
            metricas: str,
            caminho_save_arquivos: IinfraDados,
            extracao:  OpenWeatherHook,
            **kwargs
    ):
        """Operator Base

        Args:
            camada_data_lake (str): camada do datalake
            path_extracao (str): path de extração
            municipio (str): municipiop
            metricas (str): métricas
            caminho_save_arquivos (IinfraDados): caminho para salvar arquivo
            extracao (OpenWeatherHook): tipo de extração
        """

        self._camada_data_lake = camada_data_lake
        self._path_extracao = path_extracao
        self._municipio = municipio
        self._metricas = metricas
        self._caminho_save_arquivos = caminho_save_arquivos
        self._extracao = extracao
        super().__init__(**kwargs)

    def gravar_dados(self, req: Dict):
        self._caminho_save_arquivos.salvar_dados(req=req)

    @abstractmethod
    def execute(self, context):
        pass
