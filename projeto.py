import os
import json
import time as tm
valor = 0
produtos = [
    {
        "feijao": 10
    },
    {
        "arroz": 10
    },
    {
        "macarrao": 10
    },
    {
        "peitodefrango": 10
    },
    {
        "detegente": 10
    },
    {
        "aguasanitaria": 10
    },
    {
        "sabaoempo": 10
    },
    {
        "desinfetante": 10
    },
    {
        "papel": 10
    },
    {
        "pastadedente": 10
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
    with open("produtos.json", "w") as produtos_json:
        json.dump(produtos, produtos_json, indent=4)
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
            print("Digite 4 para voltar para o MENU!!")
            print("1️⃣- Itens de Alimenticios")
            print("2️⃣- Itens de Limpeza")
            print("3️⃣- Itens de Igiene Pessoal")
            print("")
            escolha= int(input("Digite o número do Produto: "))
            if escolha == 1413914:
                return admin()
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
                        quantoUnidades = int(input(f"Feijão tem {feijao} unidades. Quantas unidades quer? "))
                        if quantoUnidades > feijao:
                            print("❌ Não há unidades suficientes em estoque.")
                            tm.sleep(2)
                            return menurPrincipal()
                        dados[0]["feijao"] = feijao - quantoUnidades
                        with open("produtos.json", "w") as arquivo:
                            json.dump(dados, arquivo, indent=4)
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
                    if itensAlimenticios == 2:
                        with open("produtos.json", "r") as arquivo:
                            dados = json.load(arquivo)
                        arroz = dados[1].get("arroz", 0)
                        if arroz <= 0:
                            print("⚠️ Arroz fora de estoque!")
                            tm.sleep(2)
                            return menurPrincipal()
                        quantoUnidades = int(input(f"Arroz tem {arroz} unidades. Quantas unidades quer? "))
                        if quantoUnidades > arroz:
                            print("❌ Não há unidades suficientes.")
                            tm.sleep(2)
                            return menurPrincipal()
                        dados[1]["arroz"] = arroz - quantoUnidades
                        with open("produtos.json", "w") as arquivo:
                            json.dump(dados, arquivo,indent=4)
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
                    if itensAlimenticios == 3:
                        with open("produtos.json", "r") as arquivo:
                            dados = json.load(arquivo)
                        macarrao = dados[2].get("macarrao", 0)
                        if macarrao <= 0:
                            print("⚠️ macarrao fora de estoque!")
                            tm.sleep(2)
                            return menurPrincipal()
                        quantoUnidades = int(input(f"Macarrão tem {macarrao} unidades. Quantas unidades quer? "))
                        if quantoUnidades > macarrao:
                            print("❌ Não há unidades suficientes.")
                            tm.sleep(2)
                            return menurPrincipal()
                        dados[2]["macarrao"] = macarrao - quantoUnidades
                        with open("produtos.json", "w") as arquivo:
                            json.dump(dados, arquivo,indent=4)
                        print("1️⃣- Confimar Compra!!")
                        print("2️⃣- Para continuar comprando")
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
                    if itensAlimenticios == 4:
                        with open("produtos.json", "r") as arquivo:
                            dados = json.load(arquivo)
                        peitodefrango = dados[3].get("peitodefrango", 0)
                        if peitodefrango <= 0:
                            print("⚠️ Peito de Frango fora de estoque!")
                            tm.sleep(2)
                            return menurPrincipal()
                        quantoUnidades = int(input(f"Peito de Frango tem {peitodefrango} unidades. Quantas unidades quer? "))
                        if quantoUnidades > peitodefrango:
                            print("❌ Não há unidades suficientes.")
                            tm.sleep(2)
                            return menurPrincipal()
                        dados[3]["peitodefrango"] = peitodefrango - quantoUnidades
                        with open("produtos.json", "w") as arquivo:
                            json.dump(dados, arquivo,indent=4)
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
                    if itensAlimenticios == 5:
                        return menurPrincipal()
            elif escolha == 2:
                    os.system('cls')
                    print("5️⃣- Voltar!")
                    print("6️⃣- Confirma comprar!")
                    print("==============Itens De Limpeza==============")
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
                        detegente = dados[4].get("detegente", 0)
                        if detegente <= 0:
                            print("⚠️ Feijão fora de estoque!")
                            tm.sleep(2)
                            return menurPrincipal()
                        quantoUnidades = int(input(f"Feijão tem {detegente} unidades. Quantas unidades quer? "))
                        if quantoUnidades > detegente:
                            print("❌ Não há unidades suficientes em estoque.")
                            tm.sleep(2)
                            return menurPrincipal()
                        dados[4]["detegente"] = detegente - quantoUnidades
                        with open("produtos.json", "w") as arquivo:
                            json.dump(dados, arquivo,indent=4)
                        print("1️⃣- Confimar Compra!!")
                        print("2️⃣- Continuar comprando")
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
                    if itensDeLimpeza == 2:
                        with open("produtos.json", "r") as arquivo:
                            dados = json.load(arquivo)
                        aguasanitaria = dados[5].get("aguasanitaria", 0)
                        if aguasanitaria <= 0:
                            print("⚠️ Feijão fora de estoque!")
                            tm.sleep(2)
                            return menurPrincipal()
                        quantoUnidades = int(input(f"Feijão tem {aguasanitaria} unidades. Quantas unidades quer? "))
                        if quantoUnidades > aguasanitaria:
                            print("❌ Não há unidades suficientes em estoque.")
                            tm.sleep(2)
                            return menurPrincipal()
                        dados[5]["aguasanitaria"] = aguasanitaria - quantoUnidades
                        with open("produtos.json", "w") as arquivo:
                            json.dump(dados, arquivo,indent=4)
                        print("1️⃣- Confimar Compra!!")
                        print("2️⃣- Continuar comprando")
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
                    if itensDeLimpeza == 3:
                        with open("produtos.json", "r") as arquivo:
                            dados = json.load(arquivo)
                        sabaoempo = dados[6].get("sabaoempo", 0)
                        if sabaoempo <= 0:
                            print("⚠️ Feijão fora de estoque!")
                            tm.sleep(2)
                            return menurPrincipal()
                        quantoUnidades = int(input(f"Feijão tem {sabaoempo} unidades. Quantas unidades quer? "))
                        if quantoUnidades > sabaoempo:
                            print("❌ Não há unidades suficientes em estoque.")
                            tm.sleep(2)
                            return menurPrincipal()
                        dados[6]["sabaoempo"] = sabaoempo - quantoUnidades
                        with open("produtos.json", "w") as arquivo:
                            json.dump(dados, arquivo,indent=4)
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
                    if itensDeLimpeza == 4:
                        with open("produtos.json", "r") as arquivo:
                            dados = json.load(arquivo)
                        desinfetante = dados[7].get("desinfetante", 0)
                        if desinfetante <= 0:
                            print("⚠️ Feijão fora de estoque!")
                            tm.sleep(2)
                            return menurPrincipal()
                        quantoUnidades = int(input(f"Feijão tem {desinfetante} unidades. Quantas unidades quer? "))
                        if quantoUnidades > desinfetante:
                            print("❌ Não há unidades suficientes em estoque.")
                            tm.sleep(2)
                            return menurPrincipal()
                        dados[7]["desinfetante"] = desinfetante - quantoUnidades
                        with open("produtos.json", "w") as arquivo:
                            json.dump(dados, arquivo,indent=4)
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
            elif escolha == 3:
                    os.system('cls')
                    print("5️⃣- Voltar!")
                    print("6️⃣- Confirma comprar!")
                    print("==============Itens De Igiene Pessoal==============")
                    print("1️⃣- Papel = R$ 10,00")
                    valorPapel = 10
                    print("2️⃣- Pasta de Dente = R$ 8,00")
                    valorPastaDeDente = 8
                    itensDeIgienePessoal = int(input("Digite O número do Produto: "))
                    if itensDeIgienePessoal == 1:
                        with open("produtos.json", "r") as arquivo:
                            dados = json.load(arquivo)
                        papel = dados[8].get("papel", 0)
                        if papel <= 0:
                            print("⚠️ Feijão fora de estoque!")
                            tm.sleep(2)
                            return menurPrincipal()
                        quantoUnidades = int(input(f"Feijão tem {papel} unidades. Quantas unidades quer? "))
                        if quantoUnidades > papel:
                            print("❌ Não há unidades suficientes em estoque.")
                            tm.sleep(2)
                            return menurPrincipal()
                        dados[8]["papel"] = papel - quantoUnidades
                        with open("produtos.json", "w") as arquivo:
                            json.dump(dados, arquivo,indent=4)
                        print("1️⃣- Confimar Compra!!")
                        print("2️⃣- Continuar comprando")
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
                    if itensDeIgienePessoal == 2:
                        with open("produtos.json", "r") as arquivo:
                            dados = json.load(arquivo)
                        pastadedente = dados[9].get("pastadedente", 0)
                        if pastadedente <= 0:
                            print("⚠️ Feijão fora de estoque!")
                            tm.sleep(2)
                            return menurPrincipal()
                        quantoUnidades = int(input(f"Feijão tem {pastadedente} unidades. Quantas unidades quer? "))
                        if quantoUnidades > pastadedente:
                            print("❌ Não há unidades suficientes em estoque.")
                            tm.sleep(2)
                            return menurPrincipal()
                        dados[9]["pastadedente"] = pastadedente - quantoUnidades
                        with open("produtos.json", "w") as arquivo:
                            json.dump(dados, arquivo,indent=4)
                        print("1️⃣- Confimar Compra!!")
                        print("2️⃣- Continuar comprando")
                        voltar = int(input())
                        if voltar == 1:
                            valor += valorPastaDeDente*quantoUnidades
                            print(f"Comprar no Valor: {valor}R$")
                            print("Finalizando Comprar...")
                            tm.sleep(10)
                            return menurPrincipal()
                        if voltar == 2:
                            valor += valorPastaDeDente*quantoUnidades
            elif escolha == 4:
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
        ed_ou_ex_DeProdutos = int(input(": "))
        if ed_ou_ex_DeProdutos == 1:
            with open("produtos.json", "r") as produtos_json:
                produtos = json.load(produtos_json)
                produtos1 = produtos[0]
                produtos2 = produtos[1]
                produtos3 = produtos[2]
            print(produtos)
        elif ed_ou_ex_DeProdutos == 2:
            os.system("cls")
            with open("produtos.json", "r") as arquivo:
                dados = json.load(arquivo)
            print("Produtos cadastrados:")
            for i, item in enumerate(dados):
                nome = list(item.keys())[0]
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
nomeDeUserEditar = ""
senhaDeUserEditar = ""
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
            print("1️⃣- Editar user!!\n2️⃣- Editar Senha!!\n3️⃣- Excluir User!!")
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
menu()