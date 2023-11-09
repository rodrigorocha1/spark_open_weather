from abc import ABC, abstractmethod


class IinfraDados(ABC):

    @abstractmethod
    def salvar_dados(self, **kargs):
        pass

    @abstractmethod
    def carregar_dados(self):
        pass
