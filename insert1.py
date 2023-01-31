import mysql.connector

mydb= mysql.connector.connect(
    host= "localhost",
    user= "root",
    passwd="",
    database="python9"
)

mycursor = mydb.cursor()

mycursor.execute("INSERT INTO customers(name,address) VALUES('aa','bb')")
mydb.commit()
print("Record inserted")
