# def obterProdutoID(conbd, nome):
#     try:
#         with conbd.cursor() as cursor:
#             sql = 'SELECT ID_Produto FROM produtos WHERE Nome = %s'
#             cursor.execute(sql, (nome,))
#             resultado = cursor.fetchone()
#             if resultado:
#                 return resultado[0]
#             else:
#                 print(f"Produto com nome '{nome}' não encontrado.")
#                 return None
#     except Error as e:
#         print(f"Ocorreu um erro ao obter o ID do produto: {e}")
#         return None


# def deletarProduto(conbd, nome_produto):
#     try:
#         produto_id = obterProdutoID(conbd, nome_produto)
#         if not produto_id:
#             return
        
#         conbd.start_transaction()
#         with conbd.cursor() as cursor:
#             sql_detalhes_pedido = 'DELETE FROM detalhespedido WHERE ID_Produto = %s'
#             cursor.execute(sql_detalhes_pedido, (produto_id,))
#         with conbd.cursor() as cursor:
#             sql_estoque = 'DELETE FROM estoque WHERE ID_Produto = %s'
#             cursor.execute(sql_estoque, (produto_id,))
#         with conbd.cursor() as cursor:
#             sql_produto = 'DELETE FROM produtos WHERE ID_Produto = %s'
#             cursor.execute(sql_produto, (produto_id,))
#         conbd.commit()
#         print("Produto e suas referências deletadas com sucesso")

#     except Error as e:
#         conbd.rollback()
#         print(f"Ocorreu um erro ao deletar o produto: {e}")

#     finally:
#         conbd.close()
