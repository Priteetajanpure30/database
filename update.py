import mysql.connector

mydb= mysql.connector.connect(
    host= "localhost",
    user= "root",
    passwd="",
    database="python9"
)
mycursor = mydb.cursor()

mycursor.execute("update customers set address='Nashik' where name='admin'")
mydb.commit()
print("Record updated")
