# Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares 
# no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
numerosPar = []
numerosImpar = []

for item in numeros:
    if((item % 2) == 0):
        numerosPar.append(item)
    else:
        numerosImpar.append(item)

print("\n")
print("Números: ", str(numeros))
print("Números Pares: ", str(numerosPar))
print("Números Impar: ", str(numerosImpar))
print("\n")