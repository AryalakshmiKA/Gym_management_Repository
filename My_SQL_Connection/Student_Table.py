import mysql.connector

# Creates or gets a MySQL connection object
mydb = mysql.connector.connect(
    host="localhost",
    user= "root",
    password= "Arya@181094",
    database= "company_db"
)
cursor = mydb.cursor()

# insert
query = """
    INSERT INTO student(id, name, age,place,course,mobile, college)
    VALUES (%s, %s, %s, %s,%s, %s,%s)
"""
values = (1,"Anjana",22,"Kakkanadu","BCA",8965741254,"BMC")


cursor.execute(query, values)
#
mydb.commit()
print("New Student Added..")


# select / View student details
cursor.execute("select * from student")
result = cursor.fetchall()
print("____Student Details____")
for stud in result:
    print(stud)


# Update student details
query = """
    update student set place = "Trivandrum" where id = 1
"""
cursor.execute(query)
mydb.commit()
print("Student details updated...")

# View updated student Details
cursor.execute("select * from student")
result = cursor.fetchone()
print("____Our Student Details____")
print(result)

# Delete Data
cursor.execute("delete from student where id = 1")
mydb.commit()
print("Student Deleted...")

# close connection
cursor.close()
mydb.close()