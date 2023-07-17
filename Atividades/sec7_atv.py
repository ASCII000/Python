### 1
"""
vetor = [1, -0, 5, -2, -5, 7]
soma1 = vetor[0] + vetor[1] + vetor[5]
print(soma1)

vetor[4] = 100
print(vetor)

for i in vetor:
    print(i)
"""
### 2
"""
valores = []
while len(valores) != 6:
    x = int(input("Digite um valor: "))
    valores.append(x)
print(valores)
"""
### 3
"""
valores = []
while len(valores) != 10:
    x = int(input("Digite um valor: "))
    valores.append(x)
y = []
for i in valores:
    z = i ** 2
    y.append(z)
print(f"Os valores {valores}, sendo o seu quadrado {y}.")
"""
### 4
"""
x = [10, 4, 2, 30, 1, 3, 4, 5]
y = [2, 4, 5, 4, 2, 4 ,6 ,5]

lista = []
for i in range(0, len(x)):
    z = x[i] + y[i]
    lista.append(z)
print(lista)

# - forma 2
d = []
for a, b in zip(x, y):
    d.append(a + b)
print(d)
"""
### 5
"""
x = [10, 4, 2, 30, 1, 3, 4, 5, 12, 15]
pares = []
for i in x:
    if (i % 2) == 0:
        pares.append(i)
print(f"Temos {len(pares)} de números pares, sendo eles {pares}.")
"""
### 6
"""
vetor = []
while len(vetor) != 10:
    x = int(input("Digite um número: "))
    vetor.append(x)
print(f"O maior valor digitado foi {max(vetor)}, o menor foi {min(vetor)}.")
"""
### 7
"""
vetor = []
while len(vetor) != 10:
    x = int(input("Digite um número: "))
    vetor.append(x)
print(f"O maior elemento encontrado foi {max(vetor)} na posição {vetor.index(max(vetor))}")
"""
### 8
"""
vetor = []
while len(vetor) != 6:
    x = int(input("Digite um número: "))
    vetor.append(x)
new_vector = list(reversed(vetor))
print(f"A ordem inversa dos valores é {new_vector}")
"""
### 9
"""
vetor = []
for _ in range(0, 6):
        x = int(input("Digite um número: "))
        if (x % 2) == 0:
                vetor.append(x)
print(f"A ordem inversa dos pares é: {list(reversed(vetor))}")
"""
### 10
"""
turma = int(input("Digite a quantidade da turma: "))
vetor = []
for i in range(1, turma+1):
    nota = int(input(f"Digite a nota do {i}º aluno: "))
    vetor.append(nota)
print(f"A média das notas da turma de {turma} alunos é {sum(vetor) / turma}")
"""
### 11
"""
vetor, neg = [], []
for _ in range(1, 10+1):
    x = float(input(f"Digite o {_} valor real: "))
    if x >= 0:
        vetor.append(x)
    else:
        neg.append(x)
print(f"A quantidade de números negativos é: {len(neg)}, a soma dos positivos é: {sum(vetor)}")
"""
### 12
"""
vetor = []
while len(vetor) != 5:
    x = int(input(f"Digite o {len(vetor)+1} valor: "))
    vetor.append(x)
print(f"Os valores lidos foram {vetor}, com o maior valor
sendo {max(vetor)} o menor sendo {min(vetor)} e a média dos valores {sum(vetor) / len(vetor)}")
"""
### 13
"""
vetor = []
while len(vetor) != 5:
    x = int(input(f"Digite o {len(vetor)+1} valor: "))
    vetor.append(x)
print(f"O maior valor foi {max(vetor)}, na posição {vetor.index(max(vetor))}")
print(f"O menor valor foi {min(vetor)}, na posição {vetor.index(min(vetor))}")
"""
### 14
"""
vetor = [1, 11, 1, 20, 22, 20, 11, 11, 29, 10]
valores = []
repetidos = set()

for i in vetor:
    if i not in valores:
        valores.append(i)
    else:
        repetidos.add(i)
print(valores)
print(repetidos)
"""
### 15
"""
vetor = [1, 1, 1, 5, 5 , 6, 7, 2, 20, 20, 30, 2, 6, 2, 3, 4, 29, 30, 20]
nova = set()
for n in vetor:
    nova.add(n)
print(nova)
### 16
"""
### 16
"""
vetor = [1, 4, 6, 5]
codigo = None

while codigo != 0:
    codigo = int(input("Digite um código: "))

    if codigo == 1:
        print(f"A ordem da lista é {vetor}")
    elif codigo == 2:
        print(f"A ordem inversa da lista é {list(reversed(vetor))}")
    elif codigo != 0 and codigo != None:
        print("Código inválido.")
"""
### 17
"""
vetor = [1, -2, 2, 10, 11, -20, 20, 11, -3, 10]
for i, valor in enumerate(vetor):
    if valor < 0:
        vetor[i] = 0
print(vetor)
"""
### 18
"""
vetor = [1, 4, 2, 5, 6, 7, 9, 11]
multiplo = []
for i in vetor:
    multiplo = []
    for n in range(len(vetor)):
        multiplo.append(i*n)
    print(f"Os mutiplos de {i} é {multiplo}.")
"""
### 19
"""
print(vetor2)
vetor = []
for i in range(1, 50+1):
    vetor.append((i+5*i)%(i+1))
print(vetor)
"""
### 20
"""
vetor1 = []
vetor2 = []

while len(vetor1) < 10:
    x = int(input(f"Digite o {len(vetor1)+1} desejado: "))
    if x >= 0 and x <= 50:
        vetor1.append(x)
        if (x % 2) == 0:
            vetor2.append(x)
print(f"Os números digitados foram {vetor1}, sendo números ímpares {vetor2}")
"""
### 21
"""
a, b = list(range(5)), list(range(5))
c = []
for i in a:
    x = int(input(f"Digite o {i+1} valor no vetor 1: "))
    a[i] = x
for i in b:
    x = int(input(f"Digite o {i+1} valor no vetor 2: "))
    b[i] = x
c = set(a) - set(b)
print(c)
"""
### 22
"""
a = [1, 11, 12, 4, 5, 10, 14, 20, 49, 50]
b = [3, 5, 6, 4, 1, 20, 40, 33, 51, 41]
c = list(range(10))

for i, num in enumerate(a):
    if (i % 2) != 0:
        c[i] = num
    for i, num in enumerate(b):
        if (i % 2) == 0:
            c[i] = num
print(c)
"""
### 23
"""
x = [1.5, 2.55, 4.12, 9.22, 10.222]
y = [2.11, 5.44, 1.412, 5.555, 9.112]
z = 0

for i in range(len(x)):
    z += float(x[i]) * float(y[i])
print(f"O valor escalar é {z}")
"""
### 24
"""
alunos = {}
def key_search(dicionario, valor):
    for chave, valor in a.items():
            if b == valor:
                return chave

while len(alunos) != 10:
    aluno = int(input("Digite o número do aluno: "))
    altura = float(input(f"Digite a altura do aluno {aluno}º: "))
    alunos[aluno] = altura

print(f"O aluno mais baixo é o aluno Nº {key_search(alunos, min(alunos.values()))}\ncom a altura em Metros {min(alunos.values())}")
print(f"O  aluno mais altro é o aluno Nº {max(alunos.values())}\n com a altura em metros {max(alunos.values())}")
"""
### 25
"""
vetor = []
for i in range(1,101):
    valor = list(str(i))
    if i % 7 == 0:
        vetor.append(i)
    elif '7' in valor:
        vetor.append(i)
print(vetor)
"""
### 26
"""
import statistics
lista = [1.44, 2.555, 2.50, 12.22, 1.200, 8.123, 7.999, 1.220, 1.999, 4.900]
desvio = statistics.pstdev(lista)
print(f"O desvio padrão é {desvio:.2f}")
"""
### 27
"""
vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
primos = []

for i in vetor:
    if i > 1:
        for i in range(2, i):
            if i % i == 0:
                pass
            else:
                primos.append(i)
print(f"Os números {vetor}, sendo primos {vetor}, nas posições: ")
for i in primos:
    if i in vetor:
        print(vetor[i])
"""

### 28

"""
v1 = {11, 4, 5, 9, 10, 3, 6, 59, 13, 30}
v2 = set()
v3 = set()

for i in v1:
    if i % 2 == 0:
        v2.add(i)
    else:
        v3.add(i)
print(f"Os números utilizados da lista {v1} sobraram {v1 - v2} para o pares e {v1 - v3} para os impares.")
"""

### 29

"""
valores = []
pares = []
ímpares = []
while len(valores) != 6:
    x = int(input("Digite um valor: "))
    valores.append(x)
    if x % 2 == 0:
        pares.append(x)
    else:
        ímpares.append(x)
print(f"A soma dos pares {pares} é {sum(pares)}, os números ímpares foram {ímpares} com sua quantidade {len(ímpares)}")
"""

### 30

"""
x = {1 , 3, 5, 1, 5, 6, 7, 5, 10, 11}
y = {1, 3, 4, 5, 6, 7, 7, 11, 12}

print(f"A interseção dos vetores é {x & y}")
"""

### 31

"""
vetor = {1, 1, 5, 5, 6, 7, 8, 3, 19, 29}
vetor_2 = {1, 4, 5, 44, 50, 23, 44, 55, 66, 11}
vetor_3 = vetor | vetor_2
print(vetor_3 )
"""

### 32

"""
x = []
y = []
soma = 0
produto = 0
for i in range(1,10+1):
    if i <= 5:
        valor = int(input(f"Digite o {i}º valor para o vetor X: "))
        x.append(valor)
    else:
        valor = int(input(f"Digite o {i-5}º valor para o vetor Y: "))
        y.append(valor)

for i in range(len(x)):
    produto = x[i] * x[2]
    soma = x[i] + y[i]

print(f"Vetores informados {x} e {y}")
print(f"A sua soma é {soma} com o produto {produto}")
print(f"Com a diferença de {(set(x) - set(y))}")
print(f"Com a interseção de {(set(x) & set(y))}")
print(f"Com a união de {(set(x) | set(y))}")
"""

### 33

"""
vetor = [11, 3, 4, 5, 3, 4, 0, 4, 0, 1, 4, 0, 12, 4, 0]
print(vetor)

for i, n in enumerate(vetor):
    if n == 0:
        vetor.pop(i)
print(vetor)
"""

### 34

"""
vetor = []
while len(vetor) != 10:
    x = int(input("Digite um valor: "))
    if x not in vetor:
        vetor.append(x)
    else:
        print("valor inválido")
print(vetor)
"""

### 35

"""
a = int(input("Digite um valor: "))
b = int(input("Digite outro valor: "))

if a < 1000 and b < 1000:
    vetor = list(str(a))
    vetor2 = list(str(b))
    res = []
    for i, v in enumerate(vetor):
        res.append(int(v))
        res.append(int(vetor2[i]))
print(sum(res))
"""

### 36

"""
vetor = []
numero = 0
while len(vetor) != 2:
    x = int(input(f"Digite o {len(vetor)+1}°: "))
    vetor.append(x)
vetor.sort()
print(vetor)
"""

### 37

"""
vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
vetor_ordenado1 = []
vetor_ordenado2 = []
for index, num in enumerate(vetor):
    if index < 5:
        vetor_ordenado1.append(num)
        vetor_ordenado1.sort()
    else:
        vetor_ordenado2.append(num)
        vetor_ordenado2.sort(reverse=True)
vetor_ordenado = vetor_ordenado1 + vetor_ordenado2
print(vetor_ordenado)
"""

### 38

"""
vetor = []
while len(vetor) != 10:
    x = int(input("Digite um número: "))
    vetor.append(x)
vetor.sort()
print(f"O seu vetor em ordem crescente é: {vetor}")
"""

### 39

"""
from math import factorial 
n = 5
for i in range(n): 
    for j in range(n-i+1): 
        print(end=" ") 
  
    for j in range(i+1): 
        print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ") 
  
    
    print() 
"""
