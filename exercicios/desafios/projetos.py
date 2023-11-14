"""
     1) Um programa deve ser escrito para ler dois números e, em seguida, perguntar à pessoa usuária qual operação 
     ele deseja realizar. O resultado da operação deve incluir informações sobre o número - se é par ou ímpar, 
     positivo ou negativo e inteiro ou decimal.
     
     2) Em uma empresa de venda de imóveis você precisa criar um código que analise os dados de vendas anuais para ajudar a diretoria na tomada de decisão. O código precisa coletar os dados de quantidade de venda durante os anos de 2022 e 2023 e fazer um cálculo de variação percentual. A partir do valor da variação, deve ser enviada às seguintes sugestões:
     Para variação acima de 20%: bonificação para o time de vendas.
     Para variação entre 2% e 20%: pequena bonificação para time de vendas.
     Para variação entre 2% e -10%: planejamento de políticas de incentivo às vendas.
     Para bonificações abaixo de -10%: corte de gastos.
"""

# Projeto01
numeroUm = float(input("Informe o primeiro valor: "))
numeroDois = float(input("Informe o segundo valor: "))
print("|+| - Somar")
print("|-| - Subtrair")
print("|+| - Multiplicar")
print("|+| - Dividir")
operacao = str(input("Informe a operação que deseja realizar: "))

if(operacao == '+'):
    soma = numeroUm + numeroDois
    print("\nInformações: ")
    print(f"Soma: {soma}")
    if((soma % 2) == 0):
        print("O número é Par!")
    else:
        print("O número é Impar!")
    if(soma < 0):
        print("O número é negativo!")
    else:
        print("O número é positivo!")
    if((soma // 1) == soma):
        print("O número é inteiro!")
    else:
        print("O número é decimal!")
elif(operacao == '-'):
    subtrair = numeroUm - numeroDois
    print("\nInformações: ")
    print(f"Subtração: {subtrair}")
    if((subtrair % 2) == 0):
        print("O número é Par!")
    else:
        print("O número é Impar!")
    if(subtrair < 0):
        print("O número é negativo!")
    else:
        print("O número é positivo!")
    if((subtrair // 1) == subtrair):
        print("O número é inteiro!")
    else:
        print("O número é decimal!")
elif(operacao == '*'):
    multiplicar = numeroUm * numeroDois
    print("\nInformações: ")
    print(f"Multiplicação: {multiplicar}")
    if((multiplicar % 2) == 0):
        print("O número é Par!")
    else:
        print("O número é Impar!")
    if(multiplicar < 0):
        print("O número é negativo!")
    else:
        print("O número é positivo!")
    if((multiplicar // 1) == multiplicar):
        print("O número é inteiro!")
    else:
        print("O número é decimal!")
else:
    dividir = numeroUm / numeroDois
    print("\nInformações: ")
    print(f"Divisão: {dividir}")
    if((dividir % 2) == 0):
        print("O número é Par!")
    else:
        print("O número é Impar!")
    if(dividir < 0):
        print("O número é negativo!")
    else:
        print("O número é positivo!")
    if((dividir // 1) == dividir):
        print("O número é inteiro!")
    else:
        print("O número é decimal!")

# Projeto02
qtdVendas2022 = int(input("Informe a quantidade de vendas do ano de 2022: "))
qtdVendas2023 = int(input("Informe a quantidade de vendas do ano de 2023: "))

variacaoPerc = ((qtdVendas2022 - qtdVendas2023) / qtdVendas2022) * 100
print(variacaoPerc)

if(variacaoPerc > 20):
    print("Bonificação para o time de vendas!")
elif(variacaoPerc >= 2 and variacaoPerc <= 20):
    print("Pequena bonificação para o time de vendas!")
elif(variacaoPerc < 2 and variacaoPerc < -10):
    print("Planejamento de políticas de incentivo às vendas!")
elif(variacaoPerc < -10):
    print("Corte de Gastos!")
