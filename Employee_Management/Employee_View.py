import mysql.connector
from datetime import datetime



class DbConnect:
    def get_connection(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Arya@181094",
                database="companydb"
            )
            return self.connection
        except Exception as e:
            return None

class EmployeeManager(DbConnect):
    def get_object(self,id=None):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            query = "select * from employee where id = %s"
            values =(id, )
            self.cursor.execute(query,values)
            records = self.cursor.fetchone()
            return records
        except Exception as e:
            return None
    def get(self):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            query = "select * from employee"
            self.cursor.execute(query)
            records = self.cursor.fetchall()
            #print(records)
            for data in records:
                print(data)
        except Exception as e:
            print(e)
    def post(self,**kwargs):
       try:
           self.connect = super().get_connection()
           self.cursor = self.connect.cursor()
           query = "INSERT INTO employee (name,place,mobile,email,department,salary,joining_date) VALUES (%s,%s,%s,%s,%s,%s,%s)"
           values = [v for v in kwargs.values()]
           self.cursor.execute(query, values)
           self.connect.commit()
           print("New Member Added Successfully...")
       except Exception as e:
           print(e)
    def retrieve(self, id=None):
        try:
            records = self.get_object(id=id)
            if records == None:
                print("Employee Not Found...!")
            else:
                print(records)
        except Exception as e:
            print(e)
    def delete(self,id=None):
        try:
            records = self.get_object(id=id)
            values =(id, )
            if records != None:
                query = "delete from employee where id = %s"
                self.cursor.execute(query, values)
                self.connection.commit()
                print("Member deleted Successfully..")
            else:
                print("Member Not Fount....")
        except Exception as e:
            print(e)
    def put(self,id=None,**kwargs):
        try:
            records = self.get_object(id=id)
            if records != None:
                placeholder = " "
                for k in kwargs.keys():
                    placeholder += k + "%s, "
                    placeholder = placeholder.rstrip(", ")
                    query = f"update member set {placeholder} where id = %s"
                    values = [v for v in kwargs.values()]
                    values.append(id)
                    self.cursor.execute(query,values)
                    self.connection.commit()
                    print("Member Details Updated...")
            else:
                print("Member Not Found...")
        except Exception as e:
            print(e)






#*************************************************************************
connection_instance = DbConnect()
print(connection_instance.get_connection())

employee_instance = EmployeeManager()
#employee_instance.post(name="Maya",place="Palarivattom",mobile="8825551361",email="maya@gmail.com",department="Designer",salary="60000",joining_date=datetime.today())
#employee_instance.get()
#employee_instance.retrieve(1)
employee_instance.delete(1)
employee_instance.get()
#employee_instance.put(1)