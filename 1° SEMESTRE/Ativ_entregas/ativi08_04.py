# exer 1
'''
numeros = 0

for num in range(10):
    resposta = int(input("Digite um número: "))
    if resposta % 3 == 0:
        print(f"O número {resposta} é multiplo ")
        numeros += 1
    else:
        print(f"Número {resposta} não é multiplo")
print(f"a quatidade dos números multiplos de 3: {numeros}")
'''


# exer 2
'''
print("Tentativas de Senhas")
while True:
    senha = input("Digite a 'senha correta' com encerrar: ")
    if senha == 'senha correta':
        break
'''

# exer 3
'''
while True:
    print("Menu:")
    print("sorvete")
    print("bolo")
    print("torta de morango")
    print("mousse de limão")
    print("bombom de morango")
    print("sair")

    op = input("Escolha uma das opções acima: ")

    if op == 'sair':
        break
'''

# exer 4
"""
num = int(input("Digite um número: "))

if num % 1 == 0 and num % num == 0:
    print("primo")
elif num 
"""

# exer 5
"""
senha = 1234

contador = 0

while contador < 4:
    senhaofc = int(input("Insira a sua senha: "))
    if senha == senhaofc:
        print("Seja bem vinde!")
        break
    else:
        contador += 1
        if contador == 3:
            print("Acesso bloqueado")
            break
"""

# exer 6
'''
pares = []
impares = []

for num in range(10):
    numeros = int(input("Insira um numero: "))

    if numeros % 2 == 0:
        pares.append(numeros)
    else:
        impares.append(numeros)


print(f"Lista de pares\n{pares}")
print(f"Lista de impares\n{impares}")
'''

# exer 7
vogais = ['a', 'e', 'i', 'o', 'u']

contador = 0


