# 1
'''
class Pessoa():
    def __init__(self, nome:str, idade:int, altura:float):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura
    
    def get_nome(self):
        return self.__nome
    
    def get_idade(self):
        return self.__idade
    
    def get_altura(self):
        return self.__altura
    
    def set_nome(self, nome):
        self.__nome = nome
    
    def set_idade(self, idade):
        self.__idade = idade
    
    def set_altura(self, altura):
        self.__altura = altura

    def infos(self):
        info = {
            'Nome':self.__nome,
            'Altura':self.__altura,
            'Idade':self.__idade
        }

        return info

pessoa1 = Pessoa('Julio', 18, 1.72)
print(pessoa1.infos())

pessoa1.set_idade(22)
print(pessoa1.infos())
'''
#2
'''
import json

class Agenda():
    def __init__(self):
        try:
            with open('agenda.json') as ff:
                self.agenda = json.load(ff)

        except FileNotFoundError:
            self.agenda = [] 
    
    def update(self):
        if len(self.agenda) <= 10:
            with open('agenda.json', 'w') as ff:
                json.dump(self.agenda, ff, indent=4)
                ff.close()
        else:
            raise ValueError(f'A agenda está no limite de 10 pessoas.')

    def adicionar_pessoa(self, nome, idade, altura):
        pessoa = {
            'Nome': nome,
            'Idade': idade,
            'Altura': altura
        }

        for pessoa_agenda in self.agenda:
            if pessoa_agenda['Nome'] == pessoa['Nome']:
                raise ValueError(f'A pessoa {nome}, já está na agenda.')
        
        self.agenda.append(pessoa)
        self.update()
    
    def remover_pessoa(self, nome):
        if any(map(lambda pessoa: pessoa['Nome'] == nome, self.agenda)):
            for pessoa in self.agenda:
                if pessoa['Nome'] == nome:
                    self.agenda.remove(pessoa)
                    self.update()
        else:
            raise ValueError(f'A pessoa {nome} não está na agenda')
    
    def buscar_pessoa(self, nome: str) -> int:
        for index, pessoa in enumerate(self.agenda):
            if pessoa['Nome'] == nome:
                ind = index
        
        return ind

    def imprime_pessoa(self, nome: str):
        pessoa = next(filter(lambda pessoa: pessoa['Nome'] == nome , self.agenda), None)

        if not pessoa:
            raise KeyError(f'Pessoa {nome} não foi encontrada na agenda')

        return pessoa

agenda1 = Agenda()
print(agenda1.imprime_pessoa('Luiz'))
#print(agenda1.buscar_pessoa('Guilherme'))
#agenda1.adicionar_pessoa('Luiz', 22, 1.72)
#agenda1.remover_pessoa('Guilherme')
'''
#3
"""
from typing import Optional

class Elevador():
    andar_atual = 0
    pessoas_atuais = 0

    def __init__(self, total_andares, capacidade_elevador):
        self.capacidade = capacidade_elevador
        self.total_andares = total_andares

    def entra_pessoa(self):
        if Elevador.pessoas_atuais < self.capacidade:
            Elevador.pessoas_atuais += 1
        else:
            raise ValueError(f"O elevador está em capacidade maxima {self.capacidade}")
    
    def sai_pessoa(self):
        if Elevador.pessoas_atuais > 0:
            Elevador.pessoas_atuais -= 1
        else:
            raise ValueError(f"O elevador está vazio.")
    
    def subir_elevador(self):
        if Elevador.andar_atual < self.total_andares:
            Elevador.andar_atual += 1
        else:
            raise ValueError(f"O elevador está no ultimo andar.")
        
    def descer_elevador(self):
        if not Elevador.andar_atual == 0:
            Elevador.andar_atual -= 1
        else:
            raise ValueError(f"O elevador está no térreo")
    
    def set_elevador(self, total_andares: Optional[int] = None, capacidade: Optional[int] = None):
        
        if total_andares:
            self.total_andares = total_andares

        if capacidade:
            self.capacidade = capacidade

    def get_elevador(self):
        status_elevador = {
            'Elevador': {
                'total_andares' : self.total_andares,
                'capacidade_max' : self.capacidade,
            },
            'Status_evelador': {
                'Andar_atual': Elevador.andar_atual,
                'Quantidades_pessoas': Elevador.pessoas_atuais
            }
        }
        return status_elevador

elevador = Elevador(5, 7)

elevador.entra_pessoa()
elevador.entra_pessoa()
elevador.entra_pessoa()

print(elevador.get_elevador())

elevador.subir_elevador()
elevador.subir_elevador()
elevador.subir_elevador()

elevador.descer_elevador()
elevador.sai_pessoa()

elevador.set_elevador(total_andares=10)

print(elevador.get_elevador())
"""
# 4
"""
class Tv():
    def __init__(self):
        self.volume = 0
        self.ch = 1

class Controle(Tv):
    def __init__(self):
        super().__init__()
    
    def aumentar_volume(self):
        self.volume += 1

    def abaixar_volume(self):
        self.volume -= 1

    def passar_ch(self):
        self.ch += 1

    def voltar_ch(self):
        self.ch -= 1

    def status(self):
        return {'volume':self.volume, 'ch':self.ch}

controle = Controle()
print(controle.status())
controle.aumentar_volume()
controle.aumentar_volume()
controle.passar_ch()
print(controle.status())
"""
