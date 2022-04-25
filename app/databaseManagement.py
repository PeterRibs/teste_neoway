import psycopg2 
import pandas as pd

class DatabaseManagement:
  def __init__(self, db_name, User, Password, host):
    self.db_name = db_name
    self.User = User
    self.Password = Password
    self.host = host
    self.connected = None

  def loading(self, dataName, dataType, dataDF, colNames):
    self.del_old_table(dataName, dataType)
    self.new_table(dataName, dataType, colNames)
    self.insertData(dataName, dataType, dataDF, colNames)

  def connect_db(self):
    self.connected = psycopg2.connect(host = self.host,
                          database = self.db_name,
                          user = self.User,
                          password = self.Password)
    return self.connected

  def open_connection(self):
    print("Open the connection with %s" %(self.db_name))
    self.connect_db()

  def close_connection(self):
    if self.connected == None:
      print("Connection do not exist!")
    else:
      print("Close the connection with %s" %(self.db_name))
      self.connected.close()
      self.connected == None

  def run_sql(self, sql): 
    cur = self.connected.cursor()
    newSql = cur.mogrify(sql);
    cur.execute(newSql)
    self.connected.commit()

  def del_old_table(self, dataName, dataType):
    sql = 'DROP TABLE IF EXISTS public.%s CASCADE' % (dataType +'_'+dataName)
    self.run_sql(sql)

  def new_table(self, dataName, dataType, *colNames):
    dataColNames = colNames[0]
    databaseColumns = []
    if dataType.lower() == 'general':
      for dataColName in dataColNames:
        if dataColName == "loja_mais_frequente" or dataColName == "loja_ultima_compra":
            databaseColumns.append('%s' % (dataColName + "     CHARACTER VARYING(20) REFERENCES validation_cnpj (cnpj)"))
        else:
            databaseColumns.append('%s' % (dataColName + "     CHARACTER VARYING(20)" )) 

      sql = '''CREATE TABLE public.%s 
        (%s
        )''' %(dataType +'_'+dataName, ", ".join(databaseColumns))      
      self.run_sql(sql)
    
    elif dataType.lower() == 'validation':
      sql = '''CREATE TABLE public.%s
        ( %s                   CHARACTER VARYING(20) PRIMARY KEY, 
          validation           CHARACTER VARYING(2) 
        )''' % (dataType +'_'+dataName, dataName)
      self.run_sql(sql)
      
    else:
      print('Choose one possible data: general or validation')

  def insertData(self, dataName, dataType, dataDF, *colNames):
    dataColNames = colNames[0]
    databaseColumns = ", ".join(dataColNames)
    
    if dataType.lower() == 'general':
      for i in range(0, len(dataDF)):
        sql_general = """ INSERT into public.%s (%s) values('%s','%s','%s','%s','%s','%s','%s','%s','%s')""" % (dataType +'_'+dataName, databaseColumns, dataDF[dataColNames[0]][i], dataDF[dataColNames[1]][i], dataDF[dataColNames[2]][i], dataDF[dataColNames[3]][i], dataDF[dataColNames[4]][i], dataDF[dataColNames[5]][i], dataDF[dataColNames[6]][i], dataDF[dataColNames[7]][i], dataDF[dataColNames[8]][i])
        self.insert_db(sql_general)

    elif dataType.lower() == 'validation':
      for i in range(0, len(dataDF)):
        sql_validation= """ INSERT into public.%s (%s, validation) values('%s','%s')""" % (dataType +'_'+dataName, dataName, dataDF[i][0], dataDF[i][1])
        self.insert_db(sql_validation)

    else:
      print('Choose one possible data: general or validation')

  def insert_db(self, sql):
    cur = self.connected.cursor()
    try:
      cur.execute(sql)
      self.connected.commit()
    except (Exception, psycopg2.DatabaseError) as error:
      print("Error: %s" % error)
      self.connection.rollback()
      cur.close()
      return 1
    cur.close()

  def get_db(self):
    return

  def print_db(self, dataName, dataType, *colNames):
    dataColNames = colNames[0]
    reg = self.call_db('select * from public.%s' % (dataType +'_'+dataName))
    df_bd = pd.DataFrame(reg, columns = dataColNames)              
    return df_bd.head()

  def call_db(self, sql):
    con = self.connect_db()
    cur = con.cursor()
    cur.execute(sql)
    recset = cur.fetchall()
    data_row = []
    for rec in recset:
      data_row.append(rec)
    con.close()
    return data_row
