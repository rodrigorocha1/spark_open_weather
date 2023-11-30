try:
    import sys
    import os
    sys.path.insert(0, os.path.abspath(os.curdir))
except ModuleNotFoundError:
    pass
from typing import Dict
import requests
from airflow.providers.http.hooks.http import HttpHook
from airflow.models import Variable
from abc import ABC, abstractmethod


class OpenWeatherHook(HttpHook, ABC):
    def __init__(self, municipio: str, conn_id: str = None) -> None:
        """Class para 

        Args:
            municipio (str): _description_
            salvar_dados (IinfraDados): _description_
            conn_id (str, optional): _description_. Defaults to None.
        """
        self._municipio = municipio
        self._chave = Variable.get('CHAVE_API_OPENWEATER')
        self._conn_id = conn_id
        super().__init__(http_conn_id=self._conn_id)

    @abstractmethod
    def _criar_url(self):
        pass

    def conectar_api(self, url: str,  params: Dict, session) -> requests.models.Response | bool:
        """Método para conectar na API

        Args:
            url (str): url da API
            params (Dict): parametros requeridos        

        Returns:
            requests.models.Response | bool: respsosta da API ou false
        """
        try:
            response = requests.Request('GET', url=url, params=params)
            prep = session.prepare_request(response)
            return self.run_and_check(session, prep, {})

        except:
            return False

    @abstractmethod
    def run(self):
        pass
