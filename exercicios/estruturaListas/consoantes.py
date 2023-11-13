# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

frase = "trabalhoso"
vogais = ["a", "e", "i", "o", "u"]
soma = 0

print("Consoante impressa: ")
for x in frase:
    for y in vogais:
        if(x == y):
            soma = soma + 1
            print(y, end=" ") #Imprimir na mesma linha
        
print("\nSoma das consoantes: ", soma)
