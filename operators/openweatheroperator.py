from abc import ABC, abstractmethod
from typing import Dict
from src.dados.iinfra_dados import IinfraDados
from airflow.models import BaseOperator


class OpenWeatherOperator(BaseOperator, ABC):
    template_fields = [
        'camada_data_lake',
        'path_extracao',
        'municipio',
        'metricas',
        'caminho_save_arquivos'
    ]

    def __init__(self, camada_data_lake: str, path_extracao: str, municipio: str, metricas: str, caminho_save_arquivos: IinfraDados, **kwargs):
        """Classe Base de operator

        Args:
            camada_data_lake (str): camada do datalake
            path_extracao (str): path_extracao ex: extracao_dia)
            municipio (str): nome do munpicipio
            metricas (str): métrica
            caminho_save_arquivos (IinfraDados): local para salvar arquivos
        """

        self._camada_data_lake = camada_data_lake
        self._path_extracao = path_extracao
        self._municipio = municipio
        self._metricas = metricas
        self._caminho_save_arquivos = caminho_save_arquivos
        super().__init__(**kwargs)

    @abstractmethod
    def gravar_dados(self, req: Dict):
        pass

    @abstractmethod
    def execute(self, context):
        pass
