import mysql.connector

# Creates or gets a MySQL connection object
mydb = mysql.connector.connect(
    host="localhost",
    user= "root",
    password= "Arya@181094",
    database= "company_db"
)
print("Connected to MySQL Database")

obj = mydb.cursor()
query = """ 
        CREATE TABLE employee(
        id int primary key,
        name varchar(200),
        place varchar(200),
        company varchar(200),
        age int,
        salary int )
"""

obj.execute(query)
print("Table Create Successfully.....")

