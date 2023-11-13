#Exercício 01
numeroUm = int(input("Informe o primeiro valor: "))
numeroDois = int(input("Informe o segundo valor: "))

if(numeroUm > numeroDois):
    print(numeroUm)
else:
    print(numeroDois)

#Exercício 02
vogais = ['a', 'e', 'i', 'o', 'u']
letra = str(input("Informe uma letra qualquer: ").lower())
if(letra in vogais):
    print("A letra informada é uma vogal!")
else:
    print("A letra informada não é uma vogal!")

