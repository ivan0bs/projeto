import os
import json
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
        print("3️⃣ -Sair")
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
            print("3️⃣ -Sair")
            print("")
            entrada1 = int(input())
        if entrada1 == 1:
            cadastrar()
        if entrada1 == 2:
            entrar()
        else:
            os.system('cls')
            break
def menurAlternativo():
    while True:
        os.system('cls')
        print("===========================MENU===========================")
        print("")
        print("Digite qual sua escolha!!")
        print("")
        print("1️⃣ -Produtos")
        print("2️⃣ -Carrinho")
        print("3️⃣ -Sair")
        print("")
        entrada1 = int(input())
        if entrada1 <= 0 or entrada1 >= 4:
            while True:
                os.system('cls')
                print("Número inválido!!")
                print("Por favor digite um número válido!!!")
                print("===========================MENU===========================")
                print("Digite qual sua escolha!!")
                print("")
                print("1️⃣ -Produtos")
                print("2️⃣ -Carrinho")
                print("3️⃣ -Sair")
                print("")
                entrada1 = int(input())
                if entrada1 == 1:
                    pass
                if entrada1 == 2:
                    pass
                else:
                    os.system('cls')
                    return
def menurPrincipal():
        os.system('cls')
        print("BEM-VINDO!!")
        tm.sleep(3)
        #os.system('cls')
        print("!MENU!")
        print("Digite 4 para voltar para o MENU!!")
        voltarParaMenur = int(input())
        if voltarParaMenur == 4:
            menurAlternativo()
def cadastrar():
    os.system('cls')
    print("========================CADASTRAR========================")
    with open("logins.json", "r") as arquivo:
        usuarios = json.load(arquivo)
    nomeNovo = input("Nome: ").strip().lower()
    for u in usuarios:
        if nomeNovo == u["nome"]:
            print("\033[1mNOME EXISTENTE\033[0m")
            return cadastrar()
    print("OBS: digite apenas os numeros do CPF!!")
    cpf = input("CPF: ").strip().lower()
    for u in usuarios:
        if cpf == u["cpf"]:
            print("\033[1mCPF JA REGISTRADO\033[0m")
            return cadastrar()
    contadorCPF = 0
    for i in cpf:
        contadorCPF += 1
    idade = int(input("Idade: ").lower().strip())
    while idade <3 and idade>150:
        print("Idade invalida!!")
        idade = int(input("Idade: "))
        if idade >3 and idade<150:
            break
    print("\033[1mSenha deve conter no minimo 8 digitos ou caracteres\033[0m")
    senhaNova = input("Senha: ").strip()
    contadorSenha = 0
    for i in senhaNova:
        contadorSenha +=1
    if idade > 18 and contadorCPF == 11 and contadorSenha == 8:
        novoUsuario = {
            "nome": nomeNovo.strip().lower(),
            "senha": senhaNova.strip(),
            "idade": idade,
            "cpf": cpf
        }
        usuarios.append(novoUsuario)
        with open("logins.json", "w") as arquivo:
            json.dump(usuarios, arquivo)
        menurPrincipal()
    else:
        menu()
def entrar():
    os.system('cls')
    print("==========================ENTRAR==========================")
    while True:
        fechar = 0
        with open("logins.json", "r") as arquivo:
            usuarios = json.load(arquivo)
        nome = input("User: ")
        senha = input("Senha: ")
        for u in usuarios:
            if nome == u["nome"] and senha == u["senha"]:
                print("\033[1mUSER EXISTENTE\033[0m")
                fechar = 1
                break
            else:
                print("\033[1mNOME OU SENHA INVÁLIDO!!\033[0m")
                print("==========================ENTRAR==========================")
        if fechar == 1:
            break
    menurPrincipal()
menu()