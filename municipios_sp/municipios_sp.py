import requests
from typing import Tuple, List, Any
from time import sleep
import pickle
import os


def obter_municipio_sp() -> List[Tuple[Any, Any]]:
    with open(os.path.join(os.getcwd(), 'municipios_sp', 'municipios.pkl'), 'rb') as arquivo:
        municipios = pickle.load(arquivo)
    return municipios
