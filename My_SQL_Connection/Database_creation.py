import mysql.connector

# Creates or gets a MySQL connection object
mydb = mysql.connector.connect(
    host="localhost",
    user= "root",
    password= "Arya@181094"
)

mycursor = mydb.cursor()
#mycursor.execute("create database Company_db")
#print("Database Created Successfully.....")
mycursor.execute("SHOW DATABASES")
print(mycursor.fetchall())
