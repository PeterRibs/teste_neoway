# Rodando todo o processo:

from app import app

User = 'postgres'
Password = 'test'

app().all_process('db_neoway_ps', User, Password, 'base_teste.txt')

# Para consultar a tabela basta descomentar as linhas a baixo:

#from getdata import getdata
# getdata().print_db('db_neoway_ps', User, Password, 'validation', 'cnpj')
# getdata().print_db('db_neoway_ps', User, Password, 'general', 'table')