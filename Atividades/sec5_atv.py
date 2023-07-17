### 1
#x, y = int(input("Digite um valor: ")), int(input("Digite outro valor: "))

#if x > y:
#    print(f"O numero {x} é maior que o numero {y}.")
#elif x == y:
#    print(f"Os numeros são identicos.")
#else:
#    print(f"O numero {y} é maior que o numero {x}.")    

### 2
#while True:
#    x = float(input("Digite um numero: "))
#    if x >= 0:
#        res = x ** 0.5
#        break
#    else:
#        print("O número não é válido.")
    
#print(f"A raiz quadrada de {x} é {res:.2f}.")

### 3

#x = float(input("Digite um número: "))
#if x >= 0:
#    res = x ** 0.5
#    print(f"O numero é positivo então a sua raiz é: {res:.2f}.")
#else:
#    res = x * 2
#    print(f"O numero é negativo então o seu quadrado é: {res:.2f}.")

### 4

#while True:
#    x = float(input("Digite um numéro: "))
    
#    if x >= 0:
#       y = quadrado(x)
#       z = raiz(y)
#       break
#    else:
#        print("Por favor digite um valor positivo...")
#print(f"O valor digitado foi {x:.2f}, seu quadrado é {y:.2f}, e a raíz do quadrado do número é {z:.2f}.")

### 5

#x = int(input("Digite um número: "))

#if (x%2) == 0:
#    print(f"O número {x}, é par.")
#else:
#    print(f"O número {x}, é impar.")

### 6
#x, y = int(input("Digite o primeiro número: ")), int(input("Digite o segundo número: "))
#if x > y:
#    res = x - y
#    print(f"O número maior é {x}, então sua subtração é {res}.")
#else:
#    res = y - x
#    print(f"O número maior é {y}, então sua subtração é {res}.")

### 7
#x, y = int(input("Digite o primeiro numero: ")), int(input("Digite o segundo numero: "))
#if x == y:
#    print("Os números são iguais")
#else:
#    print("Os números não são iguais")

### 8
#x, y = float(input("Digite a primeira nota do aluno: ")), float(input("Digite a segunda nota do aluno: "))

#if x >= 0 and x <= 10 and y <= 10 and y >=0:
#    soma = x + y
#    res = soma / 2
#    print(f"As notas {x} e {y}, sua media é {res}.")
#else:
#    print("Os números são invalidos.")

### 9
#salario, prestacao = float(input("Digite seu salário: ")), float(input("Digite sua prestação: "))
#c = prestacao * 0.2

#if c <= salario:
#    print("Empréstino concedido.")
#else:
#    print("Empréstino não concedido.")

### 10

#while True:
#    altura, sexo = float(input("Digite a sua altura: ")), str(input("Digite seu sexo [H] ou [M]: "))

#    s = sexo.lower()    
#    if 'm' in s:
#        p = 62.1 * altura - 44.7
#        print(f"Como você definiu seu sexo como Mulher seu peso ideal é: {p:.2f}")
#        break
#    elif 'h' in s:
#        p = 72.7 * altura - 58
#        print(f"Como você definiu seu genero para Homem seu peso ideal é: {p:.2f}")
#        break
#    else:
#        print("Valores inválidos.")
### 11
#while True:
#    try:
#        x = int(input("Digite um número: "))
#        break
#    except:
#        print("Digite um número válido!")
#if x >= 0:
#    valores = []
#    y = str(x)

#    for z in list(y):
#        valores.append(int(z))
#    res = sum(valores)

#    print(f"A soma dos valores {list(y)}, é respectavamente {res}")

### 12
#import math

#x = int(input("Digite um número: "))

#if x >= 0:
#    res = math.log(x)
#    print(f"O logaritmo de {x} é {res:.2f}.")
#else:
#    print("Número inválido.")

### 13
#n1, n2, n3 = float(input("Digite a primeira nota: ")), float(input("Digite a segunda nota: ")), float(input("Digite a terceira nota: "))
#m_po = (1 * n1) + (1 * n2) + (2* n3) / 4
#if m_po >= 60:
#    print("Aprovado!")
#else:
#    print("Reprovado!")

### 14
#lb, av_s, ef = float(input("Digite a nota de laboratório: ")), float(input("Digite a nota de avaliação semestral: ")), float(input("Digite a nota do exame final: "))

#m_po = (2 * lb + 3 * av_s + 5 * ef) / 10

#print(lb, av_s, ef)

#if m_po >= 0:
#    if  ((m_po >= 0) and (m_po <= 2.9)):
#        print(f"REPROVADO...", m_po)
#    elif ((m_po >= 3) and (m_po <= 4.9)):
#        print(f"RECUPERAÇÃO...", m_po)
#    else:
#        print(f"PARABÉNS VOCÊ FOI APROVADO!", m_po)
#else:
#    print("Valores inválidos.")

### 15
#while True:
#    try:
#        x = int(input("Escolha um número de 1 à 10: "))
#        break
#    except:
#        print("Digite um valor válido.")

#match x:
#    case 1:
#        print("Domingo")
#    case 2:
#        print("Segunda")
#    case 3:
#        print("Terça")
#    case 4:
#        print("Quarta")
#    case 5:
#        print("Quinta")
#    case 6:
#        print("Sexta")
#    case 7:
#        print("Sabádo")
### 16
"""
x = int(input("Digite um número de 1 à 12: "))

match x:
    case 1:
        print("Janeiro")
    case 2:
        print("Feveiro")
    case 3:
        print("Março")
    case 4:
        print("Abril")
    case 5:
        print("Maio")
    case 6:
        print("Junho")
    case 7:
        print("Julho")
    case 8:
        print("Agosto")
    case 9:
        print("Setembro")
    case 10:
        print("Outubro")
    case 11:
        print("Novembro")
    case 12:
        print("Dezembro")
"""
### 17
#ba, be = float(input("Insira o tamanho da base maior: ")), float(input("Insira o tamanho da base menor: "))
#res = (ba + be) / 2
#print(f"A área do trapézio é : {res:.2f}")

"""
### 18
escolha = str(input("Qual calculo deseja? Ex: [(Soma) +,(Substração) - ,(Multiplicação) * ,(Divisão) /]: "))

if escolha == '+' or escolha == '-' or escolha == '*' or escolha == '/':
    n1, n2 = float(input("Digite o seu primeiro número: ")), float(input("Digite o seu segundo número: "))

match escolha:
    case '+':
        res = n1 + n2
        print(f"O resultado da sua conta é: ", res)
    case '-':
        res = n1 + n2
        print(f"O resultado da sua conta é: ", res)
    case '*':
        res = n1 + n2
        print(f"O resultado da sua conta é: ", res)
    case '/':
        res = n1 + n2
        print(f"O resultado da sua conta é: ", res)
"""
### 19
#x = int(input("Digite um númeor inteiro: "))

#if x >= 0:
#    y1 = x % 3
#    y2 = x % 5
#    if y1 != y2:
#        if y1 == 0:
#            print(f"O número {x} é divisivel por 3")
#        elif y2 == 0:
#            print(f"O número {x} é divisivel por 5")
#        else:
#            print(f"O número {x} não é divisor de 5 e nem de 3.")
#    else:
#        print(f"O número {x} é divisivel por 5 e por 3.")

### 20
"""
a, b, c = float(input("Digite o primeiro comprimento: ")), float(input("Digite o segundo comprimento: ")), float(input("Digite o terceiro comprimento: "))
soma = a + b
if c < soma:
    if a == b and a == c:
        print("É um triângulo equilátero.")
    elif a == b or a == c or b == c:
        print("É um triângulo isósceles.")
    elif a != b and c != b and c != a:
        print("É um triângulo escaleno.")
else:
    print("Não é um triângulo.")
"""
### 21
"""
while True:
    print("Escolha uma das opições baixo: \n",
        "[1] Faça a soma de dois números. \n",
        "[2] Diferença entre dois números maior para o menos. \n",
        "[3] Produto entre dois números.\n",
        "[4] Divisão entre dois números (O denominador não pode ser zero) \n")
    opc = int(input("Qual sua escolha: "))

    match opc:
        case 1:
            n1, n2 = int(input("Digite o seu primeiro número: ")), int(input("Digite o seu segundo número: "))
            res = n1 + n2
            print(f"O resultado da soma de {n1} e {n2} é {res}")
        case 2:
            n1, n2 = int(input("Digite o seu primeiro número: ")), int(input("Digite o seu segundo número: "))
            res = n1 - n2
            print(f"O resultado da diferença {n1} e {n2} é {res}")
        case 3:
            n1, n2 = int(input("Digite o seu primeiro número: ")), int(input("Digite o seu segundo número: "))
            res = n1 * n2
            print(f"O resultado do produto de {n1} e {n2} é {res}")
        case 4:
            n1, n2 = int(input("Digite o seu primeiro número: ")), int(input("Digite o seu segundo número: "))
            res = n1 / n2
            print(f"O resultado da divisão de {n1} e {n2} é {res}")
        case _:
            print("Opição escolhida inválida.")
    sair = input("Gostaria de sair do programa? digite sim ou não: ")
    if sair.lower() == "sim":
        break
"""
### 22
"""
idade = int(input("Digite sua idade: "))
t_s = int(input("Digite seu tempo de serviço: "))

if idade >= 65 or t_s >= 30:
    print("Pode ser aposentar.")
elif idade >=60 and t_s >= 25:
    print("Pode se aposentar")
else:
    print("Não pode se aposentar")
"""
### 23
"""
ano = int(input("Digite um ano: "))
if (ano % 4) == 0 and not (ano % 100) == 0:
    print(f"O ano de {ano} é bissexto.")
else:
    print(f"O ano de {ano} não é bissexto.")
"""
### 24
"""
mg = 0.7
sp = 0.12
rj = 0.15
ms = 0.8

valor_produto = float(input("Digite o valor do produto: "))
destino = str(input("Digite o estado desejado (mg, sp, rj, ms): "))

match destino.lower():
    case 'mg':
        acrescimo = valor_produto * mg
        print("O destino sera Mato grosso.")
        print(f"O valor final do produto será {valor_produto + acrescimo}")
    case 'sp':
        acrescimo = valor_produto * sp
        print("O destino sera São paulo.")
        print(f"O valor final do produto será {valor_produto + acrescimo}")
    case 'rj':
        acrescimo = valor_produto * rj
        print("O destino sera Rio de janeiro.")
        print(f"O valor final do produto será {valor_produto + acrescimo}")
    case 'ms':
        acrescimo = valor_produto * ms
        print("O destino sera Mato grosso do Sul.")
        print(f"O valor final do produto será {valor_produto + acrescimo}")
    case _:
        print("Estado inválido")
"""
### 25
"""
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

if a != 0:
    b_inv = b * -1
    delta = (b * 2) - (4 * a * c)
    x1 = (b_inv + pow(delta, 0.5)) / (2 * a)
    x2 = (b_inv - pow(delta, 0.5)) / (2 * a)

    print(f"A sua equação trás o resultado de x = [{x1}, {x2}].")
    if delta < 0:
        print("Não existe raiz")
    elif delta == 0:
        print(f"Existe uma raiz real: {pow(delta, 0.5)}, sendo uma Raiz unica.")
    elif delta >= 0:
        print(f"Suas Raizes são x = [{x1}, {x2}].")
else:
    print("Não é uma equação do segundo grau.")
"""
### 26
"""
km = int(input("Digite a quantidades de Km percorridos: "))
gas = int(input("Digite ta quantidade de gasolina gasta: "))
cos = km / gas

if cos < 8:
    print("Venda o carro!")
elif cos > 7 and cos < 15:
    print("Economico.")
elif cos > 12:
    print("Super economico!")
"""
### 27
"""
idade = int(input("Digite a idade do nadador: "))

if idade >= 5 and idade <= 7:
    print("Categoria infantil A")
elif idade >= 8 and idade <= 10:
    print("Categoria infantil B")
elif idade >= 11 and idade <= 13:
    print("Juventil A")
elif idade >= 14 and idade <= 17:
    print("Juventil B")
elif idade >= 18:
    print("Sênior")
"""
### 28
"""
print("Qual calculo você gostaria de fazer: ", 
            "(a) Geometrico.",
            "(b) Ponderada.",
            "(c) Hârmonica.",
            "(d) Aritmética")
while True:
    try:
        sw = str(input("Qual sua escolha: "))
        break
    except:
        print("Escolha uma opição válida")
        break

match sw.lower():
    case "a":
        num1, num2, num3 = int(input("Digite o primeiro número: ")), int(input("Digite o segundo número: ")), int(input("Digite o terceiro número: "))
        calculo = num1 * num2 * num3
        print(f"O resultado Geometrica dos números é {pow(calculo, 1/3):.2f}")
    case "b":
        num1, num2, num3 = int(input("Digite o primeiro número: ")), int(input("Digite o segundo número: ")), int(input("Digite o terceiro número: "))
        calculo = num1 + (2 * num2) + (3 * num3)
        print(f"O resultado Ponderada dos números é {calculo / 6:.2f}")
    case "c":
        num1, num2, num3 = int(input("Digite o primeiro número: ")), int(input("Digite o segundo número: ")), int(input("Digite o terceiro número: "))
        calculo = 1 / num1 + 1 / num2 + num3 / 1
        print(f"O resultado Hârmonica dos números é {calculo:.2f}")
    case "d":
        num1, num2, num3 = int(input("Digite o primeiro número: ")), int(input("Digite o segundo número: ")), int(input("Digite o terceiro número: "))
        calculo = (num1 + num2 + num3) / 3
        print(f"O resultado Aritmética dos números é {calculo / 6:.2f}")
    case _:
        print("Escolha inválida")
"""
### 29
"""
from random import randint
acertos = 0
for i in range(0, 5):
    x1 = randint(1, 100)
    x2 = randint(1, 100)

    res = x1 + x2
    entrada = int(input(f"Qual é o resultado da soma dos números {x1} e {x2}?: "))
    if entrada == res:
        acertos += 1
print(f"A sua quantidade de acertos foi: {acertos}")
"""
### 30
"""
x1, x2, x3 = int(input("Digite um número: ")), int(input("Digite outro número: ")), int(input("Digite mais um número: "))
valores = [x1, x2, x3]
print(f"Os valores em onder é: {sorted(valores)}")
"""
### 31
"""
altura = float(input("Digite sua altura: "))
peso = float((input("Digite seu peso: ")))

if altura < 1.20:
    if peso <= 60:
        print("Lista A")
    elif peso >= 60 and peso <= 90:
        print("Classe D")
    elif peso >= 90:
        print("Classe G")
elif altura >= 1.20 and altura < 1.70:
    if peso <= 60:
        print("Lista B")
    elif peso >= 60 and peso <= 90:
        print("Classe E")
    elif peso >= 90:
        print("Classe H")
elif altura >= 1.70:
    if peso <= 60:
        print("Lista C")
    elif peso >= 60 and peso <= 90:
        print("Classe F")
    elif peso >= 90:
        print("Classe I")
"""
### 32
"""
produto = int(input("Digite o código do produto: "))
quantidade = int(input("Informe a quantidade do produto: "))
produtos = ['Cachorro quente', 'Bauru simples','Bauru com ovo','Hamburger','Cheeseburger','Suco','Refrigerante']
valores = [1.20, 1.30, 1.50, 1.20, 1.70, 2.20, 1.00]
match produto:
    case 100:
        valor = valores[0] * quantidade
        print(f"O produto escolhido foi {produtos[0]}, o valor total a pagar é {valor}")
    case 101:
        valor = valores[1] * quantidade
        print(f"O produto escolhido foi {produtos[1]}, o valor total a pagar é {valor}")
    case 102:
        valor = valores[2] * quantidade
        print(f"O produto escolhido foi {produtos[2]}, o valor total a pagar é {valor}")
    case 103:
        valor = valores[3] * quantidade
        print(f"O produto escolhido foi {produtos[3]}, o valor total a pagar é {valor}")
    case 104:
        valor = valores[4] * quantidade
        print(f"O produto escolhido foi {produtos[4]}, o valor total a pagar é {valor}")
    case 105:
        valor = valores[5] * quantidade
        print(f"O produto escolhido foi {produtos[5]}, o valor total a pagar é {valor}")
    case 106:
        valor = valores[6] * quantidade
        print(f"O produto escolhido foi {produtos[6]}, o valor total a pagar é {valor}")
"""
### 33
"""
valor = float(input("Digite o preço do iten para descobrir o preço antigo e o novo: "))
mensagem = ['Barato', 'Normal','Caro','Muito caro']
preco_antigo = [0.05 , 0.10, 0.20]

if valor <= 50:
    valor += valor * preco_antigo[0]
elif valor > 50 and valor < 100:
    valor += valor * preco_antigo[1]
elif valor > 100:
    valor += valor * preco_antigo[2]

if valor >= 0 and valor < 80:
    print(f"Barato, o preço novo é: {valor}")
elif valor >= 80 and valor < 120:
    print(f"Normal, o preço novo é: {valor}")
elif valor >= 120 and valor <= 200:
    print(f"Caro, o preço novo é: {valor}")
elif valor > 200:
    print(f"Muito caro, o preço novo é: {valor}")
"""
### 34
"""
nota, faltas = float(input("Digite a nota do seu aluno: ")), float(input("Digite o número de faltas do aluno: "))
if faltas <= 20:
    if nota >= 9:
        print("O conceito aplicado é (A)")
    elif nota >= 7.5 and nota <= 8.9:
        print("O conceito aplicado é (B)")
    elif nota >= 5 and nota <= 7.4:
        print("O conceito aplicado é (C)")
    elif nota >=4 and nota <= 4.9:
        print("O conceito aplicado é (D)")
    elif nota >= 0 and nota <= 3.9:
        print("O conceito aplicado é (E)")
else:
    if nota >= 9:
        print("O conceito aplicado é (B)")
    elif nota >= 7.5 and nota <= 8.9:
        print("O conceito aplicado é (C)")
    elif nota >= 5 and nota <= 7.4:
        print("O conceito aplicado é (D)")
    elif nota >=4 and nota <= 4.9:
        print("O conceito aplicado é (E)")
    elif nota >= 0 and nota <= 3.9:
        print("O conceito aplicado é (E)")
"""
### 35
"""
while True:
    data_entrada = str(input("Digite uma data no formato dd/mm/aa: ")).replace("/", " ")
    ano_bissesto = str(input("É um ano bissexto SIM/NÃO: ")).lower()
    data = data_entrada.split()

    if ano_bissesto == 'sim' or ano_bissesto == 'não':
        if int(data[1]) == 2 and int(data[0]) > 28 and ano_bissesto == 'não':
            print("Data inválida.")
        elif int(data[0]) <= 28:
            if int(data[1]) <= 12:
                    break
print(f"A data digitada é válida sendo, dia {data[0]} do mês {data[1]} de {data[2]}.")
"""
### 36
"""
valor = float(input("Digite o valor da venda: "))

if valor >= 100000.00:
    print(f"Sua comissão será: {700.00 + valor * 0.16}")
elif valor > 80_000.00 and valor < 100_000.00:
    print(f"Sua comissão será: {650.00 + valor * 0.14}")
elif valor <= 80000.00 and valor > 60_000.00:
    print(f"Sua comissão será: {600.00 + valor * 0.14}")
elif valor < 40000.00 and valor >= 60_000.00:
    print(f"Sua comissão será: {550.00 + valor * 0.14}")
elif valor <= 40000.00 and valor > 20_000.00:
    print(f"Sua comissão será: {500.00 + valor * 0.14}")
elif valor <= 20_000.00:
    print(f"Sua comissão será: {400.00 + valor * 0.14}")
"""
### 37
"""
tempo = int(input("Digite quantos minutos ficou na vaga: "))
valor = 0
if tempo <= 60:
    valor += 1
else:
    valor += 2

if tempo >= 180:
    valor += 1.40
elif tempo > 300:
    valor += 2.00

print(f"O tempo que você vai pagar é: {valor}")
"""
### 38
"""
dd, mm, aa = int(input("Digite o dia: ")), int(input("Digite o mês: ")), int(input("Digite o ano: "))
biss = str(input("É um ano bissexto: ")).lower()

if dd > 0 and mm > 0 and aa > 0:
    if aa < 2008:
        if biss == 'não' and mm == 2 and dd == 29:
            print("Valor inválido pois não é ano bissexto.")
        elif biss == 'sim' and mm == 2 and dd == 29:
            print(f"Data válida: {dd}/{mm}/{aa}")
        elif biss == 'não' and dd < 29 and mm <= 12:
            print(f"Data válida: {dd}/{mm}/{aa}")
    else:
        print("Ano inválido.")
else:
    print("Valores inválidos.")
"""
### 39
"""
salario = float(input("Digite o salário do funcionário: "))
tempo = int(input("Digite o tempo de serviço em anos: "))

if tempo < 1:
    bonus = 0
elif tempo >= 1 and tempo <= 3:
    bonus = 100
elif tempo >= 4 and tempo <= 6:
    bonus = 200
elif tempo >= 7 and temop <= 10:
    bonus = 300
elif tempo > 10:
    bonus = 500

if salario <= 500:
    reajuste = salario * 0.25 + bonus
elif salario <= 1000:
    reajuste = salario * 0.20 + bonus
elif salario <= 1500:
    reajuste = salario * 0.15 + bonus
elif salario <= 2000:
    reajuste = salario * 0.10 + bonus
elif salario > 2000:
    reajuste = salario + bonus
print(f"O seu novo salário já é: {salario + reajuste - bonus}, e com um bônus de: {bonus}, totalizando {salario + reajuste}")
"""
### 40
"""
carro = float(input("Digite o valor do carro: "))

if carro <= 12000:
    distribuidor = carro * 0.05
    imposto = 0
elif carro > 12000 and carro <= 25000:
    distribuidor = carro * 0.10
    imposto = carro * 0.15
    
elif carro > 25000:
    distribuidor = carro * 0.15
    imposto = carro * 0.20
print(f"O valor do carro com os impostos é: {carro + distribuidor + imposto:.2f}
sendo o valor da distribuidora R$ {distribuidor:.2f} é o imposto de {imposto:.2f}")
"""
### 41
