import math
import re
from random import randint
# 1
"""
palavra = input("Digite uma palavra: ")
print(palindromo := "È um palindromo" if palavra[::-1] == palavra else "Não é um palindromo")
"""
#2
"""
try:
    numero = int(input("Digite um numero: "))
except:
    raise ValueError("Numero invalido.")

fatorial = math.factorial(numero)
    
subs = {"[":"", ']':"", ",": " * "}
resultado = f"{fatorial} (pois {numero}! = {str([n for n in range(numero, 0, -1)])})"

padrao = re.compile("|".join(re.escape(chave) for chave in subs.keys()))
print(padrao.sub(lambda chave: subs[chave.group()], resultado))
"""
# 3
"""
def numeroPrimo(numero):
    x = "É primo" if numero % 2 == 0 else "Não é primo"
    return x

print(numeroPrimo(2))
"""
# 4
"""
def contagemCarateres(texto: str):
    letras = {}

    for letra in texto.lower():
        letras[letra] = letras.get(letra, 0) + 1

    return letras

print(contagemCarateres('Olá, Mundo!'))
"""
# 5
"""
while True:
    try:
        entrada = int(input("Tente advinhar um numero de 1 a 100: "))
        break
    except:
        print("Por favor digite um numero inteiro!")

if entrada == (x := randint(1, 100)):
    print(f"Parabens você acertou o numero era: {x}")
else:
    print(f"Você errou o numero era {x}")
"""