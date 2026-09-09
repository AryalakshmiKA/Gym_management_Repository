import mysql.connector

# Creates or gets a MySQL connection object
mydb = mysql.connector.connect(
    host="localhost",
    user= "root",
    password= "Arya@181094",
    database= "company_db"
)
cursor = mydb.cursor()

id = int(input("Enter your ID: "))
name = input("Enter your name : ")
place = input("Enter your Location : ")
company = input("Enter your Company : ")
age = int(input("Enter your age : "))
salary = int(input("Enter Your Salary : "))

query = """
    INSERT INTO employee(id, name, place, company, age, salary)
    VALUES (%s, %s, %s, %s, %s, %s)
"""
values = (id,name,place,company,age,salary)
cursor.execute(query,values)
mydb.commit()
print("New employee record inserted...")

cursor.execute("SELECT * FROM employee")
result = cursor.fetchall()
for emp in result:
    print(emp)