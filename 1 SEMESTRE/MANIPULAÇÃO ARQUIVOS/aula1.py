# Manipulação de arquivos
# -> escrita e  leitura

"""
arquivos possiveis de manipular
- txt
- csv
- json
- xml
- excel

# Comandos
- .with.open()
- .write()
- .read()

# parametros
- r: read
- a: adicionar
- w: escrever
- x: criar

"""



# criação de arquivo
with open("C:/meu_arquivo.txt", "w") as arquivo:
    arquivo.write("Olá mundo!\n")
    arquivo.write("Aprendendo Python\n")

with open("meu_arquivo.txt", "r") as arquivo2:
    print(arquivo2.read())
