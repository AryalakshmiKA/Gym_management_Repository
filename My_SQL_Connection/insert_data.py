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
       INSERT INTO employee(id, name, place,company, age, salary)
       VALUES (1, "Rahul","Aluva","Luminar",35,80000),
       (2,"Teena","Kakkanadu","TCS",30,75000),
       (3,"Gouthan","Edappally","TCS",27,65000),
       (4,"Shyam","Edappally","Infosys",29,60000)
"""
obj.execute(query)
mydb.commit()
print("Employee data inserted successfully")