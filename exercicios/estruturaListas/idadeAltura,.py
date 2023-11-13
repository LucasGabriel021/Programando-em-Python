# Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação 
# no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

idades = []
alturas = []

print("Informe as idades e alturas correspondentes: ")
for i in range(5):
    idade = int(input("Informe a idade da pessoa {}: " .format(i+1)))
    altura = float(input("Informe a altura da pessoa {}: " .format(i+1)))

    idades.append(idade)
    alturas.append(altura)

print("\n")

print("Ordem inversa de idades: ")
for item in reversed(idades):
    print(item, end=" ")

print("\n\nOrdem inversa de alturas: ")
for item in reversed(alturas):
    print(item, end=" ")
