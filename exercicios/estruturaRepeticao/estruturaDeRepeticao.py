# # Exercício 01
# nota = 11
# while(nota < 0 or nota > 10):
#     nota = int(input("Insira um numero entre 10 e 0: "))
#     if(nota < 0 or nota > 10):
#         print("Insira um numero que corresponda a condição! ")

# #Exercício 02
# nameUser = str(input("Insira um nome de usuário: "))
# senhaUser = str(input("Insira um senha que não seja igual o nome de usuário: "))

# while(senhaUser == nameUser):
#     senhaUser = str(input("A senha não pode ser igual ao nome de usuário! Insira um senha que não seja igual o nome de usuário: "))

# print("Login cadastrado com sucesso: ")
# print("Usuário: ", nameUser)
# print("Senha: ", senhaUser)

#Exercício 03
nomeUsuario = str(input("Informe um nome: "))
while(len(nomeUsuario) <= 3):
    nomeUsuario = str(input("O nome deve ser maio que 3 caracteres: "))
    if(len(nomeUsuario) > 3):
        print("Nome cadastrado com sucesso! ")


idadeUsuario = int(input("Informe a idade: "))
while(idadeUsuario < 0 and idadeUsuario > 150):
    nomeUsuario = str(input("A idade deve estar entre 0 e 150! "))
    if(idadeUsuario > 0 and idadeUsuario < 150):
        print("Idade sucesso! ")
 