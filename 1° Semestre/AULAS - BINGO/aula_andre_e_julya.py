# Web Scraping
# ferramentas - requests, beautifulSoup

"""
import requests

url = "https://books.toscrape.com/"
response = requests.get(url)

print(response.status_code)

from bs4 import BeautifulSoup

html = response.text
soup = BeautifulSoup(html,'html.parser')

print(soup.prettify())

titulos = soup.find_all('h2', class_='titulo-noticia')

for titulo in titulos:
    print(titulo.text.strip())

with open ('titulos.txt', 'w', encoding='utf-8') as f:
    for titulo in titulos:
        f.write(titulo.text.strip() + '\n')

# user agente
headers={
    'User-Agent':'Mozilla/5.0...',
    'Accept-Languege':'pt-BR,pt;q=0.9',
    'Accept-Encoding':'gzip, deflate, br',
    'Referer':'https//:www.google.com/'
}
"""
from http.client import responses

import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

headers={
    'User-Agent':'Mozilla/5.0...'
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

livros = soup.find_all('article',class_='product_pod') # verifica se tem o item

for livro in livros:
    titulo = livro.h3.a['title']
    preco = livro.find('p', class_='price_color').text

    print(f'Titulo: {titulo} - Preço: {preco}')

#************************************************************************************************************************************************************************

# Manipulação de String - str()
# é o uso de métodos e operações que permitem alterar ou analisar sequencias de caracteres (as strings) de forma eficiente, com o objetivo
# de modificas, analisar ou extrair informações delas.

# operadores:
# + - print(f"{titulo + subtitulo}")
# * - multiplica str -> print(f"{10 * '='} menu {10 * '='}")
# in - procura uma string espeficica, sensivel, precisa ser igual
# str() - transforma uma variavel em string
# len() - retorna a quantidade de caracteres em uma string

# metodos
# .capitalize() - deixa tudo maiusculo
# .title() - deixa a primeira letra maiusculo
# .swapcase() - transforma as letras minusculas em maiusculas e vice-versa
# upper() - deixa tudo maiusculo
# .lower() - deixa tudo em minusculas
# .replace() - troca de palavras

# indexação - o que permite acessar e manipular partes especificas de uma string
# -> o indece é a posição de cada caractere na string
# -> a contagem do indice começa em zero. Indice negativos contam do fim para o inicio

palavra = 'oioi'

print(palavra [0])
print(palavra [2])

# negativo - conta de tras para a frente

print(palavra[-1])

# slicing - permite acessar uma subsequencia de caracteres, ou seja, uma parte da sequencia de strings, mas mantendo a ordem dos caracteres.
print(palavra[1:3])

# negativo
print(palavra[-3:])

# inverte strings
print(palavra[::-1])

# indetificação de caracteres
# .isalnum() - verifica se todos os caracteres são alfanumericos(letras ou numeros), não pode ter espaço, pois espaço nao é alfanumerico
# .isalpha() - verifica se todos os caracteres de uma string são letras
# .isdigit() - verifica se todos os caracteres de uma strings são digitos
# .islower()
# istitle() - verifica se a string esta no formato de titulo, a primeira letra maiuscula

# exer

palavra2 = input("Digite uma palavra: ")
maior = palavra2.upper()
menor = palavra2.lower()
primeira = palavra2.capitalize()
cada = palavra2.title()
trocada = palavra2.swapcase()
tamanho = len(palavra2)

print(f"Todas maiúsculas: {maior}")
print(f"Todas minusculas: {menor}")
print(f"A primeira maior: {primeira}")
print(f"Cada letra de cada palavra maiuscula: {cada}")
print(f"Trocadas: {trocada}")
print(f"Tamanho: {tamanho}")

# exer 2

palavra3 = "Aprendendo Python"

print(f"Trocando a palavra: {palavra3.replace('Python', 'JavaScript')}")
print(f"Verifica se python é Python: {'Python' in palavra3}")
print(f"Primeira letra: {palavra3[0]}")
print(f"A ultima letra: {palavra3[-1]}")
print(f"5 primeiros e 5 ultimos: {palavra3[5:-5]}")