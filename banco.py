import mysql.connector


class Banco():
 def __init__(self):
  pass
 def ConfirmConection(self):
  mydb = mysql.connector.connect(host = 'localhost',user='root',password='eucalipito',database='spc')
  mycursor = mydb.cursor()
  mycursor.execute("show tables")
  for x in mycursor:
   print(x)
  mydb.close()
  mycursor.close()

 def insert(self,a):

  mydb = mysql.connector.connect(host='localhost', user='root', password='eucalipito', database='spc')
  mycursor = mydb.cursor()
  sql = f"INSERT INTO pessoa (NOME,RG,CPF,ENDERECO,CPMENDERECO,CIDADE,ESTADO,PAIS,SEXO,DTNASC,EMAIL,TELEFONE,CEP) VALUES ('{a[0]}','{a[1]}','{a[2]}','{a[3]}','{a[4]}','{a[5]}','{a[6]}','{a[7]}','{a[8]}','{a[9]}','{a[10]}','{a[11]}','{a[12]}');"
  mycursor.execute(sql)
  mydb.commit()
  mydb.close()
  mycursor.close()