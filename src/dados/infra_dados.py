from src.dados.iinfra_dados import IinfraDados
import os


class InfraDados(IinfraDados):

    def __init__(
            self,
        diretorio_datalake: str,
        path_extracao: str,
        municipio: str,
        metricas: str,
        nome_arquivo: str
    ) -> None:
        """Classe para guardar dados

        Args:
            diretorio_datalake (str): diretório do datalake (bronze, prata, ouro)
            path_extracao (str): path_extração ex: extracao_dia
            municipio (str): municipio ex: Ribeirão Preto
            metricas (str): métrica de análise
            nome_arquivo (str): nome_arquivo
        """
        self._diretorio_datalake = diretorio_datalake
        self._path_extracao = path_extracao
        self._municipio = municipio
        self._metricas = metricas
        self._nome_arquivo = nome_arquivo
        self._diretorio_completo = os.path.join(
            diretorio_datalake, path_extracao, municipio, metricas, nome_arquivo)
