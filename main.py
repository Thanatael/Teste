from conexaobd import connect
from bd import *

conbd = connect()

Carrinho = []
Total = 0

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
    elif opc == "1":  # ============================================================= PEDIDO
        while True:
            print("=" * 15, "FAZENDO PEDIDO", "=" * 15)
            opcpedi = input("Olá cliente! Selecione oque deseja: \n"
                        "[1] Produtos \n"
                        "[2] Ofertas \n"
                        "[3] Carrinho \n"
                        "[4] Voltar \n"
                        "--> ")
            if opcpedi == "4":
                break
            elif opcpedi == "1":
                while True:
                    print("=" * 50)
                    oplistar = input("Selecione oque deseja fazer a seguir: \n"
                                    "[1] Comprar produto \n"
                                    "[2] Descrição do produto \n"
                                    "[3] Categoria do produto \n"
                                    "[4] Carrinho \n"
                                    "[5] Voltar \n"
                                    "--> ")
                    if oplistar == "5":
                        break
                    elif oplistar == "1":
                        while True:
                            listarProdutosPedido(conbd)
                            print("=" * 50)
                            vavpedido = input("Digite o [Nome] do produto que deseja comprar: ")
                            if vavpedido in VerificaProdu(conbd):
                                # ===========================================================
                                pedido(conbd, compra=vavpedido)
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
                    elif oplistar == "2":
                        listarPedidosDescricao(conbd)
                    elif oplistar == "3":
                        listarPedidosCategoria(conbd)
                    elif oplistar == "4":
                        print("="*20,"CARRINHO","="*20)
                        print("Produtos: ", Carrinho)
                        print("Total: R$",Total, sep="")
                        print("=" * 50)
                        input("Presione [ENTER] para continuar ")
                    else:
                        print("Valor inválido, tente novamente.")
# =====================================================================================================================                        
            elif opcpedi == "2":
                print("Ofertas")
            elif opcpedi == "3":
                print("="*20,"CARRINHO","="*20)
                print(Carrinho)
                print("=" * 50)
                input("Presione [ENTER] para continuar ")             
            else:
                print("Valor inválido, tente novamente.")

    elif opc == "2":  # ============================================================= BANCO DE DADOS
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
                            opcate = input("Deseja cadastrar o novo produto a uma categoria? [1] para Sim e [2] para NÃO \n"
                                        "--> ")

                            if opcate == "2":

                                print("="*20,"SEM CATEGORIA","="*20)

                                while True:
                                    opcate = input(
                                        "Deseja cadastrar o novo produto a um fornecedor? [1] para Sim e [2] para NÃO \n"
                                        "--> ")

                                    if opcate == "2":

                                        print("="*20,"SOMENTE PRODUTO","="*20)

                                        cadastrarProdutos(conbd,
                                                        nome=input("Digite o nome: "),
                                                        descricao=input("Digite a descrição: "),
                                                        preco=input("Digite o preço: "),
                                                        quantidade=input("Digite a quantidade: "))

                                        break

                                    elif opcate == "1":

                                        print("="*20,"COM FORNECEDOR","="*20)

                                        cadastrarProdutosF(conbd,
                                                        nome=input("Digite o nome: "),
                                                        descricao=input("Digite a descrição: "),
                                                        preco=input("Digite o preço: "),
                                                        quantidade=input("Digite a quantidade: "),
                                                        fnome=input("Digite o nome do fornecedor: "),
                                                        fcontato=input("Digite o contato: "),
                                                        fende=input("Digite o endereço: "))

                                        break
                                    else:
                                        print("Opção inválida")
                                    continue

                                break

                            elif opcate == "1":

                                print("="*20,"COM CATEGORIA","="*20)

                                while True:
                                    opcate = input(
                                        "Deseja cadastrar o novo produto a um fornecedor? [1] para Sim e [2] para NÃO \n"
                                        "--> ")

                                    if opcate == "2":

                                        print("="*20,"PRODUTO COM CATEGORIA","="*20)

                                        cadastrarProdutosC(conbd,
                                                        nome=input("Digite o nome: "),
                                                        descricao=input("Digite a descrição: "),
                                                        preco=input("Digite o preço: "),
                                                        quantidade=input("Digite a quantidade: "),
                                                        cnome=input("Digite a categoria: "),
                                                        cdes=input("Digite a descrição da categoria: "))

                                        break

                                    elif opcate == "1":

                                        print("="*10,"PRODUTO COM CATEGORIA E FORNECEDOR","="*10)

                                        cadastrarProdutosCF(conbd,
                                                        nome=input("Digite o nome: "),
                                                        descricao=input("Digite a descrição: "),
                                                        preco=input("Digite o preço: "),
                                                        quantidade=input("Digite a quantidade: "),
                                                        cnome=input("Digite a categoria: "),
                                                        cdes=input("Digite a descrição da categoria: "),
                                                        fnome=input("Digite o nome do fornecedor: "),
                                                        fcontato=input("Digite o contato: "),
                                                        fende=input("Digite o endereço: "))

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

                        if verifica(conbd, tabela=tab, veri=0) != 0:  # Verifica se possui valores
                            while True:
                                print("=" * 50)
                                oplinha = input("São os IDs {} na tabela [{}], digite o ID que deseja alterar \n"
                                                "Ou digite [sair] para voltar \n"
                                                "--> "
                                                .format(verifica(conbd, tabela=tab, veri=[]), tab))
                                if oplinha != "sair":
                                    if oplinha.isnumeric():  # Verifica se o usuario digitou um número
                                        if int(oplinha) in verifica(conbd, tabela=tab,
                                                                    veri=[]):  # Verifica número digitado do usúsario
                                            print("=" * 50)
                                            print("Aqui está a lista das colunas dessa tabela: \n",
                                                verificaColums(conbd, table=tab, colum=[]))
                                            opcolum = input("Digite o nome da coluna que deseja alterar \n"
                                                            "--> ")
                                            if opcolum in verificaColums(conbd, table=tab, colum=[]):
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

                        if verifica(conbd, tabela=tab, veri=0) != 0:  # Verifica se possui valores
                            while True:
                                print("=" * 50)
                                oplinha = input("São os IDs {} na tabela [{}], digite o ID que deseja alterar \n"
                                                "Ou digite [sair] para voltar \n"
                                                "--> "
                                                .format(verifica(conbd, tabela=tab, veri=0), tab))
                                if oplinha != "sair":
                                    if oplinha.isnumeric():  # Verifica se o usuario digitou um número
                                        if int(oplinha) in verifica(conbd, tabela=tab,
                                                                    veri=[]):  # Verifica número digitado do usúsario
                                            print("=" * 50)
                                            print("Aqui está a lista das colunas dessa tabela: \n",
                                                verificaColums(conbd, table=tab, colum=[]))
                                            opcolum = input("Digite o nome da coluna que deseja alterar \n"
                                                            "--> ")
                                            if opcolum in verificaColums(conbd, table=tab, colum=[]):
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

                        if verifica(conbd, tabela=tab, veri=0) != 0:  # Verifica se possui valores
                            while True:
                                print("=" * 50)
                                oplinha = input("São os IDs {} na tabela [{}], digite o ID que deseja alterar \n"
                                                "Ou digite [sair] para voltar \n"
                                                "--> "
                                                .format(verifica(conbd, tabela=tab, veri=0), tab))
                                if oplinha != "sair":
                                    if oplinha.isnumeric():  # Verifica se o usuario digitou um número
                                        if int(oplinha) in verifica(conbd, tabela=tab,
                                                                    veri=[]):  # Verifica número digitado do usúsario
                                            print("=" * 50)
                                            print("Aqui está a lista das colunas dessa tabela: \n",
                                                verificaColums(conbd, table=tab, colum=[]))
                                            opcolum = input("Digite o nome da coluna que deseja alterar \n"
                                                            "--> ")
                                            if opcolum in verificaColums(conbd, table=tab, colum=[]):
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

                        if verifica(conbd, tabela=tab, veri=0) != 0:  # Verifica se possui valores
                            while True:
                                print("=" * 50)
                                oplinha = input("São os IDs {} na tabela [{}], digite o ID que deseja alterar \n"
                                                "Ou digite [sair] para voltar \n"
                                                "--> "
                                                .format(verifica(conbd, tabela=tab, veri=0), tab))
                                if oplinha != "sair":
                                    if oplinha.isnumeric():  # Verifica se o usuario digitou um número
                                        if int(oplinha) in verifica(conbd, tabela=tab,
                                                                    veri=[]):  # Verifica número digitado do usúsario
                                            print("=" * 50)
                                            print("Aqui está a lista das colunas dessa tabela: \n",
                                                verificaColums(conbd, table=tab, colum=[]))
                                            opcolum = input("Digite o nome da coluna que deseja alterar \n"
                                                            "--> ")
                                            if opcolum in verificaColums(conbd, table=tab, colum=[]):
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

                        if verifica(conbd, tabela=tab, veri=0) != 0:  # Verifica se possui valores
                            while True:
                                print("=" * 50)
                                oplinha = input("São os IDs {} na tabela [{}], digite o ID que deseja alterar \n"
                                                "Ou digite [sair] para voltar \n"
                                                "--> "
                                                .format(verifica(conbd, tabela=tab, veri=0), tab))
                                if oplinha != "sair":
                                    if oplinha.isnumeric():  # Verifica se o usuario digitou um número
                                        if int(oplinha) in verifica(conbd, tabela=tab,
                                                                    veri=[]):  # Verifica número digitado do usúsario
                                            print("=" * 50)
                                            print("Aqui está a lista das colunas dessa tabela: \n",
                                                verificaColums(conbd, table=tab, colum=[]))
                                            opcolum = input("Digite o nome da coluna que deseja alterar \n"
                                                            "--> ")
                                            if opcolum in verificaColums(conbd, table=tab, colum=[]):
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

                        if verifica(conbd, tabela=tab, veri=0) != 0:  # Verifica se possui valores
                            while True:
                                print("=" * 50)
                                oplinha = input("São os IDs {} na tabela [{}], digite o ID que deseja alterar \n"
                                                "Ou digite [sair] para voltar \n"
                                                "--> "
                                                .format(verifica(conbd, tabela=tab, veri=[]), tab))
                                if oplinha != "sair":
                                    if oplinha.isnumeric():  # Verifica se o usuario digitou um número
                                        if int(oplinha) in verifica(conbd, tabela=tab,
                                                                    veri=[]):  # Verifica número digitado do usúsario
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

                        if verifica(conbd, tabela=tab, veri=0) != 0:  # Verifica se possui valores
                            while True:
                                print("=" * 50)
                                oplinha = input("São os IDs {} na tabela [{}], digite o ID que deseja alterar \n"
                                                "Ou digite [sair] para voltar \n"
                                                "--> "
                                                .format(verifica(conbd, tabela=tab, veri=0), tab))
                                if oplinha != "sair":
                                    if oplinha.isnumeric():  # Verifica se o usuario digitou um número
                                        if int(oplinha) in verifica(conbd, tabela=tab,
                                                                    veri=[]):  # Verifica número digitado do usúsario
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

                        if verifica(conbd, tabela=tab, veri=0) != 0:  # Verifica se possui valores
                            while True:
                                print("=" * 50)
                                oplinha = input("São os IDs {} na tabela [{}], digite o ID que deseja alterar \n"
                                                "Ou digite [sair] para voltar \n"
                                                "--> "
                                                .format(verifica(conbd, tabela=tab, veri=0), tab))
                                if oplinha != "sair":
                                    if oplinha.isnumeric():  # Verifica se o usuario digitou um número
                                        if int(oplinha) in verifica(conbd, tabela=tab,
                                                                    veri=[]):  # Verifica número digitado do usúsario
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

                        if verifica(conbd, tabela=tab, veri=0) != 0:  # Verifica se possui valores
                            while True:
                                print("=" * 50)
                                oplinha = input("São os IDs {} na tabela [{}], digite o ID que deseja alterar \n"
                                                "Ou digite [sair] para voltar \n"
                                                "--> "
                                                .format(verifica(conbd, tabela=tab, veri=0), tab))
                                if oplinha != "sair":
                                    if oplinha.isnumeric():  # Verifica se o usuario digitou um número
                                        if int(oplinha) in verifica(conbd, tabela=tab,
                                                                    veri=[]):  # Verifica número digitado do usúsario
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

                        if verifica(conbd, tabela=tab, veri=0) != 0:  # Verifica se possui valores
                            while True:
                                print("=" * 50)
                                oplinha = input("São os IDs {} na tabela [{}], digite o ID que deseja alterar \n"
                                                "Ou digite [sair] para voltar \n"
                                                "--> "
                                                .format(verifica(conbd, tabela=tab, veri=0), tab))
                                if oplinha != "sair":
                                    if oplinha.isnumeric():  # Verifica se o usuario digitou um número
                                        if int(oplinha) in verifica(conbd, tabela=tab,
                                                                    veri=[]):  # Verifica número digitado do usúsario
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
