from app import App

User = 'postgres'
Password = 'test'
host = "localhost"

columnsName = ['cpf', 'private', 'incompleto', 'data_ultima_compra', 'ticket_medio', 'ticket_ultima_compra', 'loja_mais_frequente', 'loja_ultima_compra']

columnsNameGeneral = ['cpf', 'private', 'incompleto', 'data_ultima_compra', 'ticket_medio', 'ticket_ultima_compra', 'loja_mais_frequente', 'loja_ultima_compra', "validation"]

columnsNameCNPJ = ["cnpj", "validation"]

App('base_teste.txt', columnsName, 'db_test', User, Password, host).all_process(columnsNameGeneral, columnsNameCNPJ)

### Para consultar a tabela basta descomentar as linhas a baixo:
# from databaseManagement import DatabaseManagement
# callDB = DatabaseManagement('db_neoway_ps', User, Password, host)
# callDB.open_connection()
# validation_cnpj = callDB.print_db('cnpj', 'validation', columnsNameCNPJ)
# general_table = callDB.print_db('table', 'general', columnsNameGeneral)
# callDB.close_connection()
# print(validation_cnpj)
# print(general_table)