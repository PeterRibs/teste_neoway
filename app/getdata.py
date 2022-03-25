# Função para consultas no banco

from insertdata import insertdata
import pandas as pd

class getdata:
  def __init__(self) -> None:
      pass
  
  def print_db(self, db_name, User, Password, data, table_name):
    reg = self.call_db('select * from public.%s' % (data +'_'+table_name), db_name, User, Password)

    if data.lower() == 'general':
      df_bd = pd.DataFrame(reg, columns=['cpf', 'private', 'incompleto', 'data_ultima_compra','ticket_medio','ticket_ultima_compra','loja_mais_frequente','loja_ultima_compra'])
                            
    elif data.lower() == 'validation':
      df_bd = pd.DataFrame(reg, columns=['cnpj', "validation"])

    return df_bd.head()

  def call_db(self, sql, db_name, User, Password):
    con = insertdata().connect_db(db_name, User, Password)
    cur = con.cursor()
    cur.execute(sql)
    recset = cur.fetchall()
    data_row = []
    for rec in recset:
      data_row.append(rec)
    con.close()
    return data_row