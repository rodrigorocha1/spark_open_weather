
import json
from src.dados.infra_dados import InfraDados
import os


class InfraJson(InfraDados):

    def __init__(self, diretorio_datalake: str, path_extracao: str, metricas: str, nome_arquivo: str) -> None:
        """Classe para salvar a requisição

        Args:
            diretorio_datalake (str): prata, bronze, outro
            path_extracao (str): path de extracao ex: extracao_dia
            metricas (str): metricas
            nome_arquivo (str): nome do arquivo
        """
        super().__init__(
            diretorio_datalake=diretorio_datalake,
            path_extracao=path_extracao,
            metricas=metricas,
            nome_arquivo=nome_arquivo
        )

    def __verificar_diretorio(self):
        if not os.path.exists(self._diretorio_completo):
            os.makedirs(self._diretorio_completo)

    def salvar_dados(self, **kargs):
        self.__verificar_diretorio()
        with open(os.path.join(self._diretorio_completo, self._nome_arquivo), 'a') as arquivo_json:
            json.dump(
                kargs['req'],
                arquivo_json, ensure_ascii=False
            )
            arquivo_json.write('\n')

    def carregar_dados(self):
        pass
