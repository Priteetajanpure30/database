import mysql.connector

mydb= mysql.connector.connect(
    host= "localhost",
    user= "root",
    passwd="",
    database="python9"
)
mycursor= mydb.cursor()

mycursor.execute("CREATE table customers(name varchar(25),address varchar(25))")
print("table created"); 
