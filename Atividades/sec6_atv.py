
### 1
"""
while True:
    x = float(input("Digite um número: "))
    soma = 0
    if x > 0:
        for quantidade in range(1, 5+1):
            y = x
            x = x * 3
            print(f"O número {y} vezes 3 é: {x:.2f}")
        break
    else:
        print(f"Digite um número válido.")
"""
##2
"""
for numero in range(0, 100+1):
    print(numero)
var = 0

print("--------------------")

while var <= 99:
    var = var + 1
    print(var)

print("---------------------")

num = 0
while True:
    if num != 100:
        num = num + 1
        print(num)
    else:
        break    
"""
### 3
"""
for contandor in range(10, 0, -1):
    print(contandor)
print("FIM")
"""
### 4
"""
valor = 0
for loop in range (0, 101_000, 1000):
    print(loop)
"""
### 5
"""
soma = int(input("Digite um número: "))
res = 0
for loop in range(1,10):
    valor = int(input("Digite outro número: "))
    res = res + valor
print(res+soma)
"""
### 6
"""
loop = 0
res = 0
while loop < 10:
    soma = int(input("Digite um número para conta: "))
    res = res + soma
    loop = loop + 1
print(f"A media dos valores é: ", (res / 10))
"""
### 7
"""
res = 0
valores = []
for i in range(0, 10):
    soma = int(input("Digite um número postivo: "))
    
    if soma >= 0:
        res = res + soma
        valores.append(int(soma))
        print(res)
    else:
        print("Número inválido!")
print(f"A média dos seus números {valores} é: ", (res / 10))
"""
### 8
"""
res = 0
valores = []

for i in range(0, 10):
    soma = int(input("Digite um número para indexar: "))
    valores.append(int(soma))
valores.sort()
indice = len(valores) - 1
print(f"O valor mais baixo informado é {valores[0]}, o valor mais alto é {valores[-1]}")
"""
### 9
"""
x = int(input("Digite um número: "))
for i in range(1, x):
    pares = i % 2
    if pares != 0:
        print(f"É impar: ", i)
"""
### 10
"""
soma = 0
for n in range (1,50):
    pares = n % 2
    if pares == 0:
        soma = soma + n
        print(f"É par: ", n)
print(f"A soma desses números é:", soma)
"""
### 11
"""
x = int(input("Digite um número: "))
soma = 0
for i in range(0, x+1):
    print(i)
"""
### 12
"""
while True:
    try:
        x = int(input("Digite um número: "))
        break
    except:
        print("Digite um número por favor")

if x >= 0:
    for n in range(x+1, 0, -1):
        pares = n % 2
        if pares == 0:
            print(f"O número {n} é par.")
else:
    print("Número inválido.")
"""
### 13
"""
while True:
    try:
        x = int(input("Digite um número: "))
        break
    except:
        print("Digite um número por favor")

if x >= 0:
    for n in range(1, x+1):
        pares = n % 2
        if pares == 0:
            print(f"O número {n} é par.")
else:
    print("Número inválido.")
"""
### 14
"""
while True:
    try:
        x = int(input("Digite um número: "))
        break
    except:
        print("Digite um número por favor")

if x >= 0:
    for n in range(1, x+1):
        pares = n % 2
        if pares != 0:
            print(f"O número {n} é par.")
else:
    print("Número inválido.")

"""
### 15
"""
valor = int(input("Digite um número: ")) + 1
impares = 0
while True:
    impares = impares + 1
    if impares >= valor:
        break
    res = impares % 2
    if res != 0:
        print(impares)
"""
### 16
""""
loop = int(input("Digite um número: "))
for i in range(loop, 0, -1):
    impar = i % 2
    if impar != 0:
        print(f"O número: {i}")
"""
### 17
"""
loop = int(input("Digite um número: "))
soma = 0
for i in range(0, loop+1):
    if i == loop:
        print(f"A soma dos seus números naturais é: ", soma)
        break
    else:
        soma = soma + i
"""
### 18
"""
maior = 0
num = 0
rep = int(input("Digite a quantidades de números desejados: "))
for i in range(1, rep+1):
    antigo = num
    num = int(input(f"Digite o {i} desejado: "))
    if num > antigo:
        maior = maior + 1
print(f"A quantidades de vezes que um número maior foi dito foi: ", maior)
"""
### 19
"""
x = int(input("Digite um número de 100 à 999: "))
if x >= 100 and x <= 999:
    lista = str(x)
    for i in range(len(lista)):
        print(lista[i])
"""
### 20
"""
num = 0
while num != 1000:
    num = int(input("Digite um número: "))
    par = num % 2
    if par == 0:
        print(f"O número {num} é par")
    else:
        print(f"Por favor digite um número par.")
"""
### 21
"""
x, y = int(input("Insira um número: ")), int(input("Insira outro número: "))
soma = 0
multi = 1
for i in range (x, y+1):
    impares = i % 2

    if impares == 0:
        soma = soma + i
    else:
        multi = multi * i
print(f"A soma dos numeros pares é {soma}.")
print(f"A multiplicação dos numeros impares é {multi}.")
"""
### 22
"""
x = int(input("Quantas notas gostaria saber a média aritmética: "))
soma = 0
for i in range(0+1, x+1):
    nota = int(input(f"Digite a sua {i} nota: "))
    soma = soma + nota

    if nota > 20 or nota < 10:
        break
if nota <= 20 and nota >= 10:
    print(nota)
    res = soma / x
    print(f"Sua média aritmetica é: {res}")
else:
    print("Valores inválidos.")
"""
### 23
"""
x = int(input("Digite um número: "))

for i in range(1, x+1):
    div = x % i
    if div == 0:
        print(f"O número {i} é divisivel por {x}")
"""
### 24
"""
x = int(input("Digite um número: "))
soma = 0
for i in range(1, x):
    div = x % i
    if div == 0:
        print(i)
        soma = soma + i
print(f"A soma dos divisores é {soma}")
"""
### 25
"""
soma = 0
for i in range (1, 1000+1):
    v3 = i % 3
    v5 = i % 5

    if v3 == 0 or v5 == 0:
        soma = soma + i
print(f"A soma dos valores multiplos de 3 ou 5 é: ", soma)
"""
### 26
"""
num = int(input("Digite um número: "))
for i in range(1, num):
    m11 = i * 11
    m13 = i * 13
    m17 = i * 17
    if m11 == num and m13 == num:
        print(f"O número 11: {m11} e 13: {m13} , é multiplo de {num}.")
        break
    elif m17 == num:
        print(f"O número 17: {i}, é multiplo de {num}.")
        break
"""
### 27
"""
x = int(input("Digite um número: "))
soma = 0
for i in range (1, x+1):
    soma += 1/i
print(f"A soma hârmonica é: {soma:.2f}")
"""
### 28
"""
x = int(input("Digite o valor de E: "))
y = 1
soma = 0
for i in range(1, x+1):
    for n in range(1, i+1):
        y *= n
    soma += y
print(f"A soma dos fatoriais é: {soma}")
"""
### 29
"""
loop = 0
soma = 0
multi = 0
fatorial = 1
while loop != 5:
    loop += 1
    x = int(input(f"Digite o número {loop}: "))
    if x != 0:
        for i in range(2, x+1):
            multi += i
            fatorial = 1 * multi
            soma += fatorial
print(soma)
"""
### 30
"""
x1 = int(input("Digite a primeira sequência: "))
x2 = (2 * int(input("Digite a segunda sequência: "))) -1
x3 = (2 * int(input("Digite a segunda sequência: "))) -1
conta1 = 0
conta2 = 0
conta3 = 0

for i in range(1, x1+1):
    conta1 += i

for i in range(1, x2+1):
    impar = i % 2
    if impar == 1:
        conta2 += i
    else:
        conta2 -= i

for i in range(1, x3+1):
    impar = i % 2
    if impar == 1:
        conta3 += i
print(f"O valor da primeira formula é: {conta1}")
print(f"O valor da segunda formula é: {conta2}")
print(f"O valor da terceira formula é: {conta3}")
"""
### 31
"""
n = 0
res = 0

for i in range(1, 99+1, 2):
    n += 1
    res += i / n
print(f"O resutado da equação é: {res:.2f}")
"""
### 32
"""
from random import randint
giradas = int(input("Digite a quantidade de rodadas: "))
for i in range(1, giradas+1):
    d1 = randint(1, 9)
    d2 = randint(1, 9)

if d1 > d2:
    print(f"O resultado dos dois dados são: o dado 1 igual a {d1}, o dado 2 = {d2} sendo respectivamente {d1} maior que {d2}")
elif d2 > d1:
    print(f"O resultado dos dois dados são: o dado 1 igual a {d1}, o dado 2 = {d2} sendo respectivamente {d1} menor que {d2}")
elif d2 == d1:
    print(f"Os dois dados são iguais sendo o valor de ambos {d1}")
"""
### 33
"""
n = int(input("Digite o valor de N: "))
i = int(input("Digite o valor de I: "))
j = int(input("Digite o valor de J: "))

nat_nums, x = [], 0
while len(nat_nums) < n:
    if(x%i == 0 or x%j == 0):
        nat_nums.append(x)
    x += 1

print(nat_nums)
"""
### 34
"""
num = 0
while True:
    num += 1
    print(num)
    for i in range(1,20+1):
        div = num % i
        print(div)
        if div == 0:
            if i == 20:
                break:
        else:
            break
    if i == 20:
        break
print(f"O menor número divisivel de 1 até 20 é: {num}")
"""
"""
from math import lcm

print(lcm(*range(2, 21))) # 232792560
"""
### 35
"""
intervalo1, intervalo02 = int(input("Digite o primeiro valor do intervalo: ")), int(input("Digite o segundo valor do intervalo: "))
soma = 0
if intervalo1 < intervalo02:
    for i in range(intervalo1, intervalo02+1):
        valor = i % 2
        if valor != 0:
            soma += i
    print(f"A soma dos valores impares é: {soma}")
else:
    print("Valores informados inválidos.")
"""
### 36
"""
eq1 = 0
eq2 = 0
for i in range (1, 10+1):
    eq1 += i ** 2
    eq2 += i

print(f"A diferença da soma é {eq1} - {eq2*eq2} = {eq2*eq2-eq1}")
"""
### 37
"""
i = 1000
n1 = 0
n2 = 0
soma = 0
quadrado = 0
for i in range(1000, 9999+1):
    n1 = int(i / 100)
    n2 = int(i % 100)
    soma = n1 + n2
    quadrado = soma * soma

    if quadrado == i:
        print(n1, n2, soma)
        print(f"O número {i} é um dos números possiveis.")
"""
###38
"""
e1 = 0
e2 = 0

for i in range (1, 999+1):
    soma = 0
    e1 = i * i
    for i2 in range(1, 999+1):
        e2 = i2 * i2
        soma = e1 + e2

        if soma == 1000:
            print(f"Um resultado possivel da formulá é {i}² + {i2}² = {soma} = {soma**0.5:.2f}")
            break
"""
###39
"""
while True:
    altura= float(input("Digite a altura do seu triângulo: "))
    if altura <= 0:
        print("Valor da altura informado inválido.")
    else:
        break
while True:
    base =float(input("Digite a base do seu triângulo: "))
    if base <= 0:
        print("Valor da basa inválido")
    else:
        break
print(f"A área do seu triângulo é {base*altura / 2}")
"""
###40
"""
maior = 0
menor = 0
while True:
    x = int(input("Informe um número verdadeiro: "))
    if x < 0:
        break
    if x > maior:
        maior = x
    else:
        menor = x

print(f"O maior número informado foi {maior} é o menor {menor}")
"""
###41

