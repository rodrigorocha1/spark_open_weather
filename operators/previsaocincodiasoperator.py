try:
    import os
    import sys
    sys.path.insert(0, os.path.abspath(os.curdir))
except:
    pass
from operators.openweatheroperator import OpenWeatherOperator
from hooks.openweaterhook import OpenWeatherHook
from src.dados.iinfra_dados import IinfraDados


class PrevisaoCincoDiasOperator(OpenWeatherOperator):

    ttemplate_fields = [
        'municipio',
        'caminho_save_arquivos',
        'extracao'
    ]

    def __init__(self, municipio: str, caminho_save_arquivos: IinfraDados, extracao: OpenWeatherHook, **kwargs):
        super().__init__(
            municipio=municipio,
            caminho_save_arquivos=caminho_save_arquivos,
            extracao=extracao,
            **kwargs
        )

    def execute(self, context):
        self.gravar_dados(self._extracao.run())


if __name__ == '__main__':

    from airflow.models import DAG, TaskInstance
    from hooks.previsaocincodias import PrevisaoCincoDiasHook
    from datetime import datetime
    from src.dados.infra_json import InfraJson

    municipios = [(1, 'Ribeirão Preto'), (2, 'Cravinhos')]

    with DAG(dag_id='tempo_agora_teste', start_date=datetime.now()) as dag:
        for municipio in municipios:
            to = PrevisaoCincoDiasOperator(
                task_id=f'id_previsao_{municipio[0]}',
                municipio=municipio[1],
                caminho_save_arquivos=InfraJson(
                    diretorio_datalake='bronze',
                    path_extracao='extracao_dia_2023_11_09',
                    nome_arquivo=f'req_temp_atual_{municipio[0]}.json',
                    metricas='previsao_atual'
                ),
                extracao=PrevisaoCincoDiasHook(
                    municipio=municipio[1],


                )
            )
            ti = TaskInstance(task=to)
            to.execute(ti.task_id)
