import math
import re
# 1
"""
palavra = input("Digite uma palavra: ")
print(palindromo := "È um palindromo" if palavra[::-1] == palavra else "Não é um palindromo")
"""
#2

try:
    numero = int(input("Digite um numero: "))
except:
    raise ValueError("Numero invalido.")

fatorial = math.factorial(numero)
    
subs = {"[":"", ']':"", ",": " * "}
resultado = f"{fatorial} (pois {numero}! = {str([n for n in range(numero, 0, -1)])})"

padrao = re.compile("|".join(re.escape(chave) for chave in subs.keys()))
print(padrao.sub(lambda chave: subs[chave.group()], resultado))