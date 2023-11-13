# Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que 
# determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.
import random

idades = []
alturas = []
soma = 0

for x in range(3):
    idade = int(input("Informe a idade da {}° pessoa: " .format(x + 1)))
    altura = float(input("Informe a altura da {}° pessoa: " .format(x + 1)))

    soma += altura
    idades.append(idade)
    alturas.append(altura)

media = soma / len(alturas)

quantidadeAlunos = 0
for i in range(len(idades)):
    if(idades[i] > 13 and alturas[i] < media):
        quantidadeAlunos = quantidadeAlunos + 1

print("Quantidade de alunos com mais de 13 anos que possuam altura inferior a média de altura é: ", quantidadeAlunos)