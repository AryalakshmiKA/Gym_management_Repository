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
        CREATE TABLE student(
        id int primary key,
        name varchar(200),
        age int,
        place varchar(200),
        course varchar(200),
        mobile bigint,
        college varchar(200) )
"""

obj.execute(query)
print("Table Create Successfully.....")
