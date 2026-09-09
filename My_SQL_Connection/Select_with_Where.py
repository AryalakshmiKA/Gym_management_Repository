import mysql.connector

# Creates or gets a MySQL connection object
mydb = mysql.connector.connect(
    host="localhost",
    user= "root",
    password= "Arya@181094",
    database= "company_db"
)
obj = mydb.cursor()

query = "select * from employee where id = 3"
obj.execute(query)
result = obj.fetchone()
print(result)

query = "select * from employee where company = 'Luminar'"
obj.execute(query)
result = obj.fetchall()
print("Employee From Luminar  :")
for emp in result:
    print(emp)

query = "select * from employee where place = 'Edappally'"
obj.execute(query)
result = obj.fetchall()
print("Employees from Edappally  : ")
for emp in result:
    print(emp)