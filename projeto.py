import os
import time as tm
def menu():
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
            cadastrar()
        if entrada1 == 2:
            entrar()
        else:
            os.system('cls')
            break
def cadastrar():
    os.system('cls')
    print("========================CADASTRAR========================")
    listaDeUser = []
    nomeNovo = input("Nome: ")
    while True:
        logins = open("logins.txt", "r")
        #logins.white("Primeira linha do arquivo.\n Segunda linha do arquivo.\n")
        lines = logins.readlines()
        for contas in lines:
            pass
        logins.close()
        if nomeNovo in contas:
            print("\033[1mNOME EXISTENTE\033[0m")
            nomeNovo = input("Nome: ")
        else:
            break
    print("OBS: digite apenas os numeros do CPF!!")
    cpf = input("CPF: ")
    while True:
        logins = open("logins.txt", "r")
        #logins.white("Primeira linha do arquivo.\n Segunda linha do arquivo.\n")
        lines = logins.readlines()
        for contas in lines:
            pass
        logins.close()
        if cpf in contas:
            print("\033[1mCPF JA REGISTRADO\033[0m")
            cpf = input("CPF: ")
        else:
            break
    contadorCPF = 0
    for i in cpf:
        contadorCPF += 1
    idade = int(input("Idade: "))
    while idade <3 and idade>150:
        print("Idade invalida!!")
        idade = int(input("Idade: "))
        if idade >3 and idade<150:
            break
    print("Senha deve conter 8 digitos ou caracteres")
    senhaDeUser = input("Senha: ")
    contadorSenha = 0
    for i in senhaDeUser:
        contador2 +=1
    if idade > 18 and contadorCPF == 11 and contadorSenha == 8:
        contador=0
        os.system('cls')
        tm.sleep(1)
        print("BEM-VINDO!!")
        logins = open("logins.txt", "a")
        nomeDeUser = str(nome.strip().lower())
        listaDeUser.append(nomeDeUser)
        listaDeUser.append(senhaDeUser)
        listaDeUser.append(idade)
        listaDeUser.append(cpf)
        cadastro = str(listaDeUser)
        logins.writelines(f"\n{cadastro}")
        logins.close()
        tm.sleep(5)
        os.system('cls')
        print("!MENU!")
        print("Digite 4 para voltar para o MENU!!")
        voltarParaMenur = int(input())
        if voltarParaMenur == 4:
            menu()
    else:
        menu()
def entrar():
    os.system('cls')
    print("==========================ENTRAR==========================")
    nome = input("User: ")
    senha = input("Senha: ")
    while True:
        logins = open("logins.txt", "r")
        #logins.white("Primeira linha do arquivo.\n Segunda linha do arquivo.\n")
        lines = logins.readlines()
        for contas in lines:
            pass
        logins.close()
        if nome in contas:
            print("\033[1mUSER EXISTENTE\033[0m")
            break
        else:
            print("\033[1mUSER NÃO EXISTENTE\033[0m")
            print("Você sera redirigido para a pagina de login")
            tm.sleep(10)
            print("USER NÃO EXISTENTE")
    seila = input()
menu()