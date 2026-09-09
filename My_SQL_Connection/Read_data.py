import mysql.connector


# Creates or gets a MySQL connection object
mydb = mysql.connector.connect(
    host="localhost",
    user= "root",
    password= "Arya@181094",
    database= "company_db"
)
obj = mydb.cursor()
query = "SELECT * FROM employee"
obj.execute(query)
result = obj.fetchall()
#print(result)
for emp in result:
    print(emp)

print("Get the Details of One employee....")
obj.execute("SELECT * FROM employee")
employee = obj.fetchone()
print(employee)