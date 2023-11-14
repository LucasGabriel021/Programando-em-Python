"""
     Crie um programa que solicite à pessoa usuária digitar seu nome, e imprima “Olá, [nome]!”.
     Crie um programa que solicite à pessoa usuária digitar seu nome e idade, e imprima “Olá, [nome], você tem [idade] anos.”.
     Crie um programa que solicite à pessoa usuária digitar seu nome, idade e altura em metros, e imprima “Olá, [nome], você tem 
     [idade] anos e mede [altura] metros!”.
"""

# Exercício 01
nome = str(input("Informe seu nome: "))
print(f"Olá, {nome}")

# Exercício 02
nome = str(input("Informe seu nome: "))
idade = int(input("Informe sua idade: "))
print(f"Olá, {nome}, você tem {idade} anos.")

# Exercício 03 
nome = str(input("Informe seu nome: "))
idade = int(input("Informe sua idade: "))
altura = float(input("Informe sua altura: "))
print(f"Olá, {nome}, você tem {idade} anos e mede {altura} metros!")