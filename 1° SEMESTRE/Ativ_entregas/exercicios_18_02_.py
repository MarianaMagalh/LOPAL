# exercicio 1
# soma de dois números dado pelo usuário
print("Soma dos Valores!")
num1 = int(input("Digite um número: "))
num2 = int(input("Digite mais um número: "))

soma = num1 + num2

print(f"\nA soma dos números é {soma}.")
print("-----------------------------------------------------------------")

# exercicio 2
# verificação do resultado anterior é ímpar
print("Verificação do resultado é par ou ímpar!")
resul =  soma % 2 == 0

print(f"Se for um número ímpar é aparecerá falso, caso ao contario é verdadeiro: {resul}")
print("-----------------------------------------------------------------")

# exercicio 3
# verificar se o primeiro valor é maior que 3 e o segundo menor que 4
print("Maior que 3 e Menor que 4?")
print(f"O valor 1 é maior que 3: {num1 > 3}\nO valor 2 é menor que 4: {num2 < 4}")
print("-----------------------------------------------------------------")

# exercicio 4
# valor absoluto
print("Número Absoluto!")
# função abs() guarda o valor do usuário e retorna o valor absoluto
print(f"O número absoluto do valor 1 e valor 2 é: {abs(num1)} e {abs(num2)}")
print("-----------------------------------------------------------------")

# exercicio 5
# verificação de números pares
print("Ambos os valores são pares?")
#verifica se o resto da divisão por dois é zero
val1 = num1 % 2 == 0
val2 = num2 % 2 == 0

print(f"Os dois valores são pares: {val2 == val1}")
print("-----------------------------------------------------------------")

# exercicio 6
# verificação de um dos valores como negativo
print("Um dos valores é negartivo?")
print(f"O primeiro valor é negativo: {num1 < 0}")
print(f"O segundo valor é negativo: {num2 < 0}")
print("-----------------------------------------------------------------")

# exercico 7
# calculando a media dos 2 valores do usuario e o resultado
print("Calculo da média")
media = num1 + num2 + resul/3
print(f"A média é: {media}")
print("-----------------------------------------------------------------")

# exercicio 8
# exibir que o num1 + 15 é igual a num2 * 3
print("True or False?")
valores = num1 + 15 == num2 * 3

print(f"O valor 1 + 15 é igual a o valor 2 * 3: {valores}")
print("-----------------------------------------------------------------")

# exercicio 9
# calcular resultado e o resto da divisão do dividendo e o divisor, exibir tudo!
print("Dividendo e Divisor")




