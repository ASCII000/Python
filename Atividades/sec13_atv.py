from io import StringIO

def criar_arquivo(NOME_ARQUIVO, CONTEUDO, EXTENSAO='txt'):
    with open(NOME_ARQUIVO + '.'+ EXTENSAO, 'w') as f:
        f.write(CONTEUDO)
# 1
"""
arr = open('arq.txt', 'w')
while True:
    valor = input("Digite o caractere, ou digite 0 para sair: ")
    print(valor)
    if valor != '0':
        arr.write(valor + "\n")
    else:
        break
arr.close()

with open('arq.txt') as f:
    for letra in f.read():
        print(letra)
"""
#2
"""
with open('pessoa.txt') as f:
    print(len(f.readlines()))
"""
#3
"""
vogais = 0
consoantes = 0

with open('pessoa.txt') as f:
    arq = f.read().lower()
    for letra in arq:
        if letra in 'aeiou':
            print(letra)
            vogais +=1
        else:
            consoantes += 1

print(f'Vogais: {vogais}, Consoantes: {consoantes}')
"""
# 4
"""
vv = {'vogais': 0, 'consoantes': 0}
with StringIO() as f:
    texto = input("Digite o seu texto: ")
    for letra in texto:
        if letra in 'aeiou':
            vv['vogais'] += 1
        elif letra.isalpha():
            vv['consoantes'] +=1
    criar_arquivo('teste', texto)
print(vv)
"""
# 5
"""
def ocorrencia_letra(arquivo):
    ocorrencias = 0
    with open(arquivo) as f:
        texto = f.read()
        caractere = input("Digite o caractere de busca: ")
        for letra in texto:
            if letra in caractere:
                ocorrencias += 1
    return ocorrencias

print(ocorrencia_letra('pessoa.txt'))
"""
#6
"""
def quantidade_letras(letra, texto):
    valor = 0
    for caractere in texto:
        if caractere in letra:
            valor += 1
    return valor

dicionario = {
    'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0,
    'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 
    'u': 0, 'a': 0, 'v': 0, 'x': 0, 'y': 0, 'z': 0
    }

print(dicionario[list(dicionario.keys())[0]])
print(list(dicionario.keys())[0])
with open('pessoa.txt') as f:
    texto = f.read().lower()
    for index in range(23):
        quantidade = 0
        dicionario[list(dicionario.keys())[index]] = quantidade_letras(list(dicionario.keys())[index], texto)
print(dict(sorted(dicionario.items(), key=lambda item: item[1], reverse=True)))
"""
# 7
"""
texto = ''
with open('pessoa.txt') as f:
    texto = f.read()
    sub = {'a': '*', 'e': '*', 'i': '*', 'o': '*', 'u': '*', }
    for k, v in sub.items():
        texto = texto.replace(k, v)
print(texto)
"""
# 8
"""
texto = ''
with open('pessoa.txt') as f:
    texto = f.read()
    t_nova = list((map(lambda x: x.lower(), texto)))
    print(''.join(t_nova))
with open('pessoa.txt', 'w') as f:
    arr = input("Digite os novos caracteres: ").lower()
    novo_texto = texto + ' ' + arr
    f.write(novo_texto)
"""
# 9
"""
arr1, arr2 = input("Digite o nome do arquivo: "), input(("Digite o nome do segundo arquivo: "))

texto1 = ''
with open(arr1) as f:
    texto1 = f.read()
with open(arr2) as f:
    texto2 = f.read()

criar_arquivo('novo_texto', texto1 + ' ' + texto2)
"""
# 10
"""
cidades = {}
with open('cidades.txt') as f:
    cidade = f.read()
    cidades = eval(cidade.replace('\n', ''))

filtro = list(sorted(cidades.items(), key=lambda x: x[1], reverse=True))
print(f"A cidade mais populosa é: {filtro[0][0]} com {filtro[0][1]} habitantes")
"""
#11
"""
arquivo = input("Digite o nome do arquivo: ")
with open(arquivo) as f:
    procurar = input("Digite a palavra para procurar: ")
    texto = f.read()
    print(texto.count(procurar))
"""
# 12

"""
def quantidade_letras(letra, texto):
    valor = 0
    for caractere in texto:
        if caractere in letra:
            valor += 1
    return valor

dicionario = {
    'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0,
    'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 
    'u': 0, 'a': 0, 'v': 0, 'x': 0, 'y': 0, 'z': 0
    }

with open('pessoa.txt', 'r', encoding='utf-8') as ff:
    lista = ['ç', 'é', 'á']
    texto = ff.read()

    for index in range(25):
        dicionario[list(dicionario.keys())[index]] = quantidade_letras(list(dicionario.keys())[index], texto)

    ff.seek(0)
    print(f"Quantidade de caracteres: {len(texto.replace(' ', ''))}")
    print(f"Quantidade de linhas: {len(ff.readlines())}")
    print(f"Quantidade de palavras: {len(texto.split(' '))}")
    print(f"Quantidade de letras: \n{dicionario}")
"""
# 13
"""
with StringIO() as lista:
    while True:
        numero = input("Digite o numero de telefone: ")
        if numero == "0":
            break
        lista.write(numero + '\n')

    # Agora, você pode obter a string com os números de telefone e fazer o que quiser com ela.
    lista_str = lista.getvalue()
    print(lista_str)
"""
#14
"""
import datetime

data_atual = str(datetime.date.today()).split('-')

def idade_pessoa(pessoa):
    idade = pessoa.replace('\n', '')[-11:].strip()
    idade_atual = list(map(lambda x: int(x), idade.split('/')))
    idade_aa = data_atual[2] - idade_atual[2]
    if int(data_atual[1]) < int(idade_atual[1]):
        if int(data_atual[0]) < int(idade_atual[0]):
            idade_aa += 1
    return idade_aa

idade_pessoa('Emerson da Silva 04/02/2004')

pessoas = []
with open('pessoas.txt') as ff:
    lista_de_pessoas = ff.readlines()
    for pessoa in lista_de_pessoas:
        nome = pessoa[:-11]
        idade = idade_pessoa(pessoa)
        with open('novas-pessoas.txt', 'w') as ff:
            ff.write(f'Nome: {nome} Idade: {idade}')
"""
#15
"""
lista_de_pessoas = []
with open('pessoa.txt') as ff:
    pessoas = list(map(lambda pessoa: pessoa.replace('\n', ''), ff.readlines()))
    for pessoa in pessoas:
        nome = pessoa[:40].strip()
        idade = f'{pessoa[46:]}/{pessoa[42:44]}/{pessoa[44:]}'
        lista_de_pessoas.append(nome + ' ' + idade + '\n')

    with open('pessoas.txt', 'w') as ff:
        ff.write(''.join(lista_de_pessoas))

nomes = list(map(lambda pessoa: pessoa.replace(pessoa.split()[-1], ''), lista_de_pessoas))
for index, pessoa in enumerate(lista_de_pessoas):
    data_hoje = [10, 4, 2023]
    data_nascimento = [int(n) for n in pessoa[len(pessoa)-11:len(pessoa)-1].split('/')]
    nome = nomes[index].replace('\n', '')

    idade = data_hoje[2] - data_nascimento[2]

    if data_hoje[1] < data_nascimento[1]:
        idade -= 1
    
    maior_de_idade = (lambda idade: 'Sim.' if idade >= 18 else 'Não.')

    print(f"Nome: {nome} é maior de idade: {maior_de_idade(idade)}")
"""
#16




        

