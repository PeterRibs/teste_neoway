# Validação das IDs (CPF e CNPJ). 
# O output serão duas tabelas diferentes para cada ID, sendo o número de identificação válido quando apresentar 'validation' = 1.

from random import sample # biblioteca usado para o embaralhamento

class datavalidation:
  def __init__(self) -> None:
    pass
  
  def validate (self, datalist):
    list_cpf = self.take_values(datalist, 0)
    list_cnpj = self.take_values(datalist, 6)
    list_id_total = []
    list_id_total.append(self.cpf(list_cpf))
    list_id_total.append(self.cnpj(list_cnpj))
    return list_id_total
  
  def take_values(self, data_list, col):
    list_id=[]
    for i in range(0, len(data_list)):
      list_id.append(data_list[i][col])
    id_set = set(list_id)
    id_list = list(id_set)
    return id_list

  def shuffle(self, value): # embaralhamento para testar se os IDs possuem os números todos iguais
    return ''.join(sample(value, len(value)))
  
  def cpf (self, data_id): # validação do cpf
    list_validate_cpf = []
    for i in range(0, len(data_id)):
      data_val = data_id[i]
      shuffled_id = self.shuffle(data_val)
      if len(data_val) != 11:
        list_validate_cpf.append([data_val, '0'])
      elif data_val == data_val[::-1] and data_val == shuffled_id:
        list_validate_cpf.append([data_val, '0'])
      else:
        for i in range(9, 11):
          value = sum((int(data_val[num]) * ((i+1) - num) for num in range(0, i)))
          digit = ((value * 10) % 11) % 10
          if digit != int(data_val[i]):
            list_validate_cpf.append([data_val, '0'])
        list_validate_cpf.append([data_val, '1'])
    return list_validate_cpf
  
  def cnpj(self, data_id): # validação do cnpj
    list_validate_cnpj = []
    for i in range(0, len(data_id)):
      data_val = data_id[i]
      shuffled_id = self.shuffle(data_val)
      if data_val == data_val[::-1] and data_val == shuffled_id:
        list_validate_cnpj.append([data_val, '0'])
      elif len(data_val) != 14:
        list_validate_cnpj.append([data_val, '0'])
      else:
        for i in range(12, 14):
          w=i-8
          j = 18 - i
          k = i - 10
          value1 = sum(int(data_val[num]) * (num + j) for num in range(0, w))
          value2 = sum(int(data_val[num]) * (num - k) for num in range(w, i))
          value = value1+value2
          digit = ((value % 11))%10
          if digit != int(data_val[i]):
            list_validate_cnpj.append([data_val, '0'])
        list_validate_cnpj.append([data_val, '1'])
    return list_validate_cnpj
