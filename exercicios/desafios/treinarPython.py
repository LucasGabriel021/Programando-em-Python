"""
     1) Escreva um programa que peça à pessoa usuária para fornecer dois números e exibir o número maior.

     2) Escreva um programa que solicite o percentual de crescimento de produção de uma empresa e 
     informe se houve um crescimento (porcentagem positiva) ou decrescimento (porcentagem negativa).

     3) Escreva um programa que leia valores médios de preços de um modelo de carro por 3 anos consecutivos 
     e exiba o valor mais alto e mais baixo entre esses três anos.

     4) Escreva um programa que leia três números e os exiba em ordem decrescente.

     5) Escreva um programa que peça um número inteiro à pessoa usuária e determine se ele é par ou ímpar. Dica: Você pode utilizar o operador módulo %.

     6) Escreva um programa que peça um número à pessoa usuária e informe se ele é inteiro ou decimal.
"""

# Exercício01
valor1 = int(input("Informe o primeiro valor: "))
valor2 = int(input("Informe o segundo valor: ")) 

if valor1 > valor2:
    print(f"O primeiro valor: {valor1} é maior que o segundo valor: {valor2}")
else:
    print(f"O segundo valor: {valor2} é maior que o primeiro valor: {valor1}")

# Exercício02
percCrescProd = float(input("Informe o percentual de crescimento de produção: "))
if(percCrescProd < 0):
    print(f"Houve decrescimo de {percCrescProd}")
else:
    print(f"Houve crescimento de {percCrescProd}")

# Exercício03
valorMedioAno1 = float(input("Informe o valor médio de preços do modelo do carro no primeiro ano: "))
valorMedioAno2 = float(input("Informe o valor médio de preços do modelo do carro no segundo ano: "))
valorMedioAno3 = float(input("Informe o valor médio de preços do modelo do carro no terceiro ano: "))

if(valorMedioAno1 > valorMedioAno2 and valorMedioAno1 > valorMedioAno3):
    print(f"O valor mais alto foi o do primeiro ano {valorMedioAno1}")
    if(valorMedioAno2 > valorMedioAno3):
        print(f"O menor valor foi o do terceiro ano {valorMedioAno3}")
    else:
        print(f"O menor valor foi o do segundo ano {valorMedioAno2}")
elif(valorMedioAno2 > valorMedioAno1 and valorMedioAno2 > valorMedioAno3):
    print(f"O valor mais alto foi o do segundo ano {valorMedioAno2}")
    if(valorMedioAno1 > valorMedioAno3):
        print(f"O menor valor foi o do terceiro ano {valorMedioAno3}")
    else:
        print(f"O menor valor foi o do primeiro ano {valorMedioAno1}")
else:
    print(f"O valor mais alto foi o do terceiro ano {valorMedioAno3}")
    if(valorMedioAno1 > valorMedioAno2):
        print(f"O menor valor foi o do segundo ano {valorMedioAno2}")
    else:
        print(f"O menor valor foi o do primeiro ano {valorMedioAno1}")

# Exercício04
numero1 = int(input("Informe o primeiro valor: "))
numero2 = int(input("Informe o segundo valor: "))
numero3 = int(input("Informe o terceiro valor: "))

print("\nOrdem decrescente:")
if(numero1 > numero2 and numero1 > numero3):
    print(f"{numero1}")
    if(numero2 > numero3):
        print(f"{numero2}")
        print(f"{numero3}")
    else:
        print(f"{numero3}")
        print(f"{numero2}")
elif(numero2 > numero1 and numero2 > numero3):
    print(f"{numero2}")
    if(numero1 > numero3):
        print(f"{numero1}")
        print(f"{numero3}")
    else:
        print(f"{numero3}")
        print(f"{numero1}")
else:
    print(f"{numero3}")
    if(numero1 > numero2):
        print(f"{numero1}")
        print(f"{numero2}")
    else:
        print(f"{numero2}")
        print(f"{numero1}")

# Exercício05
numero = int(input("Informe um número qualquer: "))
if((numero % 2) == 0):
    print("O número é par")
else:
    print("O número é ímpar")

# Exercício06
numeroQualquer = float(input("Informe um número qualquer: "))
if((numeroQualquer // 1) == numeroQualquer):
    print(f"Número inteiro: {numeroQualquer}")
else:
    print(f"Número decimal: {numeroQualquer}")
