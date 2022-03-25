# Para centralizar e contabilizar todo o processo.

from insertdata import insertdata
from datamanagement import datamanagement
from datavalidation import datavalidation
import time
import pandas as pd

class app:
  def __init__(self) -> None:
      pass
  
  def all_process(self, db_name, User, Password, data_teste):
    print ("INICIO TOTAL")
    inicio_all = time.time()
    data = self.get_table(data_teste)
    list_id_total = datavalidation().validate(data)
    df_data = pd.DataFrame(data)
    df_data.columns = ['cpf', 'private', 'incompleto', 'data_ultima_compra', 'ticket_medio', 'ticket_ultima_compra','loja_mais_frequente', 'loja_ultima_compra']
    df_id_cpf = pd.DataFrame(list_id_total[0])
    df_id_cpf
    df_id_cpf.columns = ['cpf', 'validation']
    df_data_general = pd.merge(df_data, df_id_cpf, how='inner', on='cpf')
    insertdata().loading(db_name, User, Password, 'cnpj', 'validation', list_id_total[1])
    insertdata().loading(db_name, User, Password, 'table', 'general', df_data_general)
    print ("FIM - TOTAL:", time.time() - inicio_all)
    
    print('Registros CPF totais:', len(list_id_total[0]))
    for i in range(0, len(list_id_total[0])):
      if list_id_total[0][i][1] =="0":
        print('CPF não validado:', list_id_total[0][i][0])
    
    print('Registros CNPJ totais:', len(list_id_total[1]))
    for i in range(0, len(list_id_total[1])):
      if list_id_total[1][i][1] == "0":
        print('CNPJ não validado:', list_id_total[1][i][0])

  def get_table(self, data_teste): 
    list_data = datamanagement().transform_data(data_teste)
    return list_data
