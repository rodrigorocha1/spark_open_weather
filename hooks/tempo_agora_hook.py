import os
from hooks.openweaterhook import OpenWeatherHook


class TempoAgoraHook(OpenWeatherHook):

    def __init__(self, municipio: str, conn_id: str = None) -> None:
        super().__init__(municipio, conn_id)

    def _criar_url(self):
        return 'https://api.openweathermap.org/data/2.5/weather'

    def run(self):
        session = self.get_conn()
        url = self._criar_url()
        params = {
            'appid': self._chave,  # self._chave,
            'units': 'metric',
            'lang': 'pt_br',
            'q': self._municipio
        }

        response = self.conectar_api(url=url, params=params, session=session)

        return response.json()
