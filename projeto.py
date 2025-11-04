import os
import time as tm
c = 0
while True:
    os.system('cls')
    print("===========================MENU===========================")
    print("")
    print("Digite qual sua escolha!!")
    print("")
    print("1️⃣ -Cadastrar")
    print("2️⃣ -Entrar")
    print("➜ 🚪 -Sair")
    print("")
    entrada1 = int(input())
    while entrada1 <= 0 or entrada1 >= 4:
        os.system('cls')
        print("Número inválido!!")
        print("Por favor digite um número válido!!!")
        print("===========================MENU===========================")
        print("Digite qual sua escolha!!")
        print("")
        print("1️⃣ -Cadastrar")
        print("2️⃣ -Entrar")
        print("➜ 🚪 -Sair")
        print("")
        entrada1 = int(input())
    if entrada1 == 1:
        os.system('cls')
        nome = input("Nome: ")
        print("OBS: digite apenas os numeros do CPF!!")
        cpf = input("CPF: ")
        for i in cpf:
            c += 1
        idade = int(input("Idade: "))
        if idade > 18 and c == 11:
            c=0
            print("BEM-VINDO!!")
            seila = input()
    elif entrada1 == 2:
        os.system('cls')
        pass
    else:
        os.system('cls')
        break