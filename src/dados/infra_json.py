
import json
from src.dados.infra_dados import InfraDados
import os


class InfraJson(InfraDados):

    def __init__(self, diretorio_datalake: str, path_extracao: str, municipio: str, metricas: str, nome_arquivo: str) -> None:
        """Classe para salvar a requisição

        Args:
            diretorio_datalake (str): prata, bronze, outro
            path_extracao (str): path de extracao ex: extracao_dia
            municipio (str): municipio
            metricas (str): metricas
            nome_arquivo (str): nome do arquivo
        """
        super().__init__(diretorio_datalake, path_extracao, municipio, metricas, nome_arquivo)

    def __verificar_diretorio(self):
        if not os.path.exists(self._diretorio_completo):
            os.makedirs(self._diretorio_completo)

    def salvar_dados(self, **kargs):
        self.__verificar_diretorio()
        caminho_completo = os.path.join(
            self._diretorio_completo, self._nome_arquivo
        )
        with open(caminho_completo, 'a') as arquivo_json:
            json.dump(
                kargs['req'],
                arquivo_json, ensure_ascii=False
            )
            arquivo_json.write('\n')

    def carregar_dados(self):
        pass
