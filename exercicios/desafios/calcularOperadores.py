"""
     Crie um programa que solicite três valores numéricos à pessoa usuária e imprima a soma dos três valores.
     Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a subtração do primeiro pelo o segundo valor.
     Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a multiplicação dos dois valores.
     Crie um programa que solicite dois valores numéricos, um numerador e um denominador, e realize a divisão entre os dois valores. 
     Deixe claro que o valor do denominador não pode ser 0.
     Crie um programa que solicite dois valores numéricos, um operador e uma potência, e realize a exponenciação entre esses dois valores.
     Crie um programa que solicite dois valores numéricos, um numerador e um denominador e realize a divisão inteira entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.
     Crie um programa que solicite dois valores numéricos, um numerador e um denominador, e retorne o resto da divisão entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.
     Crie um código que solicita 3 notas de um estudante e imprima a média das notas.
     Crie um código que calcule e imprima a média ponderada dos números 5, 12, 20 e 15 com pesos respectivamente iguais a 1, 2, 3 e 4.
"""


# Exercício01
valor1 = float(input("Informe o primeiro valor: "))
valor2 = float(input("Informe o segundo valor: "))
valor3 = float(input("Informe o terceiro valor: "))
print(f"Resultado da soma: {valor1 + valor2 + valor3}")

# Exercício02
valor1 = float(input("Informe o primeiro valor: "))
valor2 = float(input("Informe o segundo valor: "))
print(f"Resultado da subtração: {valor1 - valor2}")

# Exercício03
valor1 = float(input("Informe o primeiro valor: "))
valor2 = float(input("Informe o segundo valor: "))
print(f"Resultado da multiplicação: {valor1 * valor2}")

# Exercício04
numerador = float(input("Informe o valor do numerador: "))
denominador = float(input("Informe o valor do denominador (ESTE VALOR NÃO PODE SER 0): "))
print(f"Resultado da divisão: {numerador / denominador}")

# Exercício05
operador = float(input("Informe o valor do operador: "))
potencia = float(input("Informe o valor da potência: "))
print(f"Resultado da exponenciação: {operador**potencia}")

# Exercício06
numerador = float(input("Informe o valor do numerador: "))
denominador = float(input("Informe o valor do denominador (ESTE VALOR NÃO PODE SER 0): "))
print(f"Resultado da divisão inteira: {numerador // denominador}")

# Exercício06
numerador = float(input("Informe o valor do numerador: "))
denominador = float(input("Informe o valor do denominador (ESTE VALOR NÃO PODE SER 0): "))
print(f"Resultado do resto da divisão do numerador pelo denominador: {numerador % denominador}")

# Exercício06
nota1 = float(input("Informe a primeira nota do aluno(a): "))
nota2 = float(input("Informe a segunda nota do aluno(a): "))
nota3 = float(input("Informe a terceira nota do aluno(a): "))
print(f"A média das três notas do aluno é de {(nota1 + nota2 + nota3) / 3}")

# Exercício07
mediaPonderada = ((5*1) + (12*2) + (20*3) + (15*4)) / (1 + 2 + 3 + 4)
print(f"A média ponderada é: {mediaPonderada}")