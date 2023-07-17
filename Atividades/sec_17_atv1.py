#1 / #2
"""
class Pessoa():

    def __init__(self, nome, endereco, telefone):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
    
    def infos(self):
        return self.__dict__

pessoa = Pessoa('Henrique', 'Sitio raposa', '12312351')
print(pessoa.infos())
"""
#3 / #4
"""
class Quadrado():
    def __init__(self, lado1, lado2, lado3, lado4):
        self.lados = [lado1, lado2, lado3, lado4]
        self.area = self.calcularArea()
        self.perimetro = self.calcularArea()

    def calcularArea(self):
        return self.lados[0] * self.lados[1]

    def calcularPerimetro(self):
        return sum(self.lados)

    def exibirInfos(self):
        return self.__dict__

pessoa = Quadrado(4, 4, 4, 4)
print(pessoa.exibirInfos())
"""
#5 / #6
"""
class Retangulo():
    
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura
        self.perimetro = self.calcularPerimetro()
        self.area = self.calcularArea()
    
    def calcularArea(self):
        return (self.comprimento * self.largura)

    def calcularPerimetro(self):
        return self.comprimento * 2

    def imprimir(self):
        return print(self.__dict__)

retangulo1 = Retangulo(5, 12)
retangulo1.imprimir()
"""
#7 / #8
"""
from typing import Optional

class Circulo():

    pi = 3.141516

    def __init__(self, raio, area: Optional[int] = None, perimetro: Optional[int] = None):
        self.raio = raio

        if not area:
            self.area = self.calcularArea()
        
        if not perimetro:
            self.perimetro = self.calcularPerimetro()

    def calcularArea(self):
        return (Circulo.pi * self.raio * self.raio)

    def calcularPerimetro(self):
        return (2 * Circulo.pi * self.raio)

    def imprimir(self):
        return self.__dict__

circulo1 = Circulo(12)
print(circulo1.imprimir())
"""
#9 / #10 / #11 / #12 / #13 / #14 / #15 / #16
"""
class Moto():

    def __init__(self, marca, modelo, cor, menorMarcha, maiorMarcha, motor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.marcha = 0
        self.maiorMarcha = maiorMarcha
        self.menorMarcha = menorMarcha
        self.motor = motor
    
    def subir_marcha(self):
        if not self.marcha == self.maiorMarcha:
            self.marcha += 1
            print(f'A marcha da moto subiu da {self.marcha - 1} para {self.marcha}')
        else:
            print(f'A moto tem apenas 5 marchas não sobe mais.')

    def descer_marcha(self):
        if not self.marcha == self.menorMarcha:
            self.marcha -= 1
            print(f'A marcha da moto desceu da {self.marcha + 1} para {self.marcha}')
        else:
            print(f'A moto já esta no neutro')

    def ligar(self):
        if self.motor == False:
            self.motor = True
            return print("Liguei a moto")
        else:
            return print("A moto esta ligada")
    
    def desligar(self):
        if self.motor == True:
            self.motor = False
            return print("Desliguei a moto")
        else:
            return print("A moto já esta desligada")

    def imprimir(self):
        return print(self.__dict__)



moto = Moto('Honda', '2010', 'vermelha', 1, 3, False)
moto.imprimir()
moto.subir_marcha()
moto.subir_marcha()
moto.descer_marcha()
moto.ligar()
moto.imprimir()
"""
# 17
