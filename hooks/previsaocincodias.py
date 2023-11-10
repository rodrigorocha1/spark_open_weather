from hooks.openweaterhook import OpenWeatherHook
import os


class PrevisaoCincoDiasHook(OpenWeatherHook):

    def __init__(self, municipio: str, conn_id: str = None) -> None:
        super().__init__(municipio, conn_id)

    def _criar_url(self):
        return 'https://api.openweathermap.org/data/2.5/forecast'

    def run(self):
        session = self.get_conn()
        url = self._criar_url()
        params = {
            'q': self._municipio,
            'appid': os.environ['key'],
            'units': 'metric',
            'lang': 'pt_br'
        }
        response = self.conectar_api(url=url, session=session, params=params)
        return response
