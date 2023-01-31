import mysql.connector

mydb= mysql.connector.connect(
    host= "localhost",
    user= "root",
    passwd="",
    database="python9"
)
mycursor = mydb.cursor()

name=input("Enter name")
address=input("Enter address")

sql="INSERT INTO CUSTOMERS(name,address)VALUES(%s%s)"
val=(name,address)

mycursor.execute(sql,val)

print("record inserted")
