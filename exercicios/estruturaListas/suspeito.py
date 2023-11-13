"""
Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" 
O programa deve no final emitir uma classificação sobre a participação da 
pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

"""

perguntas = ["Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima", "Devia para a vítima?", "Já trabalhou com a vítima?"]
respostas = []

print("Responda as perguntas abaixo: ")
for x in range(len(perguntas)):
    print(perguntas[x])
    resposta = str(input("Responda sim ou não! "))
    respostas.append(resposta.lower())

qtdResSim = 0

for x in range(len(respostas)):
    if(respostas[x] == "sim"):
        qtdResSim = qtdResSim + 1

print(respostas)

if(qtdResSim == 2): 
    print("O individuo é SUSPEITO!")
elif(qtdResSim == 3 or qtdResSim == 4):
    print("O individuo é CÚMPLICE!")
elif(qtdResSim == 5):
    print("O individuo é ASSASSINO!")
else:
    print("O individuo é INOCENTE!")
