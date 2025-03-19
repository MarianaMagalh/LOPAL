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

if qtdprodutos <= 100 :
    desconto = valorprodutos * (10/100)
    total = 
    print(f"Valor Original: {valorprodutos}\nQuantidade de Produtos: {qtdprodutos}\nDesconto por unidade: {desconto}\nValor Final: {}")

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
hora = int(input("Digite a hora: "))
min = int(input("Digite os minutos: "))
seg = int(input("digite os segundo: "))

if hora >= 24 and hora < 0 and min >= 60 and seg >= seg:
    print("Horario Invalida!")
else:
    print("Horario Valida!")
