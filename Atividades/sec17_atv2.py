from dataclasses import dataclass
#1 / #2

"""
class Equipamento:

    @property
    def nome(self):
        return self.__nome

    @property
    def tipo(self):
        return self.__tipo
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @tipo.setter 
    def tipo(self, tipo):
        self.__tipo = tipo

    def __init__(self, nome, tipo):
        self.__nome = nome
        self.__tipo = tipo

class Computador(Equipamento):
    
    @property
    def computador(self):
        return self._computador
    
    @property
    def placa(self):
        return self._placa_de_video

    @computador.setter
    def computador(self, computador):
        self._computador = computador

    @placa.setter
    def placa(self, placa):
        self._placa_de_video = placa

    def __init__(self, nome, tipo, computador, placa_de_video):
        super().__init__(nome, tipo)
        self._computador = computador
        self._placa_de_video = placa_de_video

computador1 = Computador('TV', 'Eletronico', 'I3', 'GTX1650')
print(computador1.placa)
computador1.placa = '2060TI'
print(computador1.placa)
"""
