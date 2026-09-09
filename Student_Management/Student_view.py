import mysql.connector


class DbConnect:
    def get_connection(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Arya@181094",
                database="student_db"
            )
            return self.connection
        except Exception as e:
            return None

class StudentManager(DbConnect):
    def get_object(self,id=None):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            query = "select * from student where id = %s"
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
            query = "select * from student"
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
           query = "INSERT INTO student (name,place,mobile,email,department) VALUES (%s,%s,%s,%s,%s)"
           values = [v for v in kwargs.values()]
           self.cursor.execute(query, values)
           self.connect.commit()
           print("New Student Added Successfully...")
       except Exception as e:
           print(e)
    def retrieve(self, id=None):
        try:
            records = self.get_object(id=id)
            if records == None:
                print("Student Not Found...!")
            else:
                print(records)
        except Exception as e:
            print(e)
    def delete(self,id=None):
        try:
            records = self.get_object(id=id)
            values =(id, )
            if records != None:
                query = "delete from student where id = %s"
                self.cursor.execute(query, values)
                self.connection.commit()
                print("Student deleted Successfully..")
            else:
                print("Student Not Fount....")
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
                    query = f"update student set {placeholder} where id = %s"
                    values = [v for v in kwargs.values()]
                    values.append(id)
                    self.cursor.execute(query,values)
                    self.connection.commit()
                    print("Student Details Updated...")
            else:
                print("Student Not Found...")
        except Exception as e:
            print(e)






#*************************************************************************
connection_instance = DbConnect()
print(connection_instance.get_connection())

student_instance = StudentManager()
student_instance.post(name="Maya",place="Palarivattom",mobile="8825551361",email="maya@gmail.com",department="Designer")
student_instance.get()
#student_instance.retrieve(1)
#student_instance.delete(1)
#student_instance.get()
#student_instance.put(1)