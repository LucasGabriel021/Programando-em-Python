# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

notas = []
media = 0
soma = 0

for x in range(4): 
    nota = float(input("Informe a nota: "))
    notas.append(nota)
    soma += x

for x in notas:
    soma += x

media = soma / 4

print(notas)
print(soma)
print(media)