"""
    Primeiro trecho de código utilizando a linguagem Python
"""

if(5 > 4):
    print("Olá mundo")
    if(5 < 9):
        # Printando Olá mundo em outra lingua
        print("Hello Wordl")

# Variáveis
x = 5
y = "Nome"
print(y)

y = 7
print(y)

nome = str("Lucas")
a = int(10)
b = float(11) # Type Casting
# print(nome + x) Errado
print(nome, x) # Certo
print(type(nome)) # Função type retorna o tipo da variável

nome = 5
print(type(nome))


# Descompactação
fruits = ["banana", "maca", "laranja"]
c, d, e = "banana", "maca", "laranja"

print(fruits)
print(e)


# Funções

# Criar Função
def somaUm(k, w):
    return k + w

print(somaUm(2, 2))

# Utilizar uma variável como global
def soma(k, w):
   global resSoma # global, palavra-reservada para tronar uma função global.
   resSoma = k + w

soma(2, 4)
print(resSoma)