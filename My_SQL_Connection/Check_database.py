import mysql.connector

# Creates or gets a MySQL connection object
mydb = mysql.connector.connect(
    host="localhost",
    user= "root",
    password= "Arya@181094"
)

if mydb.is_connected():
    print("MySQL Connected Sucessfully...!")