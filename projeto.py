import os
import json
import time as tm
nomeDeUserEditar = ""
senhaDeUserEditar = ""
valor = 0
produtos = [
    {
        "nome": "Feijão",
        "quantidade": 10,
        "preco":6
    },
    {
        "nome": "Arroz",
        "quantidade": 10,
        "preco":5
    },
    {
        "nome": "Macarrão",
        "quantidade": 10,
        "preco":4.5
    },
    {
        "nome": "Peito de frango",
        "quantidade": 10,
        "preco":20
    },
    {
        "nome": "Detergente",
        "quantidade": 10,
        "preco":6
    },
    {
        "nome": "Agua Sanitaria",
        "quantidade": 10,
        "preco":12
    },
    {
        "nome": "Sabaoempo",
        "quantidade": 10,
        "preco":8
    },
    {
        "nome": "Desinfetante",
        "quantidade": 10,
        "preco":14
    },
    {
        "nome": "Papel",
        "quantidade": 10,
        "preco":10
    },
    {
        "nome": "Pasta de dente",
        "quantidade": 10,
        "preco":8
    }
] 
userPadrao = [
    {
        "nome": "admin",
        "senha": "admin123",
        "idade": 19,
        "cpf": "12312312300"
    }
]
if not os.path.exists("produtos.json"):
    with open("produtos.json", "w",encoding="utf-8") as produtos_json:
        json.dump(produtos, produtos_json, indent=4,ensure_ascii=False)
if not os.path.exists("logins.json"):
    with open("logins.json", "w",encoding="utf-8") as logins:
        json.dump(userPadrao, logins,indent=4,ensure_ascii=False)
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
        if entrada1 == 1:
            return cadastrar()
        elif entrada1 == 2:
            return entrar()
        elif entrada1 == 3:
            os.system('cls')
            print("Finalizando...")
            tm.sleep(2)
            exit()
        else:
            print("Número inválido!")
            tm.sleep(1)
def menurAlternativo():
    while True:
        os.system('cls')
        print("===========================MENU===========================")
        print("")
        print("Digite qual sua escolha!!")
        print("")
        print("1️⃣ -Produtos")
        print("2️⃣ -Carrinho")
        print("3️⃣ -Perfil")
        print("4️⃣ -Sair")
        print("")
        entrada1 = int(input())
        if entrada1 == 1:
            return menurPrincipal()
        elif entrada1 == 2:
            pass
        elif entrada1 == 3:
            return perfil()
        elif entrada1 == 4:
            print("Finalizando...")
            tm.sleep(2)
            os.system('cls')
            return
        else:
            print("Número inválido!!")
            tm.sleep(2)
def menurPrincipal():
        while True:
            global valor
            os.system('cls')
            print("BEM-VINDO!!")
            tm.sleep(3)
            os.system('cls')
            print("!MENU!")
            print("Digite 0 para voltar para o MENU!!")
            print("Produtos:")
            with open("produtos.json", "r",encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
            for i, item in enumerate(dados):
                nome = item["nome"]
                print(f"{i+1} - {nome}")
            escolha= int(input("Digite o número do Produto: "))
            if escolha == 1413914:
                return admin()
            if escolha == 1:
                os.system('cls')
                print("5️⃣- Voltar!")
                print("6️⃣- Confirma comprar!")
                with open("produtos.json", "r",encoding="utf-8") as arquivo:
                    dados = json.load(arquivo)
                    valorDoFejao = dados[0].get("preco")
                    feijao = dados[0].get("quantidade")
                    nome = dados[0].get("nome")
                if feijao <= 0:
                        print(f"⚠️ {nome} fora de estoque!")
                        tm.sleep(2)
                        return menurPrincipal()
                quantoUnidades = int(input(f"{nome} tem {feijao} unidades. Quantas unidades quer? "))
                if quantoUnidades > feijao:
                        print("❌ Não há unidades suficientes em estoque.")
                        tm.sleep(2)
                        return menurPrincipal()
                dados[0]["quantidade"] = feijao - quantoUnidades
                with open("produtos.json", "w",encoding="utf-8") as arquivo:
                    json.dump(dados, arquivo, indent=4,ensure_ascii=False)
                print("1️⃣- Confimar Compra!!")
                print("2️⃣- Para continuar comprando")
                voltar = int(input())
                if voltar == 1:
                    valor += valorDoFejao*quantoUnidades
                    print(f"Comprar no Valor: {valor}R$")
                    print("Finalizando Comprar...")
                    tm.sleep(10)
                    return menurPrincipal()
                if voltar == 2:
                    valor += valorDoFejao*quantoUnidades
                    pass
            if escolha == 2:
                with open("produtos.json", "r",encoding="utf-8") as arquivo:
                    dados = json.load(arquivo)
                    valorDoArroz = dados[1].get("preco")
                    arroz = dados[1].get("quantidade")
                    nome = dados[1].get("nome")
                if arroz <= 0:
                    print(f"⚠️ {nome} fora de estoque!")
                    tm.sleep(2)
                    return menurPrincipal()
                quantoUnidades = int(input(f"{nome} tem {arroz} unidades. Quantas unidades quer? "))
                if quantoUnidades > arroz:
                    print("❌ Não há unidades suficientes.")
                    tm.sleep(2)
                    return menurPrincipal()
                dados[1]["quantidade"] = arroz - quantoUnidades
                with open("produtos.json", "w",encoding="utf-8") as arquivo:
                    json.dump(dados, arquivo,indent=4,ensure_ascii=False)
                print("1️⃣- Confimar Compra!!")
                print("2️⃣- Para continuar comprando")
                voltar2 = int(input())
                if voltar2 == 1:
                    valor += valorDoArroz*quantoUnidades
                    print(f"Comprar no Valor: {valor}R$")
                    print("Finalizando Comprar...")
                    tm.sleep(10)
                    return menurPrincipal()
                if voltar2 == 2:
                    valor += valorDoArroz*quantoUnidades
                    pass
            if escolha == 3:
                with open("produtos.json", "r",encoding="utf-8") as arquivo:
                    dados = json.load(arquivo)
                valorDoMacaarrao = dados[2].get("preco")
                macarrao = dados[2].get("quantidade")
                nome = dados[2].get("nome")
                if macarrao <= 0:
                    print(f"⚠️{nome} fora de estoque!")
                    tm.sleep(2)
                    return menurPrincipal()
                quantoUnidades = int(input(f"{nome} tem {macarrao} unidades. Quantas unidades quer? "))
                if quantoUnidades > macarrao:
                    print("❌ Não há unidades suficientes.")
                    tm.sleep(2)
                    return menurPrincipal()
                dados[2]["quantidade"] = macarrao-quantoUnidades
                with open("produtos.json", "w",encoding="utf-8") as arquivo:
                    json.dump(dados, arquivo,indent=4,ensure_ascii=False)
                print("1️⃣ Confimar Compra!!")
                print("2️⃣ Para continuar comprando")
                voltar2 = int(input())
                if voltar2 == 1:
                    valor += valorDoMacaarrao*quantoUnidades
                    print(f"Comprar no Valor: {valor}R$")
                    print("Finalizando Comprar...")
                    tm.sleep(10)
                    return menurPrincipal()
                if voltar2 == 2:
                    valor += valorDoMacaarrao*quantoUnidades
                    pass
            if escolha == 4:
                with open("produtos.json", "r",encoding="utf-8") as arquivo:
                    dados = json.load(arquivo)
                    valorDoPeitoDeFrango = dados[3].get("preco")
                    peitodefrango = dados[3].get("quantidade")
                    nome = dados[3].get("nome")
                if peitodefrango <= 0:
                    print(f"⚠️ {nome} fora de estoque!")
                    tm.sleep(2)
                    return menurPrincipal()
                quantoUnidades = int(input(f"{nome} tem {peitodefrango} unidades. Quantas unidades quer? "))
                if quantoUnidades > peitodefrango:
                    print("❌ Não há unidades suficientes.")
                    tm.sleep(2)
                    return menurPrincipal()
                dados[3]["quantidade"] = peitodefrango - quantoUnidades
                with open("produtos.json", "w",encoding="utf-8") as arquivo:
                    json.dump(dados, arquivo,indent=4,ensure_ascii=False)
                print("1️⃣- Confimar Compra!!")
                print("2️⃣- Para continuar comprando")
                voltar2 = int(input())
                if voltar2 == 1:
                    valor += valorDoPeitoDeFrango*quantoUnidades
                    print(f"Comprar no Valor: {valor}R$")
                    print("Finalizando Comprar...")
                    tm.sleep(10)
                    return menurPrincipal()
                if voltar2 == 2:
                    valor += valorDoPeitoDeFrango*quantoUnidades
                    pass
            if escolha == 5:
                with open("produtos.json", "r",encoding="utf-8") as arquivo:
                    dados = json.load(arquivo)
                valorDetergente = dados[4].get("preco")
                detegente = dados[4].get("quantidade", 0)
                nome = dados[4].get("nome")
                if detegente <= 0:
                    print(f"⚠️ {nome} fora de estoque!")
                    tm.sleep(2)
                    return menurPrincipal()
                quantoUnidades = int(input(f"Feijão tem {detegente} unidades. Quantas unidades quer? "))
                if quantoUnidades > detegente:
                    print("❌ Não há unidades suficientes em estoque.")
                    tm.sleep(2)
                    return menurPrincipal()
                dados[4]["quantidade"] = detegente - quantoUnidades
                with open("produtos.json", "w",encoding="utf-8") as arquivo:
                    json.dump(dados, arquivo,indent=4,ensure_ascii=False)
                print("1️⃣ Confimar Compra!!")
                print("2️⃣ Continuar comprando")
                voltar = int(input())
                if voltar == 1:
                    valor += valorDetergente*quantoUnidades
                    print(f"Comprar no Valor: {valor}R$")
                    print("Finalizando Comprar...")
                    tm.sleep(10)
                    return menurPrincipal()
                if voltar == 2:
                    valor += valorDetergente*quantoUnidades
                    pass 
            if escolha == 6:
                with open("produtos.json", "r",encoding="utf-8") as arquivo:
                    dados = json.load(arquivo)
                valorAguaSanitaria = dados[5].get("preco")
                aguasanitaria = dados[5].get("quantidade")
                nome = dados[5].get("nome")
                if aguasanitaria <= 0:
                    print(f"⚠️ {nome} fora de estoque!")
                    tm.sleep(2)
                    return menurPrincipal()
                quantoUnidades = int(input(f"{nome} tem {aguasanitaria} unidades. Quantas unidades quer? "))
                if quantoUnidades > aguasanitaria:
                    print("❌ Não há unidades suficientes em estoque.")
                    tm.sleep(2)
                    return menurPrincipal()
                dados[5]["quantidade"] = aguasanitaria - quantoUnidades
                with open("produtos.json", "w",encoding="utf-8") as arquivo:
                    json.dump(dados, arquivo,indent=4,ensure_ascii=False)
                print("1️⃣ Confimar Compra!!")
                print("2️⃣ Continuar comprando")
                voltar = int(input())
                if voltar == 1:
                    valor += valorAguaSanitaria*quantoUnidades
                    print(f"Comprar no Valor: {valor}R$")
                    print("Finalizando Comprar...")
                    tm.sleep(10)
                    return menurPrincipal()
                if voltar == 2:
                    valor += valorAguaSanitaria*quantoUnidades
                    pass 
            if escolha == 7:
                with open("produtos.json", "r",encoding="utf-8") as arquivo:
                    dados = json.load(arquivo)
                valorSabaoEmPo = dados[6].get("preco")
                sabaoempo = dados[6].get("quantidade")
                nome = dados[6].get("nome")
                if sabaoempo <= 0:
                    print(f"⚠️ {nome} fora de estoque!")
                    tm.sleep(2)
                    return menurPrincipal()
                quantoUnidades = int(input(f"{nome} tem {sabaoempo} unidades. Quantas unidades quer? "))
                if quantoUnidades > sabaoempo:
                    print("❌ Não há unidades suficientes em estoque.")
                    tm.sleep(2)
                    return menurPrincipal()
                dados[6]["quantidade"] = sabaoempo - quantoUnidades
                with open("produtos.json", "w",encoding="utf-8") as arquivo:
                    json.dump(dados, arquivo,indent=4,ensure_ascii=False)
                print("1️⃣- Confimar Compra!!")
                print("2️⃣- Continuar comprando")
                voltar = int(input())
                if voltar == 1:
                    valor += valorSabaoEmPo*quantoUnidades
                    print(f"Comprar no Valor: {valor}R$")
                    print("Finalizando Comprar...")
                    tm.sleep(10)
                    return menurPrincipal()
                if voltar == 2:
                    valor += valorSabaoEmPo*quantoUnidades
                    pass
            if escolha == 8:
                with open("produtos.json", "r",encoding="utf-8") as arquivo:
                    dados = json.load(arquivo)
                valorDesinfetante = dados[7].get("preco")
                desinfetante = dados[7].get("quantidade")
                nome = dados[7].get("nome")
                if desinfetante <= 0:
                    print(f"⚠️ {nome} fora de estoque!")
                    tm.sleep(2)
                    return menurPrincipal()
                quantoUnidades = int(input(f"{nome} tem {desinfetante} unidades. Quantas unidades quer? "))
                if quantoUnidades > desinfetante:
                    print("❌ Não há unidades suficientes em estoque.")
                    tm.sleep(2)
                    return menurPrincipal()
                dados[7]["quantidade"] = desinfetante - quantoUnidades
                with open("produtos.json", "w",encoding="utf-8") as arquivo:
                    json.dump(dados, arquivo,indent=4,ensure_ascii=False)
                print("1️⃣- Confimar Compra!!")
                print("2️⃣- Continuar comprando")
                voltar = int(input())
                if voltar == 1:
                    valor += valorDesinfetante*quantoUnidades
                    print(f"Comprar no Valor: {valor}R$")
                    print("Finalizando Comprar...")
                    tm.sleep(10)
                    return menurPrincipal()
                if voltar == 2:
                    valor += valorDesinfetante*quantoUnidades
                    pass
            if escolha == 9:
                with open("produtos.json", "r",encoding="utf-8") as arquivo:
                    dados = json.load(arquivo)
                valorPapel = dados[8].get("preco")
                papel = dados[8].get("quantidade")
                nome = dados[8].get("nome")
                if papel <= 0:
                    print(f"⚠️{nome}  fora de estoque!")
                    tm.sleep(2)
                    return menurPrincipal()
                quantoUnidades = int(input(f"{nome} tem {papel} unidades. Quantas unidades quer? "))
                if quantoUnidades > papel:
                    print("❌ Não há unidades suficientes em estoque.")
                    tm.sleep(2)
                    return menurPrincipal()
                dados[8]["papel"] = papel - quantoUnidades
                with open("produtos.json", "w",encoding="utf-8") as arquivo:
                    json.dump(dados, arquivo,indent=4,ensure_ascii=False)
                print("1️ Confimar Compra!!")
                print("2️⃣ Continuar comprando")
                voltar = int(input())
                if voltar == 1:
                    valor += valorPapel*quantoUnidades
                    print(f"Comprar no Valor: {valor}R$")
                    print("Finalizando Comprar...")
                    tm.sleep(10)
                    return menurPrincipal()
                if voltar == 2:
                    valor += valorPapel*quantoUnidades
                    pass
            if escolha == 10:
                with open("produtos.json", "r",encoding="utf-8") as arquivo:
                    dados = json.load(arquivo)
                valorPastaDeDente = dados[9].get("preco")
                pastadedente = dados[9].get("quantidade")
                nome = dados[9].get("nome")
                if pastadedente <= 0:
                    print(f"⚠️ {nome} fora de estoque!")
                    tm.sleep(2)
                    return menurPrincipal()
                quantoUnidades = int(input(f"{nome} tem {pastadedente} unidades. Quantas unidades quer? "))
                if quantoUnidades > pastadedente:
                    print("❌ Não há unidades suficientes em estoque.")
                    tm.sleep(2)
                    return menurPrincipal()
                dados[9]["pastadedente"] = pastadedente - quantoUnidades
                with open("produtos.json", "w",encoding="utf-8") as arquivo:
                    json.dump(dados, arquivo,indent=4,ensure_ascii=False)
                print("1️⃣ Confimar Compra!!")
                print("2️⃣ Continuar comprando")
                voltar = int(input())
                if voltar == 1:
                    valor += valorPastaDeDente*quantoUnidades
                    print(f"Comprar no Valor: {valor}R$")
                    print("Finalizando Comprar...")
                    tm.sleep(10)
                    return menurPrincipal()
                if voltar == 2:
                    valor += valorPastaDeDente*quantoUnidades
            if escolha == 0:
                return menurAlternativo()
            else:
                print("Número inválido!!")
                tm.sleep(2)
def admin():
    os.system("cls")
    print("1️⃣- Editar Produtos!!")
    print("2️⃣- Editar Clientes!!")
    adminEditar = int(input(": "))
    if adminEditar ==  1:
        os.system("cls")
        print("1️⃣- Editar Produtos!!")
        print("2️⃣- Excluir Produtos!!")
        print("2️⃣- Adicionar Produtos!!")
        while True:
            try:
                ed_ou_ex_DeProdutos = int(input(": "))
                if ed_ou_ex_DeProdutos == 1:
                    break
                else:
                    return admin()
            except ValueError:
                print("❌ Você digitou algo que não é número! Tente novamente.\n")
        if ed_ou_ex_DeProdutos == 1:
            print("Produtos:")
            with open("produtos.json", "r") as arquivo:
                dados = json.load(arquivo)
            print("Produtos cadastrados:")
            for i, item in enumerate(dados):
                nome = item["nome"]
                print(f"{i+1} - {nome}")
            print("Digite o numero do produto para excluir!")
            while True:
                try:
                    produto = int(input())
                    if produto == 1:
                        break
                    else:
                        return admin()
                except ValueError:
                    print("❌ Você digitou algo que não é número! Tente novamente.\n")
            while True:
                try:
                    print("1️⃣- Editar nome de Produtos!!")
                    print("2️⃣- Editar quantidade de Produtos!!")
                    nomeEditar = int(input())
                    if nomeEditar == 1:
                        novoNome = input("Digite o novo nome: ")
                        break
                    else:
                        return admin()
                except ValueError:
                    print("❌ Você digitou algo que não é número! Tente novamente.\n")
            os.system("cls")
            if nomeEditar == 1:
                with open("produtos.json", "r", encoding="utf-8") as arquivo:
                    produtos = json.load(arquivo)
                produto -= 1
                if True:
                    produtos[produto]["nome"]=novoNome
                    with open("produtos.json", "w",encoding="utf-8") as arquivo:
                        json.dump(produtos, arquivo,indent=4,ensure_ascii=False)
                    print(f"\033[1mNome do Produto Alterado agora o nome é {novoNome}!\033[0m")
                    tm.sleep(2)
            elif nomeEditar ==2:
                while True:
                    try:
                        print("Digite o nova Quantidade!!")
                        quantidadeEditar = int(input())
                        if quantidadeEditar >= 0:
                            break
                        else:
                            return admin()
                    except ValueError:
                        print("❌ Você digitou algo que não é número! Tente novamente.\n")
                with open("produtos.json", "r", encoding="utf-8") as arquivo:
                    produtos = json.load(arquivo)
                produto -= 1
                if True:
                    produtos[produto]["quantidade"]=quantidadeEditar
                    with open("produtos.json", "w",encoding="utf-8") as arquivo:
                        json.dump(produtos, arquivo,indent=4,ensure_ascii=False)
                    print(f"\033[1mA nova quantidade do Produto é {quantidadeEditar}!\033[0m")
                    tm.sleep(2)
            return admin()
        elif ed_ou_ex_DeProdutos == 2:
            os.system("cls")
            with open("produtos.json", "r") as arquivo:
                dados = json.load(arquivo)
            print("Produtos cadastrados:")
            for i, item in enumerate(dados):
                nome = item["nome"]
                print(f"{i+1} - {nome}")
            print("Digite o numero do produto para excluir!")
            produto = int(input())
            with open("produtos.json", "r") as produtos_json:
                produtos = json.load(produtos_json)
            if produto == 1:
                produtos.pop(0)
                with open("produtos.json", "w") as arquivo:
                    json.dump(produtos, arquivo,indent=4)
                print("produto excluido!")
                if produto == 2:
                    produtos.pop(1)
                    with open("produtos.json", "w") as arquivo:
                        json.dump(produtos, arquivo,indent=4)
                    print("produto excluido!")
                if produto == 3:
                    produtos.pop(2)
                    with open("produtos.json", "w") as arquivo:
                        json.dump(produtos, arquivo,indent=4)
                    print("produto excluido!")
                if produto == 4:
                    produtos.pop(3)
                    with open("produtos.json", "w") as arquivo:
                        json.dump(produtos, arquivo,indent=4)
                    print("produto excluido!")
                if produto == 5:
                    produtos.pop(4)
                    with open("produtos.json", "w") as arquivo:
                        json.dump(produtos, arquivo,indent=4)
                    print("produto excluido!")
                if produto == 6:
                    produtos.pop(5)
                    with open("produtos.json", "w") as arquivo:
                        json.dump(produtos, arquivo,indent=4)
                    print("produto excluido!")
                if produto == 7:
                    produtos.pop(6)
                    with open("produtos.json", "w") as arquivo:
                        json.dump(produtos, arquivo,indent=4)
                    print("produto excluido!")
                if produto == 8:
                    produtos.pop(7)
                    with open("produtos.json", "w") as arquivo:
                        json.dump(produtos, arquivo,indent=4)
                    print("produto excluido!")
                if produto == 9:
                    produtos.pop(8)
                    with open("produtos.json", "w") as arquivo:
                        json.dump(produtos, arquivo,indent=4)
                    print("produto excluido!")
                if produto == 10:
                    produtos.pop(9)
                    with open("produtos.json", "w") as arquivo:
                        json.dump(produtos, arquivo,indent=4)
                    print("produto excluido!")
    elif adminEditar == 2:
        os.system("cls")
        with open("logins.json", "r", encoding="utf-8") as arquivo:
            usuarios = json.load(arquivo)
        print("Digite o nome do Clientes:")
        cliente = input()
        for i in usuarios:
            if cliente == i["nome"]:
                print("\033[1mUSER ENCONTRADO\033[0m")
                for i in range(len(usuarios)):
                    if usuarios[i]["nome"] == cliente:
                        exCliete = i
        print("Digite 1 para excluir!")
        excluir = int(input())
        if excluir == 1:
            usuarios.pop(exCliete)
            with open("logins.json", "w",encoding="utf-8") as arquivo:
                json.dump(usuarios, arquivo,indent=4,ensure_ascii=False)
            print("Clientes excluido!")
        else:
            print("User Não encontrado!")
            return admin()
    else:
        return menurPrincipal()
def cadastrar():
    os.system('cls')
    print("========================CADASTRAR========================")
    with open("logins.json", "r", encoding="utf-8") as arquivo:
        usuarios = json.load(arquivo)
    nomeNovo = input("Nome: ").strip().lower()
    for i in usuarios:
        if nomeNovo == i["nome"]:
            print("\033[1mNOME EXISTENTE\033[0m")
            return cadastrar()
    print("OBS: digite apenas os numeros do CPF!!")
    cpf = input("CPF: ").strip().lower()
    for i in usuarios:
        if cpf == i["cpf"]:
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
        with open("logins.json", "w",encoding="utf-8") as arquivo:
            json.dump(usuarios, arquivo,indent=4,ensure_ascii=False)
        return menurPrincipal()
    else:
        return menu()
def entrar():
    global nomeDeUserEditar
    global senhaDeUserEditar
    os.system('cls')
    print("==========================ENTRAR==========================")
    while True:
        fechar = 0
        with open("logins.json", "r", encoding="utf-8") as arquivo:
            usuarios = json.load(arquivo)
        nomeDeUser = input("User: ")
        senhaDeUser = input("Senha: ")
        for u in usuarios:
            if nomeDeUser == u["nome"] and senhaDeUser == u["senha"]:
                fechar = 1
                nomeDeUserEditar = nomeDeUser
                senhaDeUserEditar = senhaDeUser
                break
            else:
                print("\033[1mNOME OU SENHA INVÁLIDO!!\033[0m")
                print("==========================ENTRAR==========================")
        if fechar == 1:
            break
    return menurPrincipal()
def perfil():
    global nomeDeUserEditar
    global senhaDeUserEditar
    with open("logins.json", "r", encoding="utf-8") as arquivo:
            usuarios = json.load(arquivo)
    for u in usuarios:
        if nomeDeUserEditar == u["nome"] and senhaDeUserEditar == u["senha"]:
            print(f"User:{nomeDeUserEditar}")
            print(f"Senha:{senhaDeUserEditar}")
            os.system("cls")
            print("1️⃣- Editar user!!\n2️⃣- Editar Senha!!\n3️⃣- Excluir User!!\n4️⃣- Voltar!!")
            while True:
                try:
                    editarConta = int(input("Digite um número: "))
                    break
                except ValueError:
                    print("❌ Você digitou algo que não é número! Tente novamente.\n")
            if editarConta == 1:
                while True:
                    try:
                        nomeEditar = int(input("Digite 1 para Editar nome: "))
                        if nomeEditar == 1:
                            novoNome = input("Digite o novo nome: ")
                            break
                        else:
                            return perfil()
                    except ValueError:
                        print("❌ Você digitou algo que não é número! Tente novamente.\n")
                os.system("cls")
                if nomeEditar == 1:
                    with open("logins.json", "r", encoding="utf-8") as arquivo:
                        usuarios = json.load(arquivo)
                    for i in usuarios:
                        if nomeDeUserEditar == i["nome"]:
                            for i in range(len(usuarios)):
                                if usuarios[i]["nome"] == nomeDeUserEditar:
                                    edCliete = i
                                    if True:
                                        usuarios[edCliete]["nome"]=novoNome
                                        with open("logins.json", "w",encoding="utf-8") as arquivo:
                                            json.dump(usuarios, arquivo,indent=4,ensure_ascii=False)
                                        print(f"\033[1mUser Alterado agora seu novo nome é {novoNome}!\033[0m")
                                        tm.sleep(2)
                return perfil()
            elif editarConta == 2:
                while True:
                    try:
                        senhaEditar = int(input("Digite 1 para Editar Senha: "))
                        if senhaEditar == 1:
                            novaSenha = input("Digite o nova Senha: ")
                            break
                        else:
                            return perfil()
                    except ValueError:
                        print("❌ Você digitou algo que não é número! Tente novamente.\n")
                os.system("cls")
                if senhaEditar == 1:
                    with open("logins.json", "r", encoding="utf-8") as arquivo:
                        usuarios = json.load(arquivo)
                    for i in usuarios:
                        if senhaDeUserEditar == i["senha"]:
                            for i in range(len(usuarios)):
                                if usuarios[i]["senha"] == senhaDeUserEditar:
                                    edCliete = i
                                    if True:
                                        usuarios[edCliete]["senha"]=novaSenha
                                        with open("logins.json", "w",encoding="utf-8") as arquivo:
                                            json.dump(usuarios, arquivo,indent=4,ensure_ascii=False)
                                        print(f"\033[1mUser Alterado agora seu nova Senha é {novaSenha}!\033[0m")
                                        tm.sleep(2)
                return perfil()
            elif editarConta == 3:
                while True:
                    try:
                        certeza = int(input("Digite 1 para confimar Exclusão: "))
                        break
                    except ValueError:
                        print("❌ Você digitou algo que não é número! Tente novamente.\n")
                os.system("cls")
                if certeza == 1:
                    with open("logins.json", "r", encoding="utf-8") as arquivo:
                        usuarios = json.load(arquivo)
                    for i in usuarios:
                        if nomeDeUserEditar == i["nome"]:
                            for i in range(len(usuarios)):
                                if usuarios[i]["nome"] == nomeDeUserEditar:
                                    exCliete = i
                    excluir = 1
                    if excluir == 1:
                        usuarios.pop(exCliete)
                        with open("logins.json", "w",encoding="utf-8") as arquivo:
                            json.dump(usuarios, arquivo,indent=4,ensure_ascii=False)
                        print("\033[1mUser excluido!\033[0m")
                    else:
                        print("User Não encontrado!")
                        return perfil()
            elif editarConta == 4:
                pass
menu()