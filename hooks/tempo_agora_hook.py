from hooks.openweaterhook import OpenWeatherHook
from src.dados.iinfra_dados import IinfraDados


class TempoAgoraHook(OpenWeatherHook):

    def __init__(self, municipio: str, carregar_dados: IinfraDados, conn_id: str = None) -> None:
        super().__init__(municipio, carregar_dados, conn_id)

    def _criar_url(self):
        return 'https://api.openweathermap.org/data/2.5/weather'

    def run(self):
        session = self.get_conn()
        url = self._criar_url()
        params = {
            'appid': '',
            'units': 'metric',
            'lang': 'pt_br',
            'q': self._municipio
        }

        response = self.conectar_api(url=url, params=params, session=session)
        return response