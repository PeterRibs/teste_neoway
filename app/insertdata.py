# Para inserir o dado no banco de dados PostgresSQL

import time
import psycopg2 # A biblioteca psycopg2 vai fazer a comunicação com o PostgreSQL.

class insertdata:
  def __init__(self)-> None:
    pass

  def loading(self, db_name, User, Password, table_name, data, dataframe): # carregar para o banco de dados
    inicio_data = time.time();
    connection = self.connect_db(db_name, User, Password) 
    self.del_old_table(connection, table_name, data)
    self.new_table(connection, table_name, data)
    self.insert_file_database(connection, dataframe, table_name, data)
    self.close_connection(connection)
    print ("loading %s:" %table_name, time.time() - inicio_data)

  def connect_db(self, db_name, User, Password): # conectar com o banco de dados
    con = psycopg2.connect(host='db',
                          database= db_name,
                          user= User,
                          password= Password)
    return con

  def run_sql(self, connection, sql): 
    cur = connection.cursor()
    newSql = cur.mogrify(sql);
    cur.execute(newSql)
    connection.commit()

  def close_connection(self, connection):
    connection.close()

  def del_old_table(self, connection, table_name, data): # deletar a tabela que estiver no banco de dados para armazenar a nova
    sql = 'DROP TABLE IF EXISTS public.%s CASCADE' % (data +'_'+table_name)
    self.run_sql(connection, sql)

  def new_table(self, connection, table_name, data): # criando uma tabela no banco de dados
    if data.lower() == 'general':   
      sql = '''CREATE TABLE public.%s
        ( cpf                   CHARACTER VARYING(20),
          cpf_validation        CHARACTER VARYING(2),
          private               CHARACTER VARYING(2), 
          incompleto            CHARACTER VARYING(2), 
          data_ultima_compra    CHARACTER VARYING(20), 
          ticket_medio          CHARACTER VARYING(20), 
          ticket_ultima_compra  CHARACTER VARYING(20), 
          loja_mais_frequente   CHARACTER VARYING(20) REFERENCES validation_cnpj(cnpj), 
          loja_ultima_compra    CHARACTER VARYING(20) REFERENCES validation_cnpj(cnpj)
        )''' % (data +'_'+table_name)
      self.run_sql(connection, sql)
    
    elif data.lower() == 'validation':
      sql = '''CREATE TABLE public.%s
        ( %s                   CHARACTER VARYING(100) PRIMARY KEY, 
          validation             CHARACTER VARYING(10) 
        )''' % (data +'_'+table_name, table_name)
      self.run_sql(connection, sql)
      
    else:
      print('Choose one possible data: general or validation')

  def insert_file_database(self, connection, file_table, table_name, data): # inserindo os dados no banco de dados de acordo com as diferentes tabelas, colunas e linhas
    if data.lower() == 'general':
      for i in range(0, len(file_table)):
        sql_general = """ INSERT into public.%s (cpf, cpf_validation, private, incompleto, data_ultima_compra, ticket_medio, ticket_ultima_compra, loja_mais_frequente, loja_ultima_compra) values('%s','%s','%s','%s','%s','%s','%s','%s','%s')""" % (data +'_'+table_name, file_table['cpf'][i], file_table['validation'][i], file_table['private'][i], file_table['incompleto'][i], file_table['data_ultima_compra'][i], file_table['ticket_medio'][i], file_table['ticket_ultima_compra'][i], file_table['loja_mais_frequente'][i], file_table['loja_ultima_compra'][i])
        self.insert_db(connection, sql_general)

    elif data.lower() == 'validation':
      for i in range(0, len(file_table)):
        sql_validation= """ INSERT into public.%s (%s, validation) values('%s','%s')""" % (data +'_'+table_name, table_name, file_table[i][0], file_table[i][1])
        self.insert_db(connection, sql_validation)

    else:
      print('Choose one possible data: general or validation')

  def insert_db(self, con, sql): # entregando a tabela
    cur = con.cursor()
    try:
      cur.execute(sql)
      con.commit()
    except (Exception, psycopg2.DatabaseError) as error:
      print("Error: %s" % error)
      con.rollback()
      cur.close()
      return 1
    cur.close()