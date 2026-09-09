class Customer:
    def __init__(self):
        self.name = ""
        self.mobil = ""
        self.address = ""
        self.email = ""
    def customer_data(self):
        self.name = input("Enter Customer Name   : ")
        self.address = input("Enter Address : ")
        self.mobil = input("Enter Mobil Number : ")
        self.email = input("Enter Email ID : ")
    def customer_info(self):
        print("_____Person Details_____")
        print("Name       :  ",self.name)
        print("Address    :  ",self.address)
        print("Mobil      :  ",self.mobil)
        print("Email-ID   :  ",self.email)
class Product:
    def __init__(self):
        self.product_name = ""
        self.price = ""
        self.description = ""
    def product_data(self):
        self.product_name = input("Enter the Product Name : ")
        self.price = int(input("Enter the price  : "))
        self.description = input("Enter the Designation  :  ")
    def product_info(self):
        print("_____Salary Details______")
        print("Product Name  : ",self.product_name)
        print("Price         : ",self.price)
        print("Description   : ",self.description)
class Order(Customer, Product):
    def __init__(self):
        self.order_id = ""
        self.quantity = ""
        self.total_price = ""
        self.order_date = ""
    def order_data(self):
        self.order_id = input("Enter the Order ID : ")
        self.quantity = input("Enter the Quantity  : ")
        self.total_price = input("Enter Total Price : ")
        self.order_date = input("Enter Order date  : ")
    def order_info(self):
        print("_____Employee Details______")
        print("Order ID    :  ",self.order_id)
        print("Quantity    :  ",self.quantity)
        print("Total Price :  ",self.total_price)
        print("Order date  :  ",self.order_date)

obj1 = Order()
obj1.order_data()
obj1.product_data()
obj1.customer_data()

obj1.order_info()
obj1.product_info()
obj1.customer_info()