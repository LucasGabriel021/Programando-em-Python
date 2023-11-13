# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. 
# Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média 
# anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

tempMes = []
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
soma = 0

print("Insira as temperaturas abaixo:")
for x in range(1, 13):
    temperatura = float(input("Informe a temperatura média do mês {}: " .format(x)))
    soma += temperatura
    tempMes.append(temperatura)

media = (soma / len(tempMes))
print("\n")

print("Meses com temperaturas acima da média no ano!")
for item in range(len(tempMes)):
    if(tempMes[item] > media):
        print("A média do mês {} - {} foi de {}" .format(item+1, meses[item],tempMes[item]))
