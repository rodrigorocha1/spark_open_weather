from typing import Dict
from operators.openweatheroperator import OpenWeatherOperator
from src.dados.iinfra_dados import IinfraDados


class TempoAgoraOperator(OpenWeatherOperator):

    template_fields = [
        'camada_data_lake',
        'path_extracao',
        'municipio',
        'metricas',
        'caminho_save_arquivos'
    ]

    def __init__(self, camada_data_lake: str, path_extracao: str, municipio: str, metricas: str, caminho_save_arquivos: IinfraDados, **kwargs):
        super().__init__(camada_data_lake, path_extracao,
                         municipio, metricas, caminho_save_arquivos, **kwargs)

    def gravar_dados(self, req: Dict):
        self._caminho_save_arquivos.salvar_dados(req=req)

    # def execute(self, context):
    #     for json_reponse in self.
