# ex 5
'''
n = int(input("Digite o tamanho da lista: "))

numeros = []
soma = 0

for _ in range(n):
    numero = float(input("Digite um número: "))
    numeros.append(numero)
    soma = soma + numero
media = soma / n
print(f"A média dos numeros é: {media}")
'''
from math import factorial

# While - estrutura que executa um bloco de código enquanto uma condição específica for verdadeira.
'''
# exe 

x = 0

while x <= 10:
    x = x + 1
    print(x)
'''

# soma += 1 - qunado é a mesma variavel (soma = soma + 1)
# ex 1
'''
num = int(input("Insira um numero de 5 ate 10: "))

if num >= 5 and num <= 10:
    while num > 0:
        num -= 1
        print(num)
else:
    print("Número deve estar entre 5 e 10")
'''

# ex 2
'''
maior = float(0.0)

contador = 1

while contador <= 5:
    numero = float(input("Digite um número: "))
    if numero > maior:
        maior = numero
    contador += 1
print(f"O maior numero é {maior}")

'''

# ex 3
'''
num = int(input("Digite um número: "))

fatorial = 1 
i = 1 

while i <= num:
    fatorial *= i
    i += 1

print(f"O resultado de {num}! é {fatorial}")
'''

# ex 4
num1 = int(input("Insira o primeiro valor: "))
num2 = int(input("Insira o primeiro valor: "))
num3 = int(input("Insira o primeiro valor: "))

i = 0

while