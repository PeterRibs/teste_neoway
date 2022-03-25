# Arquivo para ler a tabela de dados

import pandas as pd

class readtable():
  def __init__(self) -> None:
    pass

  def table(self, data_teste):
    base_teste = pd.read_table(data_teste, header = None)
    return base_teste