import os
import json
import time as tm
valor = 0
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
            print("Número inválido!!")
            print("Por favor digite um número válido!!!")
            entrada1 = int(input())
        else:
             break
    if entrada1 == 1:
            menurPrincipal()
    if entrada1 == 2:
            pass
    if entrada1 == 3:
        os.system('cls')
        return
def menurPrincipal():
        global valor
        os.system('cls')
        print("BEM-VINDO!!")
        tm.sleep(3)
        os.system('cls')
        print("!MENU!")
        print("Digite 4 para voltar para o MENU!!")
        print("1️⃣- Itens de Alimenticios")
        print("2️⃣- Itens de Limpeza")
        print("3️⃣- Itens de Igiene Pessoal")
        print("")
        escolha= int(input("Digite o número do Produto:"))
        while escolha <= 0 or escolha >= 5:
            print("Número inválido!!")
            print("Por favor digite um número válido!!!")
            tm.sleep(2)
            os.system('cls')
            print("!MENU!")
            print("Digite 4 para voltar para o MENU!!")
            print("1️⃣- Itens de Alimenticios")
            print("2️⃣- Itens de Limpeza")
            print("3️⃣- Itens de Igiene Pessoal")
            print("")
            escolha= int(input("Digite o número do Produto:"))
        if escolha == 1:
                os.system('cls')
                print("5️⃣- Voltar!")
                print("6️⃣- Confirma comprar!")
                print("==============Itens Alimentícios==============")
                print("1️⃣- Feijão = R$ 6,00")
                valorDoFejao = 6
                print("2️⃣- Arroz = R$ 5,00")
                valorDoArroz = 5
                print("3️⃣- Macarrão = R$ 4,50")
                valorDoMacaarrao = 4.50
                print("4️⃣- Peito de Frango = R$ 20,00")
                valorDoPeitoDeFrango = 20
                itensAlimenticios = int(input("Digite o número do Produto: "))
                if itensAlimenticios == 1:
                    with open("produtos.json", "r") as arquivo:
                        dados = json.load(arquivo)
                        feijao = dados[0].get("feijao", 0)
                    if feijao <= 0:
                        print("⚠️ Feijão fora de estoque!")
                        tm.sleep(2)
                        return menurPrincipal()
                    quantoUnidades = int(input(f"Feijão tem {feijao} unidades. Quantas unidades quer?"))
                    if quantoUnidades > feijao:
                        print("❌ Não há unidades suficientes em estoque.")
                        tm.sleep(2)
                        return menurPrincipal()
                    dados[0]["feijao"] = feijao - quantoUnidades
                    with open("produtos.json", "w") as arquivo:
                        json.dump(dados, arquivo)
                    print("1️⃣- Confimar Compra!!")
                    print(" 2️⃣- Para continuar comprando")
                    voltar = int(input())
                    if voltar == 1:
                        valor += valorDoFejao*quantoUnidades
                        print(f"Comprar no Valor: {valor}R$")
                        tm.sleep(15)
                        return menurAlternativo()
                    if voltar == 2:
                        valor += valorDoFejao*quantoUnidades
                        pass
                if itensAlimenticios == 2:
                    with open("produtos.json", "r") as arquivo:
                        dados = json.load(arquivo)
                    arroz = dados[0].get("arroz", 0)
                    if arroz <= 0:
                        print("⚠️ Arroz fora de estoque!")
                        tm.sleep(2)
                        return menurPrincipal()
                    quantoUnidades = int(input(f"Arroz tem {arroz} unidades. Quantas unidades quer?"))
                    if quantoUnidades > arroz:
                        print("❌ Não há unidades suficientes.")
                        tm.sleep(2)
                        return menurPrincipal()
                    dados[0]["arroz"] = arroz - quantoUnidades
                    with open("produtos.json", "w") as arquivo:
                        json.dump(dados, arquivo)
                    print("1️⃣- Confimar Compra!!")
                    print(" 2️⃣- Para continuar comprando")
                    voltar2 = int(input())
                    if voltar2 == 1:
                        valor += valorDoArroz*quantoUnidades
                        print(f"Comprar no Valor: {valor}R$")
                        tm.sleep(15)
                        return menurAlternativo()
                    if voltar2 == 2:
                        valor += valorDoArroz*quantoUnidades
                        pass
                if itensAlimenticios == 3:
                    with open("produtos.json", "r") as arquivo:
                        dados = json.load(arquivo)
                    macarrao = dados[0].get("macarrao", 0)
                    if macarrao <= 0:
                        print("⚠️ macarrao fora de estoque!")
                        tm.sleep(2)
                        return menurPrincipal()
                    quantoUnidades = int(input(f"Macarrão tem {macarrao} unidades. Quantas unidades quer?"))
                    if quantoUnidades > macarrao:
                        print("❌ Não há unidades suficientes.")
                        tm.sleep(2)
                        return menurPrincipal()
                    dados[0]["macarrao"] = macarrao - quantoUnidades
                    with open("produtos.json", "w") as arquivo:
                        json.dump(dados, arquivo)
                    print("1️⃣- Confimar Compra!!")
                    print(" 2️⃣- Para continuar comprando")
                    voltar2 = int(input())
                    if voltar2 == 1:
                        valor += valorDoMacaarrao*quantoUnidades
                        print(f"Comprar no Valor: {valor}R$")
                        tm.sleep(15)
                        return menurAlternativo()
                    if voltar2 == 2:
                        valor += valorDoMacaarrao*quantoUnidades
                        pass
                if itensAlimenticios == 4:
                    with open("produtos.json", "r") as arquivo:
                        dados = json.load(arquivo)
                    peitodefrango = dados[0].get("peitodefrango", 0)
                    if peitodefrango <= 0:
                        print("⚠️ Peito de Frango fora de estoque!")
                        tm.sleep(2)
                        return menurPrincipal()
                    quantoUnidades = int(input(f"Peito de Frango tem {peitodefrango} unidades. Quantas unidades quer?"))
                    if quantoUnidades > peitodefrango:
                        print("❌ Não há unidades suficientes.")
                        tm.sleep(2)
                        return menurPrincipal()
                    dados[0]["peitodefrango"] = peitodefrango - quantoUnidades
                    with open("produtos.json", "w") as arquivo:
                        json.dump(dados, arquivo)
                    print("1️⃣- Confimar Compra!!")
                    print(" 2️⃣- Para continuar comprando")
                    voltar2 = int(input())
                    if voltar2 == 1:
                        valor += valorDoPeitoDeFrango*quantoUnidades
                        print(f"Comprar no Valor: {valor}R$")
                        tm.sleep(15)
                        return menurAlternativo()
                    if voltar2 == 2:
                        valor += valorDoPeitoDeFrango*quantoUnidades
                        pass
                if itensAlimenticios == 5:
                    menurPrincipal()
        if escolha == 2:
                os.system('cls')
                print("""5️⃣- Voltar!
                 6️⃣- Confirma comprar!""")
                print(" ")
                print("2️⃣- Itens De Limpeza")
                print(" ")
                print("1️⃣- Detergente = R$ 6,00")
                valorDetergente = 6
                print("2️⃣- Água Sanitária = R$ 12,00")
                valorAguaSanitaria = 12
                print("3️⃣- Sabão em Pó = R$ 8,00")
                valorSabaoEmPo = 8
                print("4️⃣- Desinfetante = R$ 14,00")
                valorDesinfetante = 14
                itensDeLimpeza = int(input("Digite o número do Produto: "))
                if itensDeLimpeza == 1:
                    with open("produtos.json", "r") as arquivo:
                        dados = json.load(arquivo)
                    detegente = dados[1].get("detegente", 0)
                    if detegente <= 0:
                        print("⚠️ Feijão fora de estoque!")
                        tm.sleep(2)
                        return menurPrincipal()
                    quantoUnidades = int(input(f"Feijão tem {detegente} unidades. Quantas unidades quer?"))
                    if quantoUnidades > detegente:
                        print("❌ Não há unidades suficientes em estoque.")
                        tm.sleep(2)
                        return menurPrincipal()
                    dados[1]["detegente"] = detegente - quantoUnidades
                    with open("produtos.json", "w") as arquivo:
                        json.dump(dados, arquivo)
                    print("1️⃣- Confimar Compra!!")
                    print("2️⃣- Continuar comprando")
                    voltar = int(input())
                    if voltar == 1:
                        valor += valorDetergente*quantoUnidades
                        print(f"Comprar no Valor: {valor}R$")
                        tm.sleep(15)
                        return menurAlternativo()
                    if voltar == 2:
                        valor += valorDetergente*quantoUnidades
                        pass
                if itensDeLimpeza == 2:
                    with open("produtos.json", "r") as arquivo:
                        dados = json.load(arquivo)
                    aguasanitaria = dados[1].get("aguasanitaria", 0)
                    if aguasanitaria <= 0:
                        print("⚠️ Feijão fora de estoque!")
                        tm.sleep(2)
                        return menurPrincipal()
                    quantoUnidades = int(input(f"Feijão tem {aguasanitaria} unidades. Quantas unidades quer?"))
                    if quantoUnidades > aguasanitaria:
                        print("❌ Não há unidades suficientes em estoque.")
                        tm.sleep(2)
                        return menurPrincipal()
                    dados[1]["aguasanitaria"] = aguasanitaria - quantoUnidades
                    with open("produtos.json", "w") as arquivo:
                        json.dump(dados, arquivo)
                    print("1️⃣- Confimar Compra!!")
                    print("2️⃣- Continuar comprando")
                    voltar = int(input())
                    if voltar == 1:
                        valor += valorAguaSanitaria*quantoUnidades
                        print(f"Comprar no Valor: {valor}R$")
                        tm.sleep(15)
                        return menurAlternativo()
                    if voltar == 2:
                        valor += valorAguaSanitaria*quantoUnidades
                        pass
                if itensDeLimpeza == 3:
                    with open("produtos.json", "r") as arquivo:
                        dados = json.load(arquivo)
                    sabaoempo = dados[1].get("sabaoempo", 0)
                    if sabaoempo <= 0:
                        print("⚠️ Feijão fora de estoque!")
                        tm.sleep(2)
                        return menurPrincipal()
                    quantoUnidades = int(input(f"Feijão tem {sabaoempo} unidades. Quantas unidades quer?"))
                    if quantoUnidades > sabaoempo:
                        print("❌ Não há unidades suficientes em estoque.")
                        tm.sleep(2)
                        return menurPrincipal()
                    dados[1]["sabaoempo"] = sabaoempo - quantoUnidades
                    with open("produtos.json", "w") as arquivo:
                        json.dump(dados, arquivo)
                    print("1️⃣- Confimar Compra!!")
                    print("2️⃣- Continuar comprando")
                    voltar = int(input())
                    if voltar == 1:
                        valor += valorSabaoEmPo*quantoUnidades
                        print(f"Comprar no Valor: {valor}R$")
                        tm.sleep(15)
                        return menurAlternativo()
                    if voltar == 2:
                        valor += valorSabaoEmPo*quantoUnidades
                        pass
                if itensDeLimpeza == 4:
                    with open("produtos.json", "r") as arquivo:
                        dados = json.load(arquivo)
                    desinfetante = dados[1].get("desinfetante", 0)
                    if desinfetante <= 0:
                        print("⚠️ Feijão fora de estoque!")
                        tm.sleep(2)
                        return menurPrincipal()
                    quantoUnidades = int(input(f"Feijão tem {desinfetante} unidades. Quantas unidades quer?"))
                    if quantoUnidades > desinfetante:
                        print("❌ Não há unidades suficientes em estoque.")
                        tm.sleep(2)
                        return menurPrincipal()
                    dados[1]["desinfetante"] = desinfetante - quantoUnidades
                    with open("produtos.json", "w") as arquivo:
                        json.dump(dados, arquivo)
                    print("1️⃣- Confimar Compra!!")
                    print("2️⃣- Continuar comprando")
                    voltar = int(input())
                    if voltar == 1:
                        valor += valorPastaDeDente*quantoUnidades
                        print(f"Comprar no Valor: {valor}R$")
                        tm.sleep(15)
                        return menurAlternativo()
                    if voltar == 2:
                        valor += valorDesinfetante*quantoUnidades
                        pass
        if escolha == 3:
                os.system('cls')
                print("""3️⃣- Voltar!
                4️⃣- Confirma comprar!""")
                print(" ")
                print("1️⃣- Itens Alimentícios")
                print(" ")
                print("1️⃣- Papel = R$ 10,00")
                valorPapel = 10
                print("2️⃣- Pasta de Dente = R$ 8,00")
                valorPastaDeDente = 8
                itensDeIgienePessoal = int(input("Digite O número do Produto: "))
                if itensDeIgienePessoal == 1:
                    with open("produtos.json", "r") as arquivo:
                        dados = json.load(arquivo)
                    papel = dados[2].get("papel", 0)
                    if papel <= 0:
                        print("⚠️ Feijão fora de estoque!")
                        tm.sleep(2)
                        return menurPrincipal()
                    quantoUnidades = int(input(f"Feijão tem {papel} unidades. Quantas unidades quer?"))
                    if quantoUnidades > papel:
                        print("❌ Não há unidades suficientes em estoque.")
                        tm.sleep(2)
                        return menurPrincipal()
                    dados[2]["papel"] = papel - quantoUnidades
                    with open("produtos.json", "w") as arquivo:
                        json.dump(dados, arquivo)
                    print("1️⃣- Confimar Compra!!")
                    print("2️⃣- Continuar comprando")
                    voltar = int(input())
                    if voltar == 1:
                        valor += valorPapel*quantoUnidades
                        print(f"Comprar no Valor: {valor}R$")
                        tm.sleep(15)
                        return menurAlternativo()
                    if voltar == 2:
                        valor += valorPapel*quantoUnidades
                        pass
                if itensDeIgienePessoal == 2:
                    with open("produtos.json", "r") as arquivo:
                        dados = json.load(arquivo)
                    pastadedente = dados[2].get("pastadedente", 0)
                    if pastadedente <= 0:
                        print("⚠️ Feijão fora de estoque!")
                        tm.sleep(2)
                        return menurPrincipal()
                    quantoUnidades = int(input(f"Feijão tem {pastadedente} unidades. Quantas unidades quer? "))
                    if quantoUnidades > pastadedente:
                        print("❌ Não há unidades suficientes em estoque.")
                        tm.sleep(2)
                        return menurPrincipal()
                    dados[2]["pastadedente"] = pastadedente - quantoUnidades
                    with open("produtos.json", "w") as arquivo:
                        json.dump(dados, arquivo)
                    print("1️⃣- Confimar Compra!!")
                    print("2️⃣- Continuar comprando")
                    voltar = int(input())
                    if voltar == 1:
                        valor += valorPastaDeDente*quantoUnidades
                        print(f"Comprar no Valor: {valor}R$")
                        tm.sleep(15)
                        return menurAlternativo()
                    if voltar == 2:
                        valor += valorPastaDeDente*quantoUnidades
                        pass
        if escolha == 4:
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
    if idade > 18 and contadorCPF == 11 and contadorSenha >= 8:
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
                fechar = 1
                break
            else:
                print("\033[1mNOME OU SENHA INVÁLIDO!!\033[0m")
                print("==========================ENTRAR==========================")
        if fechar == 1:
            break
    menurPrincipal()
menu()