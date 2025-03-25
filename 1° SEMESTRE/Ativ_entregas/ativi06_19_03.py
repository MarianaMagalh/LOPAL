# ex 1
#print("Ano Bissexto!")
#ano = int(input("digite o ano: "))

#if ano // 4 == 0 :
   # print(f"O {ano} é bissexto")
#else :
   # print(f"O {ano} é bissexto")
#print("-------------------------------------------------------------------------------------------")
# ex 2
#print("IMC!")
'''
peso = float(input("Insira o seu peso: "))
altu = float(input("Insira a sua altura:"))

imc = peso / (altu ** 2)

if imc <= 18.5 :
    print(f"Seu IMC é {imc:,.2f}, logo sua classificação é baixo peso.")
elif imc >= 18.5 and imc <= 24.4 :
    print(f"Seu IMC é {imc:,.4f}, logo sua classificação é peso normal.")
elif imc >= 25 and imc <= 29.9:
    print(f"Seu IMC é {imc:,.2f}, logo sua classificação é sobrepeso.")
elif imc >= 30 and imc <= 34.9:
    print(f"Seu IMC é {imc:,.2f}, logo sua classificação é obesidade.")
elif imc >= 35 and imc <= 39.9:
    print(f"Seu IMC é {imc:,.42f}, logo sua classificação é obesidade mórbida.")
else:
    print(f"Seu IMC é {imc:,.2f}, logo sua classificação é obesidade extrema.")

'''
#print("-------------------------------------------------------------------------------------------")
# ex 3
#print("Desconto de Produto!")
'''
qtdprodutos = int(input("Insira a quantidade de produtos a ser pago: "))
valorprodutos = float(input("insira o valor dos produtos:"))

if qtdprodutos >= 100 :
    desconto = valorprodutos * (10/100)
    total = valorprodutos - desconto
    print(f"Valor Original: {valorprodutos}\nQuantidade de Produtos: {qtdprodutos}\nDesconto por unidade: {desconto}\nValor Final: {total}")
elif qtdprodutos < 100:
    desconto = valorprodutos * (5/100)
    total = valorprodutos - desconto
    print(f"Valor Original: {valorprodutos}\nQuantidade de Produtos: {qtdprodutos}\nDesconto por unidade: {desconto}\nValor Final: {total}")
else:
    print("Valores invalidos!")
'''
#print("-------------------------------------------------------------------------------------------")

# ex 4
#print("Voto Obrigatório!")
'''
idade = int(input("Insira a sua idade: "))

if idade < 18:
    print("Voto Obrigatorio")
elif idade >= 16 and idade <= 18 and idade >= 70:
    print("Voto Facultativo")
else:
    print("Voto Não Eleitor")
'''

#print("-------------------------------------------------------------------------------------------")

# ex 5
'''
print("Maior e Menor")

idaps1 = int(input("Insira a sua idade pessoa 1: "))
idaps2 = int(input("Insira a sua idade pessoa 2: "))
idaps3 = int(input("Insira a sua idade pessoa 3: "))

if idaps1 > idaps2 and idaps1 > idaps3:
    print("A pessoa 1 tem a maior idade.")
    if idaps2 > idaps3:
        print("A pessoa 3 da idade menor idade")
    else:
        print("A pessoa 2 tem a menor idade")

elif idaps2 > idaps3 and idaps2 > idaps1:
    print("A pessoa 2 tem a maior idade.")
    if idaps1 >  idaps3:
        print("A pessoa 3 tem a menor idade")
    else:
        print("a pessoa 1 tem a menor idade")
else:
    print("A pessoa 3 tem a maior idade")
    if idaps1 > idaps2:
        print("A pessoa 2 tem a menor idade")
    else:
        print("A pessoa 1 tem a menor idade")
'''
#print("-------------------------------------------------------------------------------------------")
'''
print("Validação do Horario!")
hora = int(input("Digite a hora: "))
min = int(input("Digite os minutos: "))
seg = int(input("Digite os segundo: "))

if hora >= 24 and hora < 0 and min >= 60 and seg >= seg:
    print("Horario Invalida!")
else:
    print("Horario Valida!")
'''
#print("-------------------------------------------------------------------------------------------")
'''
print("Conversao de variaveis")
notanum = int(input("Insira a nota do aluno: "))

if notanum <= 0 and notanum >= 10:
    print("Nota invalida!\nInsira novamente.")
else:
    print("Nota valida!")

notastg = str(notanum)

if notastg >= '9' and notastg == '10':
    print("A")
elif notastg >= '7' and notastg < '9':
    print("B")
elif notastg >= '5' and notastg < '7':
    print("C")
elif notastg >= '3' and notastg < '5':
    print("D")
else:
    print("E")
'''
#print("-------------------------------------------------------------------------------------------")
'''
print("Quadrado ou retagulo?")
la1 = int(input("Insira o primeiro lado: "))
la2 = int(input("Insira o segundo lado: "))
la3 = int(input("Insira o treceiro lado: "))
la4 = int(input("Insira o quarto lado: "))

if la1 == la2 and la1 == la3 and la1 == la4:
    print("Quadrado!")
else:
    print("Retagulo!")
'''
#print("-------------------------------------------------------------------------------------------")
'''
print("Calculadora")
num1 = float(input("Digite o primeiro valor: "))
num2 = float(input("Digite o segundo valor: "))

op = input("Qual operação vc irá utilizar?\n+, -, *, /")

if op == '+':
    soma = num1 + num2
    print(f"Resultado: {soma}")
elif op == '-':
    sub = num1 - num2
    print(f"Resultado: {sub}")
elif op == '*':
    multi = num1 * num2
    print(f"Resultado: {multi}")
else:
    div = num1 / num2
    print(f"Resultado: {div}")
'''
#print("-------------------------------------------------------------------------------------------")
'''
print("Calculadora de Média")
nota1 = int(input("Insira a primeira nota: "))
nota2 = int(input("Insira a segunda nota: "))
nota3 = int(input("Insira a terceira nota: "))

if nota1 < nota2 and nota1 < nota3:
    media = (nota2 + nota3) / 2
    print(f"Media: {media}")
elif nota2 < nota1 and nota2 < nota3:
    media = (nota1 + nota3) / 2
    print:(f"Media: {media}")
else:
    media = (nota1 + nota2) / 2
    print(f"Media: {media}")
'''
#print("-------------------------------------------------------------------------------------------")
# desafio
import random
# escolha de um numero aleatorio
numsecreto = random.randint(1, 10)

sugestao1 = int(input("Adivinhe o número entre 1 e 10: "))

if sugestao1 == numsecreto:
    print("Parabéns! Voce acertou!")
else:
    if sugestao1 < numsecreto:
        print("O número secreto é maior")
    else:
        print("O número secreto é menor")


sugestao2 = int(input("Tente mais uma vez: "))

if sugestao2 == numsecreto:
    print("Parabéns! Você acertou na segunda tentativa!")
else:
    print(f"Que pena! O número correto era {numsecreto}.")

