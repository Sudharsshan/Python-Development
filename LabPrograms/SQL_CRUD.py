'''
DATE: 8-7-24
TASK: Write a python program to perform CRUD operations in a SQL
      database.
'''
import mysql.connector
password = 'Lumine2004.'
database = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd=password,
    database='powerstation'
)
cursorObject = database.cursor()

#Perform query operation
cursorObject.execute('SELECT * FROM  subStation')
obtainedData = cursorObject.fetchall()
for data in obtainedData:
    print(data)
cursorObject = database.cursor()

# Perform update operation
cursorObject.execute('UPDATE subStation SET `Active Power` = 150 WHERE FeederID=2')

# Perform insert operation
cursorObject.execute('INSERT INTO subStation VALUES(3,\'LOAD\',200,200)')

# Perform delete operation
cursorObject.execute('DELETE FROM subStation WHERE FeederID=3')
obtainedData = cursorObject.fetchall()
for data in obtainedData:
    print(data)
cursorObject = database.cursor()

database.close()