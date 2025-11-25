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
if not os.path.exists("vendas.json"):
    with open("vendas.json", "w", encoding="utf-8") as vendas_json:
        json.dump([], vendas_json, indent=4, ensure_ascii=False)
if not os.path.exists("logins.json"):
    with open("logins.json", "w",encoding="utf-8") as logins:
        json.dump(userPadrao, logins,indent=4,ensure_ascii=False)
def menurAlternativo():
    while True:
        os.system('cls')
        print("===========================MENU===========================")
        print("")
        print("Digite qual sua escolha!!")
        print("")
        print("0️⃣ -Cadastrar Comprar")
        print("1️⃣ -Lista de Produtos")
        print("2️⃣ -Editar Porodutos/User/Vendas")
        print("3️⃣ -Lista de User")
        print("4️⃣ -Lista de Vendas")
        print("5️⃣ -Sair")
        print("")
        entrada1 = int(input())
        if entrada1 == 0:
            valor = 0
            return cadastrar()
        if entrada1 == 1:
            return menurPrincipal()
        elif entrada1 == 2:
            return admin()
        elif entrada1 == 3:
            return perfil()
        elif entrada1 == 4:
            return listarVendas()
        elif entrada1 == 5:
            print("Finalizando...")
            tm.sleep(2)
            os.system('cls')
            return
        else:
            print("Número inválido!!")
            tm.sleep(2) 
def menurPrincipal():
        while True:
            os.system('cls')
            print("!MENU!")
            print("Produtos:")
            with open("produtos.json", "r",encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
            for i, item in enumerate(dados):
                nome = item["nome"]
                print(f"{i+1} - {nome}")
            print("1️⃣- Relatorio Produtos!!\n2️⃣- Voltar!!")
            escolha= int(input())
            if escolha == 1:
                os.system('cls')
                with open("produtos.json", "r",encoding="utf-8") as arquivo:
                    dados = json.load(arquivo)
                for i, item in enumerate(dados):
                    nome = item["nome"]
                    quantidade = item["quantidade"]
                    print(f"{i+1} - {nome}-{quantidade}")
                print("1️⃣- Voltar!!")
                votar = int(input())
                if votar == 1:
                   return menurAlternativo() 
                else:
                    print("Numero invalido!!")
            elif escolha == 2:
                return menurAlternativo()
            else:
                print("Número inválido!!")
                tm.sleep(2)
def admin():
    os.system("cls")
    print("1️⃣- Editar Produtos!!\n2️⃣- Editar Clientes!!\n3️⃣- Editar Vendas \n4️⃣- Voltar!!")
    adminEditar = int(input())
    if adminEditar ==  1:
        os.system("cls")
        print("1️⃣- Editar Produtos!!")
        print("2️⃣- Excluir Produtos!!")
        print("3️⃣- Adicionar Produtos!!\n4️⃣- Voltar!!")
        with open("produtos.json", "r",encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
        while True:
            try:
                ed_ou_ex_DeProdutos = int(input())
                if ed_ou_ex_DeProdutos >0:
                    break
                else:
                    print("Opção invalida!")
                    continue
            except ValueError:
                print("❌ Você digitou algo que não é número! Tente novamente.\n")
        if ed_ou_ex_DeProdutos == 1:
            print("Produtos:")
            with open("produtos.json", "r",encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
            for i, item in enumerate(dados):
                nome = item["nome"]
                print(f"{i+1} - {nome}")
            print("Digite o numero do produto para Editar!")
            while True:
                try:
                    produto = int(input())
                    if produto >0:
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
                    if nomeEditar > 1:
                        novoNome = input("Digite o novo nome: ")
                        break
                    if nomeEditar >0:
                        break
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
                        if quantidadeEditar > 0:
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
                    tm.sleep(5)
            return admin()
        elif ed_ou_ex_DeProdutos == 2:
            os.system("cls")
            with open("produtos.json", "r",encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
            print("Produtos cadastrados:")
            for i, item in enumerate(dados):
                nome = item["nome"]
                print(f"{i+1} - {nome}")
            print("Digite o numero do produto para excluir!")
            produto = int(input())
            with open("produtos.json", "r",encoding="utf-8") as produtos_json:
                produtos = json.load(produtos_json)
            if produto == 1:
                produtos.pop(0)
                with open("produtos.json", "w",encoding="utf-8") as arquivo:
                    json.dump(produtos, arquivo,indent=4,ensure_ascii=False)
                print("produto excluido!")
                if produto == 2:
                    produtos.pop(1)
                    with open("produtos.json", "w",encoding="utf-8") as arquivo:
                        json.dump(produtos, arquivo,indent=4,ensure_ascii=False)
                    print("produto excluido!")
                elif produto == 3:
                    produtos.pop(2)
                    with open("produtos.json", "w",encoding="utf-8") as arquivo:
                        json.dump(produtos, arquivo,indent=4,ensure_ascii=False)
                    print("produto excluido!")
                elif produto == 4:
                    produtos.pop(3)
                    with open("produtos.json", "w",encoding="utf-8") as arquivo:
                        json.dump(produtos, arquivo,indent=4,ensure_ascii=False)
                    print("produto excluido!")
                elif produto == 5:
                    produtos.pop(4)
                    with open("produtos.json", "w",encoding="utf-8") as arquivo:
                        json.dump(produtos, arquivo,indent=4,ensure_ascii=False)
                    print("produto excluido!")
                elif produto == 6:
                    produtos.pop(5)
                    with open("produtos.json", "w",encoding="utf-8") as arquivo:
                        json.dump(produtos, arquivo,indent=4,ensure_ascii=False)
                    print("produto excluido!")
                elif produto == 7:
                    produtos.pop(6)
                    with open("produtos.json", "w",encoding="utf-8") as arquivo:
                        json.dump(produtos, arquivo,indent=4,ensure_ascii=False)
                    print("produto excluido!")
                elif produto == 8:
                    produtos.pop(7)
                    with open("produtos.json", "w",encoding="utf-8") as arquivo:
                        json.dump(produtos, arquivo,indent=4,ensure_ascii=False)
                    print("produto excluido!")
                elif produto == 9:
                    produtos.pop(8)
                    with open("produtos.json", "w",encoding="utf-8") as arquivo:
                        json.dump(produtos, arquivo,indent=4,ensure_ascii=False)
                    print("produto excluido!")
                elif produto == 10:
                    produtos.pop(9) 
                    with open("produtos.json", "w",encoding="utf-8") as arquivo:
                        json.dump(produtos, arquivo,indent=4,ensure_ascii=False)
                    print("produto excluido!")
        elif ed_ou_ex_DeProdutos == 5:
            print("1")
            return admin()
        elif ed_ou_ex_DeProdutos == 3 and len(dados) <10:
            nomeDoProduto = input("Qual o nome do Produto? ") 
            quantidadeDeProduto = int(input("Tem que ser mais de 10. Quantas Unidades? "))
            precoDoProduto = float(input("Qual o preço do produto? "))
            if quantidadeDeProduto >=10:
                novoProduto = {
                    "nome": nomeDoProduto.strip().lower(),
                    "quantidade": quantidadeDeProduto,
                    "preco": precoDoProduto
                }
                produtos.append(novoProduto)
                with open("produtos.json", "w",encoding="utf-8") as arquivo:
                    json.dump(produtos, arquivo,indent=4,ensure_ascii=False)
                print("Produto Registrado!!")
        else:
            print("\033[1m!!A lista de produtos ja tem 10 itens!!\033[0m")
            tm.sleep(2)
            return admin()
    elif adminEditar == 2:
        os.system("cls")
        with open("logins.json", "r", encoding="utf-8") as arquivo:
            usuarios = json.load(arquivo)
        print("lista de usuarios registrada:")
        for i, item in enumerate(usuarios):
            nome = item["nome"]
            print(f"{i+1} - {nome}")
        print("Digite o numero do Clientes:")
        cliente = int(input())
        for i in usuarios:
            if cliente == i["nome"]:
                print("\033[1mUSER ENCONTRADO\033[0m")
                for i in range(len(usuarios)):
                    if usuarios[i]["nome"] == cliente:
                        exCliete = i
        print("1️⃣- Editar user!!\n2️⃣- Editar Senha!!\n3️⃣- Excluir User!!\n4️⃣- Voltar!!")
        while True:
            try:
                editarConta = int(input("Digite um número: "))
                if editarConta >0 and editarConta <5:
                    break
            except ValueError:
                print("❌ Você digitou algo que não é número! Tente novamente.\n")
        if editarConta == 1:
            if True:
                novoNome = input("Digite o novo nome: ")
            os.system("cls")
            with open("logins.json", "r", encoding="utf-8") as arquivo:
                usuarios = json.load(arquivo)
            for i in usuarios:
                if cliente == i["nome"]:
                    for i in range(len(usuarios)):
                        if usuarios[i]["nome"] == cliente:
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
                        digite = input("Digite a senha atual: ")
                        for u in usuarios:
                            if digite == u["senha"]:
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
                    if digite == i["senha"]:
                        for i in range(len(usuarios)):
                            if usuarios[i]["senha"] == digite:
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
                    if certeza == 1:
                        break
                except ValueError:
                    print("❌ Você digitou algo que não é número! Tente novamente.\n")
            os.system("cls")
            if certeza == 1:
                with open("logins.json", "r", encoding="utf-8") as arquivo:
                    usuarios = json.load(arquivo)
                if True:
                    usuarios.pop(cliente-1)
                    with open("logins.json", "w",encoding="utf-8") as arquivo:
                        json.dump(usuarios, arquivo,indent=4,ensure_ascii=False)
                    print("\033[1mUser excluido!\033[0m")
                else:
                    print("User Não encontrado!")
                    return perfil()
        elif editarConta == 4:
            return menurAlternativo()
    elif adminEditar == 3:
        print("1️⃣- Editar Vendas!!\n2️⃣- Excluir Vendas!!\n3️⃣- Voltar!!")
        venda = int(input())
        if venda == 1:
            return editarVenda()
        elif venda == 2:
            excluirVenda()
        else:
            return menurAlternativo()
    else:
        return menurAlternativo()
def cadastrar():
    os.system('cls')
    print("========================CADASTRAR========================")
    with open("logins.json", "r", encoding="utf-8") as arquivo:
        usuarios = json.load(arquivo)
    nomeNovo = input("Nome do Cliente: ").strip().lower()
    print("OBS: digite apenas os numeros do CPF!!")
    cpf = input("CPF: ").strip().lower()
    contadorCPF = 0
    for i in cpf:
        contadorCPF += 1
    idade = int(input("Idade: ").lower().strip())
    while idade <3 or idade>150:
        print("Idade invalida!!")
        idade = int(input("Idade: "))
        if idade >3 and idade<150:
            break
    if idade > 18 and contadorCPF == 11:
        novoUsuario = {
            "nome": nomeNovo.strip().lower(),
            "idade": idade,
            "cpf": cpf
        }
        usuarios.append(novoUsuario)
        with open("logins.json", "w",encoding="utf-8") as arquivo:
            json.dump(usuarios, arquivo,indent=4,ensure_ascii=False)
    def produtos():
        global valor
        os.system("cls")

        # carrega os produtos
        with open("produtos.json", "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

        # mostra produtos
        print("Produtos:")
        for i, item in enumerate(dados):
            print(f"{i+1} - {item['nome']} (R$ {item['preco']})")

        escolha = int(input("Escolha o produto: ")) - 1

        # produto escolhido
        produto = dados[escolha]

        nome = produto["nome"]
        preco = produto["preco"]
        estoque = produto["quantidade"]

        if estoque <= 0:
            print("⚠️ Produto fora de estoque!")
            tm.sleep(2)
            return menurAlternativo()

        qtd = int(input(f"{nome} tem {estoque} unidades. Comprar quantas? "))

        if qtd > estoque:
            print("❌ Não há unidades suficientes!")
            tm.sleep(2)
            return menurAlternativo()

        # atualiza estoque
        produto["quantidade"] = estoque - qtd

        with open("produtos.json", "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)

        # registra venda
        valor += qtd * preco
        with open("vendas.json", "r", encoding="utf-8") as arquivo:
            vendas = json.load(arquivo)

        vendas.append({
            "produto": nome,
            "quantidade": qtd,
            "valor_unitario": preco,
            "valor_total": qtd * preco
        })

        with open("vendas.json", "w", encoding="utf-8") as arquivo:
            json.dump(vendas, arquivo, indent=4, ensure_ascii=False)

        print(f"✔ Compra registrada! Valor parcial: R$ {valor}")
        print("1️⃣ Finalizar compra")
        print("2️⃣ Continuar comprando")

        r = int(input())
        if r == 1:
            print("Finalizando compra...")
            tm.sleep(3)
            return menurAlternativo()
        else:
            return produtos()
    produtos()
def listarVendas():
    os.system("cls")
    with open("vendas.json", "r", encoding="utf-8") as arquivo:
        vendas = json.load(arquivo)
    print("===== LISTA DE VENDAS =====")
    if not vendas:
        print("Nenhuma venda registrada.\n")
        input("Pressione ENTER...")
        return menurAlternativo()
    for i, v in enumerate(vendas):
        print(f"{i+1} - {v['produto']} | {v['quantidade']} unidades | "
              f"R$ {v['valor_unitario']} cada | Total: R$ {v['valor_total']}")
    print("\n==============================")
    print("1️⃣- Relatorio Vendas!!\n2️⃣- Voltar!!")
    voltar2 = int(input())
    if voltar2 == 1:
        os.system("cls")
        with open("vendas.json", "r", encoding="utf-8") as arquivo:
            vendas = json.load(arquivo)
        total = 0
        for venda in vendas:
            total = total + venda["valor_total"]
        print("===== RELATÓRIO DE VENDAS =====")
        print("Valor total vendido: R$", total)
        print("================================")
        input("Pressione ENTER para voltar...")
        return menurAlternativo()
    else:
        return menurAlternativo()
def perfil():
    with open("logins.json", "r", encoding="utf-8") as arquivo:
        usuarios = json.load(arquivo)
    os.system("cls")
    print("!MENU!")
    print("Usuarios:")
    for i, item in enumerate(usuarios):
        nome = item["nome"]
        print(f"{i+1} - {nome}")
    escolha= int(input("Digite 0 para voltar para o MENU!!: "))
    if escolha == 0:
        return menurAlternativo()
def editarVenda():
    os.system("cls")
    with open("vendas.json", "r", encoding="utf-8") as arquivo:
        vendas = json.load(arquivo)
    listarVendas()
    if not vendas:
        print("Sem vendas registradas!")
        tm.sleep(2)
        return menurAlternativo()
    indice = int(input("Digite o número da venda para editar: ")) 
    indice = indice - 1
    if indice < 0 or indice >= len(vendas):
        print("Venda inválida!")
        tm.sleep(1.5)
        return editarVenda()
    novaQTD = int(input("Nova quantidade: "))
    if novaQTD <= 0:
        print("Quantidade inválida!")
        return editarVenda()
    vendas[indice]["quantidade"] = novaQTD
    vendas[indice]["valor_total"] = novaQTD * vendas[indice]["valor_unitario"]
    with open("vendas.json", "w", encoding="utf-8") as arquivo:
        json.dump(vendas, arquivo, indent=4, ensure_ascii=False)
    print("✔ Venda atualizada!")
    tm.sleep(1.5)
    return menurAlternativo()
def excluirVenda():
    os.system("cls")
    with open("vendas.json", "r", encoding="utf-8") as arquivo:
        vendas = json.load(arquivo)
    listarVendas()
    if not vendas:
        return menurAlternativo()
    indice = int(input("Digite o número da venda para excluir: ")) - 1
    if indice < 0 or indice >= len(vendas):
        print("Venda inválida!")
        tm.sleep(1.5)
        return  menurAlternativo()
    vendas.pop(indice)
    with open("vendas.json", "w", encoding="utf-8") as arquivo:
        json.dump(vendas, arquivo, indent=4, ensure_ascii=False)
    print("✔ Venda excluída!")
    tm.sleep(1.5)
    return menurAlternativo()
menurAlternativo()  