### 1

"""

def dobro(a):

    return a * 2

print(dobro(5))
"""


### 2

"""

def data_extenso(dd, mm, aa):

    match mm:
        case 1:

            print(f"{dd} de Janeiro de {aa}")

        case 2:

            print(f"{dd} de Fevereiro de {aa}")

        case 3:

            print(f"{dd} de Março de {aa}")

        case 4:

            print(f"{dd} de Abril de {aa}")

        case 5:

            print(f"{dd} de Maio de {aa}")

        case 6:

            print(f"{dd} de Junho de {aa}")

        case 8:

            print(f"{dd} de Julho de {aa}")

        case 9:

            print(f"{dd} de Agosto de {aa}")

        case 10:

            print(f"{dd} de Setembro de {aa}")
        case 11:

            print(f"{dd} de Novembro de {aa}")

        case 12:

            print(f"{dd} de Dezembro de {aa}")

        case _:

            print(f"Data inválida por favor considere revisar o codigo")


data_extenso(11, 2, 2004)

"""


### 3

"""

def neg_num(a):

    if a < 0:

        return -1

    elif a > 0:
        return 1

    return 0

print(neg_num(0))
"""


### 4

"""

def quadrado_perfeito(a):

    raiz = int(a ** 1/2)

    if (raiz ** 2) == a:

        return f"O número {a} tem quadrado perfeito"

    return f"O núemro {a} não tem quadrado perfeito"


print(quadrado_perfeito(4))
"""


### 5

"""

def volume_esfera(raio):

    return ((4/3) * 3.14) * (raio**3)


print(volume_esfera(2.4))
"""


### 6

"""

def horario(horas, minutos, segundos):

    h = horas * 3600

    min = minutos * 60

    return h, min, segundos


print(horario(5, 12, 30))
"""


### 7

"""

def conv_fah(celsius):

    return celsius * (9/5) + 32


print(conv_fah(31))
"""


### 8

"""

def hipotenusa(a, b):

    return pow((a**2 + b**2), 1/2)


print(hipotenusa(3, 5))
"""


### 9

"""

def volume_cilindro(altura, raio):

    return 3.14 * (raio**2) * altura


print(volume_cilindro(12, 4))
"""


### 10

"""

def maior(valor1, valor2):

    if valor1 > valor2:

        return f"Valor {valor1} é maior"

    elif valor1 < valor2:

        return f"Valor {valor2} é maior"

    return "Os valores são iguais"


print(maior(7, 7))
"""

### 11

"""

def notas_alunos(nota_1, nota_2, nota_3, letra):

    if letra.lower() == 'a':

        return nota_1 + nota_2 + nota_3 / 3

    elif letra.lower() == 'p':

        return (nota_1 * 5 + nota_2 * 3 + nota_3 * 2) / 10


print(notas_alunos(7, 8, 6, 'p'))
"""


### 12

"""

def algarismo(numero):

    n = list(str(numero))

    soma = 0
    for i in n:

        soma += int(i)
    return soma


print(algarismo(52))
"""


### 13

"""

def equacao(num1, num2, eq):

    match eq:

        case '+':

            return num1 + num2

        case '-':

            return num1 - num2

        case '*':

            return num1 * num2

        case '/':

            return num1 / num2


print(equacao(5, 5, '/'))
"""


### 14

"""

def consumo(km, litros):

    consumo = km / litros

    if consumo < 8:

        print("Venda o carro!")

    elif consumo >= 8 and consumo < 14:

        print("Econômico!")

    elif consumo >= 14:

        print("Super Econômico!")


consumo(12, 1)
"""


### 15

"""
def triangulo(v1, v2, v3):
    if v1 > 0 and v2 > 0 and v3 > 0:
        if v1 + v2 > v3 or v2 + v3 > v1:
            if v1 == v2 and v2 == v3:
                return 'Triângulo equilátero'
            elif v1 == v2 or v2 == v3 or v3 == v1:
                return 'Triangulo isosceles'
            else:
                return 'Triangulo escaleno'
        else:
            return 'Não é um triângulo'
    else:
        return 'Valores inválidos'

print(triangulo(4, 3, 2))
"""

### 16

"""
def DesenharLinha(quantidade, sinal):
    x = ''
    for i in range(1,quantidade+1):
        x += str(sinal)
    return x

print(DesenharLinha(quantidade))
"""

### 17

"""
def NumerosInteiros(numero_1, numero_2):
    soma =0
    for i in range(numero_1+1, numero_2):
        soma += i
    return soma

print(NumerosInteiros(5, 8))
"""

### 18

"""
def parametro(x, z):
    return x ** z

print(parametro(5, 2))
"""

### 19
"""
def maior_primo(n):

    primos = []
    for i in range(n):
        c = 0
        for j in range(n):
            if i%(j+1) == 0: 
                c += 1
        if c == 2:
            primos.append(i)

    return(max(primos))
"""
### 20

"""
def quantos_primos(numero):
    qtd = 0
    for i in range(2, numero+1):
        for n in range(2,i+1):
            if i % n == 0:
                if i == n:
                    qtd += 1
                    print(f"O número {i} é primo.")
                else:
                    print(f"O número {i} não é primo.")
                    break
    return print(f"Tem exatamente {qtd} de números primos.")

x = int(input("Digite um número: "))
quantos_primos(x)
"""

### 21

"""
def gerar_linha(quantidade):
    for n in range(quantidade):
        for vezes in range(n):
            print("!", end="")
        print("!")
gerar_linha(5)
"""

### 22

def gerar_triangulo(quantidade):
    altura = 2*quantidade-1
    for n in range(int(altura/2)+1):
        for linha in range(n):
            print("*", end="")
        print("*")
    for n in range(int(altura/2)-1, -1, -1):
        for linha in range(n):
            print("*", end="")
        print("*")
gerar_triangulo(8)
