# Transformação dos dados.
# Após pegar ler a tabela fornecida, separei as colunas e utilizei como lista para inserir no banco de dados.
# CPF e CNPJ foram trasformados em células apenas com os números e as vírgulas foram transformadas em pontos.
# Os valores 'NULL' continuaram assim.

from readtable import readtable

class datamanagement:
  def __init__(self) -> None:
    pass

  def transform_data(self, data_teste):
    data = self.read_table(data_teste)
    data_list = self.split_columns(data)

    for i in range(0, len(data_list)):
      data_list[i][0] = self.id_transform (data_list[i][0])
      for ii in range(1, len(data_list[i])):
        if data_list[i][ii] == 'NULL':
          data_list[i][ii] = 'NULL'
        else:
          data_list[i][4] = self.decimal_transform (data_list[i][4])
          data_list[i][5] = self.decimal_transform (data_list[i][5])
          data_list[i][6] = self.id_transform (data_list[i][6])
          data_list[i][7] = self.id_transform (data_list[i][7])
    return data_list

  def read_table(self, data_teste):
    base_teste = readtable().table(data_teste)
    return base_teste

  def split_columns(self, value):
    data_list=[]
    for i in range(1, len(value)):
      data_list.append(value[0][i].split())
    return data_list
  
  def id_transform (self, value):
    if(value == 'NULL'):
      return "NULL"
    else:
      return ''.join([str(digits_num) for digits_num in value if digits_num.isdigit()])

  def decimal_transform (self, value):
    return value.replace(',', '.')