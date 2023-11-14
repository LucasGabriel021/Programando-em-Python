"""
     Crie uma variável chamada “frase” e atribua a ela uma string de sua escolha. Em seguida, imprima a frase na tela.
     Crie um código que solicite uma frase e depois imprima a frase na tela.
     Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase digitada mas com todas as letras maiúsculas.
     Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase digitada mas com todas as letras minúsculas.
     Crie uma variável chamada “frase” e atribua a ela uma string de sua escolha. Em seguida, imprima a frase sem espaços em branco no início e no fim.
     Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase sem espaços em branco no início e no fim.
     Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase sem espaços em branco no início e no fim e em letras minúsculas.
     Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as vogais “e” trocadas pela letra “f”.
     Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as vogais “a” trocadas pela caractere “@”.
     Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as consoantes “s” trocadas pelo caractere “$”.
"""

# Exercício01
frase = "Red Dead"
print(f"A frase informada é: {frase}")

# Exercício02
campoFrase = input("Informe uma frase ou palavra: ")
print(f"A frase ou palavra informada é: {campoFrase}")

# Exercício03
campoFrase = input("Informe uma frase ou palavra: ")
print(f"A frase ou palavra informada é: {campoFrase.upper()}")

# Exercício03
frase02 = "  Red Dead é o melhor jogo do mundo!   "
print(f"A frase atribuida é: {frase02.strip()}")

# Exercício04
campoFrase02 = input("Informe uma frase com espaços no ínicio e fim: ")
print(f"A frase informada com espaços é: {campoFrase02.strip()}")

# Exercício05
campoFrase02 = input("Informe uma frase com espaços no ínicio e fim e em caixa alta: ")
print(f"A frase informada com espaços é: {campoFrase02.strip().lower()}")

# Exercício06
campoFrase03 = input("Informe uma frase ou palavra para trocar a letra (e) por (f): ")
print(f"A frase informada para a troca é: {campoFrase03.lower().replace('e', 'f')}")

# Exercício07
campoFrase03 = input("Informe uma frase ou palavra para trocar a letra (s) por ($): ")
print(f"A frase informada para a troca é: {campoFrase03.lower().replace('s', '$')}")

# Exercício08
campoFrase03 = input("Informe uma frase ou palavra para trocar a letra (a) por (@): ")
print(f"A frase informada para a troca é: {campoFrase03.lower().replace('a', '@')}")