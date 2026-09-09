import mysql.connector

# Creates or gets a MySQL connection object
mydb = mysql.connector.connect(
    host="localhost",
    user= "root",
    password= "Arya@181094",
    database= "company_db"
)
obj = mydb.cursor()

query = """
    UPDATE employee set place = "Trivandrum" 
    where id = 1
"""
obj.execute(query)
mydb.commit()
print("Data updated successfully")

print("___After Updation_____")
query = "select * from employee where id = 1"
obj.execute(query)
result = obj.fetchone()
print(result)


print("___Delete data___")
query = "DELETE FROM employee where id = 5"
obj.execute(query)
mydb.commit()

query = "select * from employee"
obj.execute(query)
result = obj.fetchall()
for row in result:
    print(row)