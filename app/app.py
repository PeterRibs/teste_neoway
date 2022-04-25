# Para centralizar e contabilizar todo o processo.

from dataTransformationTool import DataTransformationTool
from databaseManagement import DatabaseManagement
from datavalidation import DataValidation
import time
import pandas as pd

class App:
  def __init__(self, dataSet, columnsName, db_name, User, Password, host):
      self.dataSet = dataSet
      self.columnsName = columnsName
      self.db_name = db_name
      self.User = User
      self.Password = Password
      self.host = host
  
  def all_process(self, columnsNameGeneral, columnsNameCNPJ):
    print ("INICIO TOTAL")
    inicio_all = time.time()
    data = DataTransformationTool(self.dataSet, self.columnsName)
    list_id_total = DataValidation(data.dataList).validate()
    df_data = data.dataDF
    df_id_cpf = pd.DataFrame(list_id_total[0])
    df_id_cpf
    df_id_cpf.columns = ['cpf', 'validation']
    df_data_general = pd.merge(df_data, df_id_cpf, how='inner', on='cpf')
    database = DatabaseManagement(self.db_name, self.User, self.Password, self.host)
    database.open_connection()
    #database.loading('cnpj', 'validation', list_id_total[1], columnsNameCNPJ)
    database.loading('table', 'general', df_data_general, columnsNameGeneral)
    database.close_connection()
    print ("FIM - TOTAL:", time.time() - inicio_all)
    
    print('Registros CPF totais:', len(list_id_total[0]))
    for i in range(0, len(list_id_total[0])):
      if list_id_total[0][i][1] =="0":
        print('CPF não validado:', list_id_total[0][i][0])
    
    print('Registros CNPJ totais:', len(list_id_total[1]))
    for i in range(0, len(list_id_total[1])):
      if list_id_total[1][i][1] == "0":
        print('CNPJ não validado:', list_id_total[1][i][0])