import mysql.connector

# Creates or gets a MySQL connection object
mydb = mysql.connector.connect(
    host="localhost",
    user= "root",
    password= "Arya@181094",
    database= "company_db"
)
obj = mydb.cursor()
employees = [
    (5,"Ashna","Kaloor","Luminar",23,20000),
    (6,"Vinay","Thrissur","Wipro",32,90000)
]
query = """
       INSERT INTO employee(id, name, place, company, age, salary)
       VALUES (%s, %s, %s, %s, %s, %s)
"""

obj.executemany(query, employees)
mydb.commit()
print("Employee data inserted successfully")