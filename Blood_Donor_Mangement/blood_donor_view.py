import mysql.connector
import datetime


class BloodDonorManager:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host= "localhost",
            user= "root",
            password="Arya@181094",
            database="blood_db"
        )
        print("Connected Successfully")
    def post(self,**kwargs):
        try:
            self.cursor = self.connection.cursor()
            query = ("insert into donor(name, blood_group, phone, city, last_donation) values (%s, %s, %s, %s, %s)")
            values = [v for v in kwargs.values()]
            self.cursor.execute(query, values)
            self.connection.commit()
            print("Donor Added Successfully")
        except Exception as e:
            print(e)
    def get(self):
        try:
            self.cursor = self.connection.cursor()
            query = "select * from donor"
            self.cursor.execute(query)
            records = self.cursor.fetchall()
            #print(records)
            for data in records:
                print(data)
        except Exception as e:
            print(e)
    def retrieve(self,id=None):
        try:
            #self.cursor = self.connection.cursor()
            #query = "Select * from donor where id = %s"
            #values = (id,)
            #self.cursor.execute(query,values)
            #record = self.cursor.fetchone()
            record = self.get_object(id=id)
            if record == None:
                print("Donor Not Found...")
            print(record)
        except Exception as e:
            print(e)
    def delete(self,id=None):
        try:
            #self.cursor = self.connection.cursor()
            #query = "select * from donor where id = %s"
            #values = (id,)
            #self.cursor.execute(query,values)
            #record = self.cursor.fetchone()
            record = self.get_object(id=id)
            if record != None:
                query = "delete from donor where id = %s"
                self.cursor.execute(query,values)
                self.connection.commit()
                print("Donor deleted Successfully..")
            else:
                print("Donor Not Found...")
        except Exception as e:
            print(e)
    def get_object(self,id=None):
        try:
            self.cursor = self.connection.cursor()
            query = "select * from donor where id = %s"
            values = (id,)
            self.cursor.execute(query, values)
            record = self.cursor.fetchone()
            return record
        except Exception as e:
            return None
    def put(self,id=None,**kwargs):
        try:
            record = self.get_object(id=id)   # check whether the record exists
            if record != None: # if a record is found, record will not be none
                self.cursor = self.connection.cursor()
                placeholder = ""  # creates an empty string
                # this variable will be used to construct the SET part of the SQL Query.
                for k in kwargs.keys():
                    placeholder += k + "%s, " # Build the SET condition
                    # SET name = %s, city = %s, blood_group = %s....etc
                    placeholder = placeholder.rstrip(", ") # Remove the last comma
                    # Remove the last comma
                    query = f"update donor set {placeholder} where id = %s"
                    values = [v for v in kwargs.values()]
                    values.append(id)
                    self.cursor.execute(query,values)
                    self.connection.commit()
                    print("Donor details updates successfully...")
            else:
                print("Donor not found...!")
        except Exception as e:
            print(e)


donor_instance = BloodDonorManager()
#donor_instance.post(name="Naomika",blood_group = "B+",phone="8556234580",city="Varkala",last_donation= datetime.datetime.today())
#donor_instance.get()
#donor_instance.retrieve(id = 5)
#donor_instance.delete(id = 2)
#print("After Deleting a donor...")
#donor_instance.get()
donor_instance.put(id= 4)