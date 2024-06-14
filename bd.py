# ================================================ VERIFICAR ============================================================

def verifica(condb, tabela): # Função para verificar quantas linhas de ID a tabela possui
    mycursor = condb.cursor()
    mycursor.execute(f"SELECT * FROM {tabela}")
    myresult = mycursor.fetchall()
    veri = []
    for x in myresult:
        veri.append(x[0])
    mycursor.close()
    return list(veri)

def verificaNome(condb, tabela): # Função para verificar quantas linhas de ID a tabela possui
    mycursor = condb.cursor()
    mycursor.execute(f"SELECT * FROM {tabela}")
    myresult = mycursor.fetchall()
    veri = []
    for x in myresult:
        veri.append(x[1])
    mycursor.close()
    return list(veri)

def verificaColums(condb, table): # Função para verificar quantas colunas a tabela possui
    mycursor = condb.cursor()
    mycursor.execute(f"DESCRIBE {table}")
    colum = mycursor.fetchall()
    mycursor.close()
    return [c[0] for c in colum if c[3] != 'PRI']

# ================================================ CADASTRO ============================================================
def cadastrarProdutos(condb, nome, descricao, preco, quantidade):
    myCursor = condb.cursor()

    sql = "INSERT INTO produtos (Nome, Descricao, Preco) Values (%s, %s, %s)"
    val = (nome, descricao, preco)
    myCursor.execute(sql, val)

    ID = myCursor.lastrowid

    sql1 = "INSERT INTO estoque (ID_Produto, Quantidade) VALUE (%s, %s)"
    val1 = (ID, quantidade)
    myCursor.execute(sql1, val1)

    condb.commit()
    print("=" * 50)
    print("Produto cadastrado com sucesso!")
    myCursor.close()


def cadastrarProdutosC(condb, nome, descricao, preco, quantidade, cnome, cdes):
    myCursor = condb.cursor()

    sql = "INSERT INTO produtos (Nome, Descricao, Preco) Values (%s, %s, %s)"
    val = (nome, descricao, preco)
    myCursor.execute(sql, val)

    ID = myCursor.lastrowid

    sql1 = "INSERT INTO estoque (ID_Produto, Quantidade) VALUE (%s, %s)"
    val1 = (ID, quantidade)
    myCursor.execute(sql1, val1)

    sql2 = "INSERT INTO categoriasprodutos (ID_Categoria, Nome, Descricao) VALUE (%s, %s, %s)"
    val2 = (ID, cnome,cdes)
    myCursor.execute(sql2, val2)

    condb.commit()
    print("=" * 50)
    print("Produto cadastrado com sucesso!")
    myCursor.close()


def cadastrarProdutosF(condb, nome, descricao, preco, quantidade, fnome, fcontato, fende):
    myCursor = condb.cursor()

    sql = "INSERT INTO produtos (Nome, Descricao, Preco) Values (%s, %s, %s)"
    val = (nome, descricao, preco)
    myCursor.execute(sql, val)

    ID = myCursor.lastrowid

    sql1 = "INSERT INTO estoque (ID_Produto, Quantidade) VALUE (%s, %s)"
    val1 = (ID, quantidade)
    myCursor.execute(sql1, val1)

    sql2 = "INSERT INTO fornecedores (ID_Fornecedor, Nome, Contato, Endereco) VALUE (%s, %s, %s, %s)"
    val2 = (ID, fnome, fcontato, fende)
    myCursor.execute(sql2, val2)

    condb.commit()
    print("=" * 50)
    print("Produto cadastrado com sucesso!")
    myCursor.close()


def cadastrarProdutosCF(condb, nome, descricao, preco, quantidade, cnome, cdes, fnome, fcontato, fende):
    myCursor = condb.cursor()

    sql = "INSERT INTO produtos (Nome, Descricao, Preco) Values (%s, %s, %s)"
    val = (nome, descricao, preco)
    myCursor.execute(sql, val)

    ID = myCursor.lastrowid

    sql1 = "INSERT INTO estoque (ID_Produto, Quantidade) VALUE (%s, %s)"
    val1 = (ID, quantidade)
    myCursor.execute(sql1, val1)

    sql2 = "INSERT INTO categoriasprodutos (ID_Categoria, Nome, Descricao) VALUE (%s, %s, %s)"
    val2 = (ID, cnome,cdes)
    myCursor.execute(sql2, val2)

    sql3 = "INSERT INTO fornecedores (ID_Fornecedor, Nome, Contato, Endereco) VALUE (%s, %s, %s, %s)"
    val3 = (ID, fnome, fcontato, fende)
    myCursor.execute(sql3, val3)

    condb.commit()
    print("=" * 50)
    print("Produto cadastrado com sucesso!")
    myCursor.close()


def cadastrarClientes(condb, nome, sobrenome, endereco, cidade, codigo):
    myCursor = condb.cursor()
    sql = "INSERT INTO clientes (Nome, Sobrenome, Endereco, Cidade, CodigoPostal) Values (%s, %s, %s, %s, %s)"
    val = (nome, sobrenome, endereco, cidade, codigo)
    myCursor.execute(sql, val)
    condb.commit()
    print("Cliente cadastrados com sucesso!")
    myCursor.close()


def cadastrarFornecedores(condb, nome, contato, endereco):
    myCursor = condb.cursor()
    sql = "INSERT INTO fornecedores (Nome, Contato, Endereco) Values (%s, %s, %s)"
    val = (nome, contato, endereco)
    myCursor.execute(sql, val)
    condb.commit()
    print("Fornecedores cadastrados com sucesso!")
    myCursor.close()


def cadastrarFuncionarios(condb, nome, cargo, depart):
    myCursor = condb.cursor()
    sql = "INSERT INTO funcionarios (Nome, Cargo, Departamento) Values (%s, %s, %s)"
    val = (nome, cargo, depart)
    myCursor.execute(sql, val)
    condb.commit()
    print("Funcionarios cadastrados com sucesso!")
    myCursor.close()


def cadastrarPromocoes(condb, nome, descricao, datai, dataf):
    myCursor = condb.cursor()
    sql = "INSERT INTO promocoes (Nome, Descricao, DataInicio, DataFim) Values (%s, %s, %s, %s)"
    val = (nome, descricao, datai, dataf)
    myCursor.execute(sql, val)
    condb.commit()
    print("Promoções cadastrados com sucesso!")
    myCursor.close()


# ================================================== ATUALIZAR =========================================================

def atualizarProdutos(condb, coluna, new, linha):
    mycursor = condb.cursor()
    sql = f"UPDATE produtos SET {coluna} = %s WHERE ID_Produto = %s"
    val = (new, linha)
    mycursor.execute(sql, val)
    condb.commit()
    print("Valores atualizados com sucesso!")
    mycursor.close()

def atualizarClientes(condb, coluna, new, linha):
    mycursor = condb.cursor()
    sql = f"UPDATE clientes SET {coluna} = %s WHERE ID_Cliente = %s"
    val = (new, linha)
    mycursor.execute(sql, val)
    condb.commit()
    print("Valores atualizados com sucesso!")
    mycursor.close()

def atualizarFornecedores(condb, coluna, new, linha):
    mycursor = condb.cursor()
    sql = f"UPDATE fornecedores SET {coluna} = %s WHERE ID_Fornecedor = %s"
    val = (new, linha)
    mycursor.execute(sql, val)
    condb.commit()
    print("Valores atualizados com sucesso!")
    mycursor.close()

def atualizarFuncionarios(condb, coluna, new, linha):
    mycursor = condb.cursor()
    sql = f"UPDATE funcionarios SET {coluna} = %s WHERE ID_Funcionario = %s"
    val = (new, linha)
    mycursor.execute(sql, val)
    condb.commit()
    print("Valores atualizados com sucesso!")
    mycursor.close()

def atualizarPromocoes(condb, coluna, new, linha):
    mycursor = condb.cursor()
    sql = f"UPDATE promocoes SET {coluna} = %s WHERE ID_Promocao = %s"
    val = (new, linha)
    mycursor.execute(sql, val)
    condb.commit()
    print("Valores atualizados com sucesso!")
    mycursor.close()

# ==================================================== DELETAR =========================================================

def deletarProdutos(condb, linha):
    mycursor = condb.cursor()
    sql = "DELETE FROM produtos WHERE ID_Produto = %s"
    val = (linha,)
    mycursor.execute(sql, val)
    condb.commit()
    print("Linha deletada de PRODUTOS com sucesso!")
    mycursor.close()

def deletarClientes(condb, linha):
    mycursor = condb.cursor()
    sql = "DELETE FROM clientes WHERE ID_Cliente = %s"
    val = (linha,)
    mycursor.execute(sql, val)
    condb.commit()
    print("Linha deletada de CLIENTES com sucesso!")
    mycursor.close()

def deletarFornecedores(condb, linha):
    mycursor = condb.cursor()
    sql = "DELETE FROM fornecedores WHERE ID_Fornecedor = %s"
    val = (linha,)
    mycursor.execute(sql, val)
    condb.commit()
    print("Linha deletada de FORNECEDORES com sucesso!")
    mycursor.close()

def deletarFuncionarios(condb, linha):
    mycursor = condb.cursor()
    sql = "DELETE FROM funcionarios WHERE ID_Funcionario = %s"
    val = (linha,)
    mycursor.execute(sql, val)
    condb.commit()
    print("Linha deletada de FUNCIONARIOS com sucesso!")
    mycursor.close()

def deletarPromocoes(condb, linha):
    mycursor = condb.cursor()
    sql = "DELETE FROM promocoes WHERE ID_Promocao = %s"
    val = (linha,)
    mycursor.execute(sql, val)
    condb.commit()
    print("Linha deletada de PROMOCOES com sucesso!")
    mycursor.close()

# ==================================================== LISTAR ==========================================================

def listar(condb, table):
    mycursor = condb.cursor()
    mycursor.execute(f"SELECT * FROM {table}")
    myresult = mycursor.fetchall()
    for i in myresult:
        print(i)
    mycursor.close()

# ==================================================== PEDIDO ==========================================================

def listarProdutosPedido(condb):
    print("=" * 50)
    print("Produtos disponiveis:")
    print("=" * 50)
    mycursor = condb.cursor()
    mycursor.execute("SELECT * FROM produtos")
    myresult = mycursor.fetchall()
    for i in myresult:
        print(i[1],": R$" ,i[3], sep="")
    mycursor.close()

def listarPedidosDescricao(condb):
    print("=" * 50)
    print("Descrição dos Produtos:")
    print("=" * 50)
    mycursor = condb.cursor()
    mycursor.execute("SELECT * FROM produtos")
    myresult = mycursor.fetchall()
    for i in myresult:
        print(i[1],": " ,i[2], sep="")
    mycursor.close()

def listarPedidosCategoria(condb):
    print("=" * 50)
    print("Categoria dos Produtos:")
    print("=" * 50)
    mycursor = condb.cursor()
    mycursor.execute("SELECT * FROM produtos")
    myresult = mycursor.fetchall()
    mycursor.execute("SELECT * FROM categoriasprodutos")
    socoro = mycursor.fetchall()
    for i,v in zip(myresult,socoro):
       print(i[1],": ",v[1], sep="") 
    mycursor.close()

def PediCarrinho(condb, compra):
    mycursor = condb.cursor()
    sql = "SELECT * FROM produtos WHERE Nome = %s"
    mycursor.execute(sql, (compra,))
    myresult = mycursor.fetchone()
    if myresult:
        print("="*10,"PRODUTO ADCIONADO AO CARRINHO","="*10)
        print("Nome:", myresult[1])
        print("Descrição:", myresult[2])
        print("Preço: $", myresult[3], sep="")
    else:
        print("Produto não encontrado.")
    mycursor.close()

def VerificaProdu(condb):
    mycursor = condb.cursor()
    mycursor.execute("SELECT * FROM produtos")
    myresult = mycursor.fetchall()
    loro = []
    for i in myresult:
        loro.append(i[1])
    mycursor.close()
    return loro

def Preco(condb, nome):
    mycursor = condb.cursor()
    sql= "SELECT * FROM produtos WHERE Nome = %s"
    mycursor.execute(sql, (nome,))
    myresult = mycursor.fetchone()
    mycursor.close()
    return myresult[3]

def Pedido(condb, data, toto):
    mycursor = condb.cursor()
    mycursor.execute("SELECT MAX(ID_Cliente) FROM Clientes")
    ID = mycursor.fetchone()[0]
    sql = "INSERT INTO pedidos (Data_Pedido, ID_Cliente, Total) VALUES (%s, %s, %s)"
    val = (data, ID, toto)
    mycursor.execute(sql, val)
    condb.commit()
    print("Pedido Finalizado!")
    mycursor.close()

def detalhesPedi(condb, IDprodu, quanti):
    mycursor = condb.cursor()
    mycursor.execute("SELECT MAX(ID_Pedido) FROM pedidos")
    IDpedi = mycursor.fetchone()[0]
    sql = "INSERT INTO detalhespedido (ID_Pedido, ID_Produto, Quantidade) VALUES (%s, %s, %s)"
    val = (IDpedi,IDprodu,quanti)
    mycursor.execute(sql,val)
    condb.commit()
    mycursor.close()

def Ovelhas(condb, nome): #  Vai pegar o ID do Produto com mesmo nome
    mycursor = condb.cursor()
    sql = f"SELECT ID_Produto FROM produtos WHERE Nome = %s"
    val = (nome,)
    mycursor.execute(sql,val)
    ID = mycursor.fetchone()[0]
    condb.commit()
    mycursor.close()
    return ID