from conexaobd import connect
from bd import *
from datetime import datetime

conbd = connect()

Carrinho = []
Total = 0.00
clienteNovo = True

while True:
    print("=" * 50)
    opc = input("Bem-vindo! Oque deseja fazer? \n"
                "[1] Fazer Pedido \n"
                "[2] Banco de dados \n"
                "[3] Finalizar \n"
                "--> ")
    if opc == "3":
        print("Encerrando..")
        break
    # ============================================================= PEDIDO
    elif opc == "1":
            while True:
                if clienteNovo:
                    print("=" * 50)
                    opcliente = input("Você é um novo cliente? Deseja se cadastra-se? \n"
                                    "[1] Sim \n"
                                    "[2] Não \n"
                                    "--> ")
                    if opcliente == "2":
                        clienteNovo = False
                        break
                    elif opcliente == "1":
                        print("="*10,"Digite a seguir: Ex [João],[Silva],[Rua Palmeiras, 000],[São Paulo],[00000-000]","="*10)
                        cadastrarClientes(conbd,
                                        nome=input("Nome: "),
                                        sobrenome=input("Sobrenome: "),
                                        endereco=input("Endereço: "),
                                        cidade=input("Cidade: "),
                                        codigo=input("Código Postal: "))
                        clienteNovo = False
                        break
                    else:
                        print("Valor inválido, tente novamente.")
                        continue
            while True:
                print("=" * 50)
                oplistar = input("Selecione oque deseja fazer a seguir: \n"
                                "[1] Comprar produto \n"
                                "[2] Descrição dos produtos \n"
                                "[3] Categoria dos produtos \n"
                                "[4] Carrinho \n"
                                "[5] Voltar \n"
                                "--> ")
                if oplistar == "5":
                    break
                elif oplistar == "1": # ======================== COMPRA
                    while True:
                        listarProdutosPedido(conbd)
                        print("=" * 50)
                        vavpedido = input("Digite o [Nome] do produto que deseja comprar: ")
                        if vavpedido in VerificaProdu(conbd):
                            # ===========================================================
                            PediCarrinho(conbd, compra=vavpedido)
                            Carrinho.append(vavpedido)
                            Total += float(Preco(conbd, nome=vavpedido))
                            # ===========================================================
                            print("="*50)
                            opcomp = input("Deseja comprar novamente? \n"
                                            "[1] Sim \n"
                                            "[2] Não \n"
                                            "--> ")
                            if opcomp == "2":
                                break
                            elif opcomp == "1":
                                VerificaProdu(conbd)
                                continue
                            else:
                                print("Valor inválido, tente novamente.")
                        else:
                            print("=" * 50)
                            print("Produto não encontrado, tente novamente.")
                            print("=" * 50)
                            continue
                elif oplistar == "2": # ======================== DESCRIÇÃO
                    listarPedidosDescricao(conbd)
                elif oplistar == "3": # ======================== CATEGORIA
                    listarPedidosCategoria(conbd)
                elif oplistar == "4": # CARRINHO DO PEDIDO =====================================
                    while True:
                        print("="*20,"CARRINHO","="*20)
                        quantia = {}
                        for produ in Carrinho:
                            if produ in quantia:
                                quantia[produ]["quantidade"] += 1
                                quantia[produ]["precototal"] += Preco(conbd,nome=produ)
                            else:
                                quantia[produ] = {
                                    "quantidade": 1,
                                    "precototal": Preco(conbd,nome=produ)
                                    }
                        for pr, info in quantia.items():
                            print(f"{pr}: R${info['precototal']} [{info['quantidade']}x]")
                        # --------------------------------------------------------------------------
                        print("-"*50)
                        print("Total: R$",round(Total, 2), sep="")                    
                        print("=" * 50)
                        opcar = input("Digite oq deseja fazer a seguir?: \n"
                                    "[1] Finalizar pedido \n"
                                    "[2] Remover um produto da lista \n"
                                    "[3] Voltar \n"
                                    "--> ")
                        if opcar == "3":
                            break

                        elif opcar == "1": # FINALIZAR O PEDIDO =========================================
                            if Carrinho:
                                print("=" * 50)
                                datahj = datetime.now().strftime("%y-%m-%d")
                                lobos = verificaNome(conbd, tabela='produtos')
                                Pedido(conbd, data=datahj, toto=float(Total)) # FUNÇÃO PEDIDO

                                for di, qua in quantia.items(): # Loop da FUNÇÃO DETALHES PEDIDO
                                    if di in lobos:
                                        detalhesPedi(conbd,
                                                     IDprodu=Ovelhas(conbd,nome=di),
                                                     quanti=qua['quantidade']
                                                     )

                                # RESET -------------
                                Total = 0.00
                                Carrinho = []
                                quantia = {}
                                # -------------------
                                break
                            else:
                                print("="*50)
                                print("O CARRINHO está VAZIO! Não há compras para ser finalizadas.")

                        elif opcar == "2": # REMOVER DA LISTA CARRINHO ==================================
                            while True:
                                print("=" * 50)
                                reop = input("Digite o [NOME] do produto que deseja REMOVER do carrinho \n"
                                            "Digite [x] para cancelar: \n"
                                            "--> ")
                                if reop == "x":
                                    break
                                elif reop in Carrinho:
                                    print("=" * 50)
                                    Carrinho.remove(reop)
                                    Total -= float(Preco(conbd, nome=reop))
                                    print(reop, "Foi removido do carrinho.")
                                    break
                                else:
                                    print("Produto não encontrado, tente novamente.")
                                    continue
                        else:
                            print("Valor inválido, tente novamente.")
                else:
                    print("Valor inválido, tente novamente.")

    # ============================================================= BANCO DE DADOS
    elif opc == "2":
        while True:
            print("=" * 50)
            opcbc = input("Bem-vindo ao banco de dados! Selecione oque deseja fazer? \n"
                        "[1] Cadastrar \n"
                        "[2] Alterar \n"
                        "[3] Deletar \n"
                        "[4] Listar \n"
                        "[5] Voltar \n"
                        "--> ")

            if opcbc == "5":
                break
            elif opcbc == "1":  # ============================================================= CADASTRO
                while True:
                    print("=" * 50)
                    opcadastro = input("Qual tabela deseja CADASTRAR novos valores? \n"
                                    "[1] Produtos \n"
                                    "[2] Clientes \n"
                                    "[3] Fornecedores \n"
                                    "[4] Funcionarios \n"
                                    "[5] Promocoes \n"
                                    "[6] Voltar \n"
                                    "--> ")
                    if opcadastro == "6":
                        break


                    elif opcadastro == "1":

                        print("=" * 20, "CADASTRANDO PRODUTOS", "=" * 20)

                        while True:
                            opcate = input("Deseja cadastrar o novo produto a uma CATEGORIA? [1] para Sim e [2] para NÃO \n"
                                        "--> ")

                            if opcate == "2": # ====== SEM CATEGORIA

                                print("="*50)

                                while True:
                                    opcate = input(
                                        "Deseja cadastrar o novo produto a um FORNECEDOR? [1] para Sim e [2] para NÃO \n"
                                        "--> ")

                                    if opcate == "2": # ====== SOMENTE PRODUTO

                                        cadastrarProdutos(conbd,
                                                        nome=input("Digite o nome: "),
                                                        descricao=input("Digite a descrição: "),
                                                        preco=input("Digite o preço: "),
                                                        quantidade=input("Digite a quantidade: "))

                                        break

                                    elif opcate == "1": # ====== COM FONECEDOR

                                        pnome = input("Digite o nome do produto: ")
                                        pdes = input("Digite a descrição do produto: ")
                                        ppreco = input("Digite o preço do produto: ")
                                        pquanti = input("Digite a quantidade em estoque: ")
                                        print("="*15,"FORNECEDOR","="*15)
                                        ffnome = input("Digite o nome do fornecedor: ")
                                        ffcontato = input("Digite o contato do fornecdor: ")
                                        ffende = input("Digite o endereçodo fornecedor: ")

                                        cadastrarProdutosF(conbd,
                                                        nome=pnome,
                                                        descricao=pdes,
                                                        preco=ppreco,
                                                        quantidade=pquanti,
                                                        fnome=ffnome,
                                                        fcontato=ffcontato,
                                                        fende=ffende)

                                        break
                                    else:
                                        print("Opção inválida")
                                    continue

                                break

                            elif opcate == "1": # ====== COM CATEGORIA

                                while True:
                                    opcate = input(
                                        "Deseja cadastrar o novo produto a um FORNECEDOR? [1] para Sim e [2] para NÃO \n"
                                        "--> ")

                                    if opcate == "2": # ====== PRODUTO COM CATEGORIA

                                        pnome = input("Digite o nome do produto: ")
                                        pdes = input("Digite a descrição do produto: ")
                                        ppreco = input("Digite o preço do produto: ")
                                        pquanti = input("Digite a quantidade em estoque: ")
                                        print("="*15,"CATEGORIA","="*15)
                                        ccnome = input("Digite a categoria do produto: ")
                                        ccdes = input("Digite a descrição da categoria: ")

                                        cadastrarProdutosC(conbd,
                                                        nome=pnome,
                                                        descricao=pdes,
                                                        preco=ppreco,
                                                        quantidade=pquanti,
                                                        cnome=ccnome,
                                                        cdes=ccdes)

                                        break

                                    elif opcate == "1": # ====== PRODUTO COM CATEGORIA E FORNECEDOR

                                        pnome = input("Digite o nome do produto: ")
                                        pdes = input("Digite a descrição do produto: ")
                                        ppreco = input("Digite o preço do produto: ")
                                        pquanti = input("Digite a quantidade em estoque: ")

                                        print("=" * 15, "FORNECEDOR", "=" * 15)
                                        ffnome = input("Digite o nome do fornecedor: ")
                                        ffcontato = input("Digite o contato do fornecdor: ")
                                        ffende = input("Digite o endereçodo fornecedor: ")

                                        print("=" * 15, "CATEGORIA", "=" * 15)
                                        ccnome = input("Digite a categoria do produto: ")
                                        ccdes = input("Digite a descrição da categoria: ")

                                        cadastrarProdutosCF(conbd,
                                                        nome=pnome,
                                                        descricao=pdes,
                                                        preco=ppreco,
                                                        quantidade=pquanti,
                                                        cnome=ccnome,
                                                        cdes=ccdes,
                                                        fnome=ffnome,
                                                        fcontato=ffcontato,
                                                        fende=ffende)

                                        break
                                    else:
                                        print("Opção inválida")
                                    continue

                                break
                            else:
                                print("Opção inválida")
                            continue

                    elif opcadastro == "2":
                        print("=" * 20, "CADASTRANDO CLIENTES", "=" * 20)
                        cadastrarClientes(conbd,
                                        nome=input("Digite o nome: "),
                                        sobrenome=input("Digite o sobrenome: "),
                                        endereco=input("Digite o endereço: "),
                                        cidade=input("Digite a cidade: "),
                                        codigo=input("Digite o código postal: "))
                    elif opcadastro == "3":
                        print("=" * 20, "CADASTRANDO FORNECEDORES", "=" * 20)
                        cadastrarFornecedores(conbd,
                                            nome=input("Digite o nome: "),
                                            contato=input("Digite o contato: "),
                                            endereco=input("Digite o endereço: "))
                    elif opcadastro == "4":
                        print("=" * 20, "CADASTRANDO FUNCIONARIOS", "=" * 20)
                        cadastrarFuncionarios(conbd,
                                            nome=input("Digite o nome: "),
                                            cargo=input("Digite o cargo: "),
                                            depart=input("Digite o departamento: "))
                    elif opcadastro == "5":
                        print("=" * 20, "CADASTRANDO PROMOCOES", "=" * 20)
                        cadastrarPromocoes(conbd,
                                        nome=input("Digite o nome: "),
                                        descricao=input("Digite a descrição: "),
                                        datai=input("Digite a data de inicio: "),
                                        dataf=input("Digite a data final: "))
                    else:
                        print("Errou!")
            elif opcbc == "2":  # =========================================================== ALTERAR
                while True:
                    print("=" * 50)
                    opalterar = input("Qual tabela deseja ALTERAR novos valores? \n"
                                    "[1] Produtos \n"
                                    "[2] Clientes \n"
                                    "[3] Fornecedores \n"
                                    "[4] Funcionarios \n"
                                    "[5] Promocoes \n"
                                    "[6] Voltar \n"
                                    "--> ")
                    if opalterar == "6":
                        break

                    elif opalterar == "1":

                        # =================================
                        tab = 'produtos'  # TABELA ESCOLHIDA
                        # =================================

                        if verifica(conbd, tabela=tab) != 0:  # Verifica se possui valores
                            while True:
                                print("=" * 50)
                                oplinha = input("São os IDs {} na tabela [{}], digite o ID que deseja alterar \n"
                                                "Ou digite [sair] para voltar \n"
                                                "--> "
                                                .format(verifica(conbd, tabela=tab), tab))
                                if oplinha != "sair":
                                    if oplinha.isnumeric():  # Verifica se o usuario digitou um número
                                        if int(oplinha) in verifica(conbd, tabela=tab,
                                                                    ):  # Verifica número digitado do usúsario
                                            print("=" * 50)
                                            print("Aqui está a lista das colunas dessa tabela: \n",
                                                verificaColums(conbd, table=tab))
                                            opcolum = input("Digite o nome da coluna que deseja alterar \n"
                                                            "--> ")
                                            if opcolum in verificaColums(conbd, table=tab):
                                                print("=" * 50)
                                                # ===================================
                                                atualizarProdutos(conbd,
                                                                coluna=opcolum,
                                                                new=input(f"Digite o novo valor de {opcolum}: "),
                                                                linha=int(oplinha))
                                                break
                                                # ===================================
                                            else:
                                                print("Essa coluna não existe.")
                                        else:
                                            print("Esse ID não existe, tente novamente.")
                                    else:
                                        print("O ID digitado está inválido, tente novamente.")
                                else:
                                    break
                        else:
                            print("Essa tabela não possui valores para serem alterados.")

                    elif opalterar == "2":

                        # =================================
                        tab = 'clientes'  # TABELA ESCOLHIDA
                        # =================================

                        if verifica(conbd, tabela=tab) != 0:  # Verifica se possui valores
                            while True:
                                print("=" * 50)
                                oplinha = input("São os IDs {} na tabela [{}], digite o ID que deseja alterar \n"
                                                "Ou digite [sair] para voltar \n"
                                                "--> "
                                                .format(verifica(conbd, tabela=tab), tab))
                                if oplinha != "sair":
                                    if oplinha.isnumeric():  # Verifica se o usuario digitou um número
                                        if int(oplinha) in verifica(conbd, tabela=tab,
                                                                    ):  # Verifica número digitado do usúsario
                                            print("=" * 50)
                                            print("Aqui está a lista das colunas dessa tabela: \n",
                                                verificaColums(conbd, table=tab))
                                            opcolum = input("Digite o nome da coluna que deseja alterar \n"
                                                            "--> ")
                                            if opcolum in verificaColums(conbd, table=tab):
                                                print("=" * 50)
                                                # ===================================
                                                atualizarClientes(conbd,
                                                                coluna=opcolum,
                                                                new=input(f"Digite o novo valor de {opcolum}: "),
                                                                linha=int(oplinha))
                                                break
                                                # ===================================
                                            else:
                                                print("Essa coluna não existe.")
                                        else:
                                            print("Esse ID não existe, tente novamente.")
                                    else:
                                        print("O ID digitado está inválido, tente novamente.")
                                else:
                                    break
                        else:
                            print("Essa tabela não possui valores para serem alterados.")

                    elif opalterar == "3":

                        # =================================
                        tab = 'fornecedores'  # TABELA ESCOLHIDA
                        # =================================

                        if verifica(conbd, tabela=tab) != 0:  # Verifica se possui valores
                            while True:
                                print("=" * 50)
                                oplinha = input("São os IDs {} na tabela [{}], digite o ID que deseja alterar \n"
                                                "Ou digite [sair] para voltar \n"
                                                "--> "
                                                .format(verifica(conbd, tabela=tab), tab))
                                if oplinha != "sair":
                                    if oplinha.isnumeric():  # Verifica se o usuario digitou um número
                                        if int(oplinha) in verifica(conbd, tabela=tab,
                                                                    ):  # Verifica número digitado do usúsario
                                            print("=" * 50)
                                            print("Aqui está a lista das colunas dessa tabela: \n",
                                                verificaColums(conbd, table=tab))
                                            opcolum = input("Digite o nome da coluna que deseja alterar \n"
                                                            "--> ")
                                            if opcolum in verificaColums(conbd, table=tab):
                                                print("=" * 50)
                                                # ===================================
                                                atualizarFornecedores(conbd,
                                                                    coluna=opcolum,
                                                                    new=input(f"Digite o novo valor de {opcolum}: "),
                                                                    linha=int(oplinha))
                                                break
                                                # ===================================
                                            else:
                                                print("Essa coluna não existe.")
                                        else:
                                            print("Esse ID não existe, tente novamente.")
                                    else:
                                        print("O ID digitado está inválido, tente novamente.")
                                else:
                                    break
                        else:
                            print("Essa tabela não possui valores para serem alterados.")

                    elif opalterar == "4":

                        # =================================
                        tab = 'funcionarios'  # TABELA ESCOLHIDA
                        # =================================

                        if verifica(conbd, tabela=tab) != 0:  # Verifica se possui valores
                            while True:
                                print("=" * 50)
                                oplinha = input("São os IDs {} na tabela [{}], digite o ID que deseja alterar \n"
                                                "Ou digite [sair] para voltar \n"
                                                "--> "
                                                .format(verifica(conbd, tabela=tab), tab))
                                if oplinha != "sair":
                                    if oplinha.isnumeric():  # Verifica se o usuario digitou um número
                                        if int(oplinha) in verifica(conbd, tabela=tab,
                                                                    ):  # Verifica número digitado do usúsario
                                            print("=" * 50)
                                            print("Aqui está a lista das colunas dessa tabela: \n",
                                                verificaColums(conbd, table=tab))
                                            opcolum = input("Digite o nome da coluna que deseja alterar \n"
                                                            "--> ")
                                            if opcolum in verificaColums(conbd, table=tab):
                                                print("=" * 50)
                                                # ===================================
                                                atualizarFuncionarios(conbd,
                                                                    coluna=opcolum,
                                                                    new=input(f"Digite o novo valor de {opcolum}: "),
                                                                    linha=int(oplinha))
                                                break
                                                # ===================================
                                            else:
                                                print("Essa coluna não existe.")
                                        else:
                                            print("Esse ID não existe, tente novamente.")
                                    else:
                                        print("O ID digitado está inválido, tente novamente.")
                                else:
                                    break
                        else:
                            print("Essa tabela não possui valores para serem alterados.")

                    elif opalterar == "5":

                        # =================================
                        tab = 'promocoes'  # TABELA ESCOLHIDA
                        # =================================

                        if verifica(conbd, tabela=tab) != 0:  # Verifica se possui valores
                            while True:
                                print("=" * 50)
                                oplinha = input("São os IDs {} na tabela [{}], digite o ID que deseja alterar \n"
                                                "Ou digite [sair] para voltar \n"
                                                "--> "
                                                .format(verifica(conbd, tabela=tab), tab))
                                if oplinha != "sair":
                                    if oplinha.isnumeric():  # Verifica se o usuario digitou um número
                                        if int(oplinha) in verifica(conbd, tabela=tab,
                                                                    ):  # Verifica número digitado do usúsario
                                            print("=" * 50)
                                            print("Aqui está a lista das colunas dessa tabela: \n",
                                                verificaColums(conbd, table=tab))
                                            opcolum = input("Digite o nome da coluna que deseja alterar \n"
                                                            "--> ")
                                            if opcolum in verificaColums(conbd, table=tab):
                                                print("=" * 50)
                                                # ===================================
                                                atualizarPromocoes(conbd,
                                                                coluna=opcolum,
                                                                new=input(f"Digite o novo valor de {opcolum}: "),
                                                                linha=int(oplinha))
                                                break
                                                # ===================================
                                            else:
                                                print("Essa coluna não existe.")
                                        else:
                                            print("Esse ID não existe, tente novamente.")
                                    else:
                                        print("O ID digitado está inválido, tente novamente.")
                                else:
                                    break
                        else:
                            print("Essa tabela não possui valores para serem alterados.")

                    else:
                        print("Valor inválido, tente novamente.")
            elif opcbc == "3":  # =================================================================== DELETAR
                while True:
                    print("=" * 50)
                    opdeletar = input("Qual tabela deseja DELETAR seus valores? \n"
                                    "[1] Produtos \n"
                                    "[2] Clientes \n"
                                    "[3] Fornecedores \n"
                                    "[4] Funcionarios \n"
                                    "[5] Promocoes \n"
                                    "[6] Voltar \n"
                                    "--> ")
                    if opdeletar == "6":
                        break
                    elif opdeletar == "1":

                        # ============================
                        tab = 'produtos'
                        # ============================

                        if verifica(conbd, tabela=tab) != 0:  # Verifica se possui valores
                            while True:
                                print("=" * 50)
                                oplinha = input("São os IDs {} na tabela [{}], digite o ID que deseja alterar \n"
                                                "Ou digite [sair] para voltar \n"
                                                "--> "
                                                .format(verifica(conbd, tabela=tab), tab))
                                if oplinha != "sair":
                                    if oplinha.isnumeric():  # Verifica se o usuario digitou um número
                                        if int(oplinha) in verifica(conbd, tabela=tab,
                                                                    ):  # Verifica número digitado do usúsario
                                            # ==================================
                                            print("=" * 50)
                                            deletarProdutos(conbd, linha=oplinha)
                                            break
                                            # ==================================
                                        else:
                                            print("Esse ID não existe, tente novamente.")
                                    else:
                                        print("O ID digitado está inválido, tente novamente.")
                                else:
                                    break
                        else:
                            print("Essa tabela não possui valores para serem alterados.")

                    elif opdeletar == "2":

                        # ============================
                        tab = 'clientes'
                        # ============================

                        if verifica(conbd, tabela=tab) != 0:  # Verifica se possui valores
                            while True:
                                print("=" * 50)
                                oplinha = input("São os IDs {} na tabela [{}], digite o ID que deseja alterar \n"
                                                "Ou digite [sair] para voltar \n"
                                                "--> "
                                                .format(verifica(conbd, tabela=tab), tab))
                                if oplinha != "sair":
                                    if oplinha.isnumeric():  # Verifica se o usuario digitou um número
                                        if int(oplinha) in verifica(conbd, tabela=tab,
                                                                    ):  # Verifica número digitado do usúsario
                                            # ==================================
                                            print("=" * 50)
                                            deletarClientes(conbd, linha=oplinha)
                                            break
                                            # ==================================
                                        else:
                                            print("Esse ID não existe, tente novamente.")
                                    else:
                                        print("O ID digitado está inválido, tente novamente.")
                                else:
                                    break
                        else:
                            print("Essa tabela não possui valores para serem alterados.")

                    elif opdeletar == "3":

                        # ============================
                        tab = 'fornecedores'
                        # ============================

                        if verifica(conbd, tabela=tab) != 0:  # Verifica se possui valores
                            while True:
                                print("=" * 50)
                                oplinha = input("São os IDs {} na tabela [{}], digite o ID que deseja alterar \n"
                                                "Ou digite [sair] para voltar \n"
                                                "--> "
                                                .format(verifica(conbd, tabela=tab), tab))
                                if oplinha != "sair":
                                    if oplinha.isnumeric():  # Verifica se o usuario digitou um número
                                        if int(oplinha) in verifica(conbd, tabela=tab,
                                                                    ):  # Verifica número digitado do usúsario
                                            # ==================================
                                            print("=" * 50)
                                            deletarFornecedores(conbd, linha=oplinha)
                                            break
                                            # ==================================
                                        else:
                                            print("Esse ID não existe, tente novamente.")
                                    else:
                                        print("O ID digitado está inválido, tente novamente.")
                                else:
                                    break
                        else:
                            print("Essa tabela não possui valores para serem alterados.")

                    elif opdeletar == "4":

                        # ============================
                        tab = 'funcionarios'
                        # ============================

                        if verifica(conbd, tabela=tab) != 0:  # Verifica se possui valores
                            while True:
                                print("=" * 50)
                                oplinha = input("São os IDs {} na tabela [{}], digite o ID que deseja alterar \n"
                                                "Ou digite [sair] para voltar \n"
                                                "--> "
                                                .format(verifica(conbd, tabela=tab), tab))
                                if oplinha != "sair":
                                    if oplinha.isnumeric():  # Verifica se o usuario digitou um número
                                        if int(oplinha) in verifica(conbd, tabela=tab,
                                                                   ):  # Verifica número digitado do usúsario
                                            # ==================================
                                            print("=" * 50)
                                            deletarFuncionarios(conbd, linha=oplinha)
                                            break
                                            # ==================================
                                        else:
                                            print("Esse ID não existe, tente novamente.")
                                    else:
                                        print("O ID digitado está inválido, tente novamente.")
                                else:
                                    break
                        else:
                            print("Essa tabela não possui valores para serem alterados.")

                    elif opdeletar == "5":

                        # ============================
                        tab = 'promocoes'
                        # ============================

                        if verifica(conbd, tabela=tab) != 0:  # Verifica se possui valores
                            while True:
                                print("=" * 50)
                                oplinha = input("São os IDs {} na tabela [{}], digite o ID que deseja alterar \n"
                                                "Ou digite [sair] para voltar \n"
                                                "--> "
                                                .format(verifica(conbd, tabela=tab), tab))
                                if oplinha != "sair":
                                    if oplinha.isnumeric():  # Verifica se o usuario digitou um número
                                        if int(oplinha) in verifica(conbd, tabela=tab,
                                                                    ):  # Verifica número digitado do usúsario
                                            # ==================================
                                            print("=" * 50)
                                            deletarPromocoes(conbd, linha=oplinha)
                                            break
                                            # ==================================
                                        else:
                                            print("Esse ID não existe, tente novamente.")
                                    else:
                                        print("O ID digitado está inválido, tente novamente.")
                                else:
                                    break
                        else:
                            print("Essa tabela não possui valores para serem alterados.")
            elif opcbc == "4":  # =================================================================== LISTAR
                while True:
                    print("=" * 50)
                    oplistar = input("Qual tabela deseja LISTAR sua tabela e valores? \n"
                                    "[1] Produtos \n"
                                    "[2] Clientes \n"
                                    "[3] Fornecedores \n"
                                    "[4] Funcionarios \n"
                                    "[5] Promocoes \n"
                                    "[6] Voltar \n"
                                    "--> ")
                    if oplistar == "6":
                        break
                    elif oplistar == "1":
                        tab = 'produtos'
                        print("=" * 50)
                        listar(conbd, table=tab)
                        break
                    elif oplistar == "2":
                        tab = 'clientes'
                        print("=" * 50)
                        listar(conbd, table=tab)
                        break
                    elif oplistar == "3":
                        tab = 'fornecedores'
                        print("=" * 50)
                        listar(conbd, table=tab)
                        break
                    elif oplistar == "4":
                        tab = 'funcionarios'
                        print("=" * 50)
                        listar(conbd, table=tab)
                        break
                    elif oplistar == "5":
                        tab = 'promocoes'
                        print("=" * 50)
                        listar(conbd, table=tab)
                        break
                    else:
                        print("Valor inválido, tente novamente")
            else:
                print("Valor inválido, tente novamente.")

    else:
        print("Valor inválido, tente novamente.")
