import requests
from typing import Tuple, List, Any
from time import sleep


def obter_municipio_sp() -> List[Tuple[Any, Any]]:
    url = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados/35/municipios?view=nivelado'
    req = requests.get(url=url)
    req = req.json()
    municipios = [(mun['municipio-id'], mun['municipio-nome']) for mun in req]
    return municipios
