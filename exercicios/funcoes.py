# Exercício01
def somaTres(n1, n2, n3):
    return n1 + n2 + n3

print(somaTres(5, 5, 5))

# Exercício02
def verificaNum(valor):
    if(valor >= 0):
        return 'P'
    else:
        return 'N'
    
print(verificaNum(-5))

# Exercício03

# Faça um programa que converta da notação de 24 horas para a notação de 12 horas. 
# Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em 
# dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e 
# uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ 
# para P.M. Assim, a função para efetuar as conversões terá um parâmetro formal para registrar 
# se é A.M. ou P.M. Inclua um loop que permita que o usuário repita esse cálculo para novos 
# valores de entrada todas as vezes que desejar.

horas = int(input("Informe as horas: "))
minutos = int(input("Informe os minutos: "))

def conversao(hora):
    return hora - 12

def apresentar(hr, mn):
    if(hr <= 12):
        print(f"{hr}:{mn}A")
    else:
        print(f"{hr}:{mn}P")

res = conversao(horas)

apresentar(res, minutos)