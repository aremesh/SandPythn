import pyodbc 
#cnxn = pyodbc.connect("Driver=SQL Server Native Client 11.0;"
#                      "Server=15FF9043PC;"
#                      "Database=tbdb;"
#                      "Trusted_Connection=yes;")
cnxn = pyodbc.connect("Driver=SQL Server Native Client 11.0;"
                      "Server=15FF9043PC;"
                      "Database=tbdb;"
                      "user=pyuser;"
                      "password=abcd12345;"
                      "Trusted_Connection=yes;")


cursor = cnxn.cursor()
cursor.execute("insert into xx_users(userid,username,password)values('ac1','c','c')")
cursor.execute("update xx_users set [password]='bisi' where userid='ac'")
cursor.execute("delete from  xx_users  where userid='ac'")
cnxn.commit()
cursor.execute('SELECT *  FROM xx_users')

for row in cursor:
    print('row = %r' % (row,))