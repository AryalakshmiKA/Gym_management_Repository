class Bank():
    def __init__(self):
        self.bank_name = ""
        self.branch = ""
        self.ifsc = ""
        self.manager_name = ""
        self.contact_no = ""
    def bank_data(self):
        self.bank_name = input("Enter Bank Name : ")
        self.branch = input("Enter Branch Name : ")
        self.ifsc = input("Enter IFSC Code : ")
        self.manager_name = input("Enter Manager Name : ")
        self.contact_no = input("Enter Contact No : ")
    def bank_info(self):
        print("_____Bank Details____")
        print("Bank Name     : ",self.bank_name)
        print("Branch        : ",self.branch)
        print("IFSC Code     : ",self.ifsc)
        print("Manager Name  : ",self.manager_name)
        print("Contact.No    : ",self.contact_no)

class Savings_Account(Bank):
    def __init__(self):
        self.ac_no = ""
        self.customer_name = ""
        self.balance = ""
        self.mobil = ""
        self.interest = ""
    def account_data(self):
        self.ac_no = input("Enter Account.No : ")
        self.customer_name = input("Enter Customer Name : ")
        self.balance = input("Enter Balance : ")
        self.mobil = input("Enter Mobil Number : ")
        self.interest = input("Enter Interest Rate : ")
    def account_info(self):
        print("_____Savings Account Details____")
        print("Account No       : ", self.ac_no)
        print("Customer Name    : ", self.customer_name)
        print("Balance          : ", self.balance)
        print("Mobile Number    : ", self.mobil)
        print("Interest Rate    : ", self.interest)

class Current_Account(Bank):
    def __init__(self):
        self.current_ac_no = ""
        self.curr_customer_name = ""
        self.curr_balance = ""
        self.curr_business_Name = ""
    def curr_account_data(self):
        self.current_ac_no = input("Enter Account.No : ")
        self.curr_customer_name = input("Enter Customer Name : ")
        self.curr_balance = input("Enter Balance : ")
        self.curr_business_Name = input("Enter Business Name : ")
    def curr_account_info(self):
        print("_____Savings Account Details____")
        print("Account No       : ", self.current_ac_no)
        print("Customer Name    : ", self.curr_customer_name)
        print("Balance          : ", self.curr_balance)
        print("Business Name    : ", self.curr_business_Name)

class Loan_Account(Bank):
    def __init__(self):
        self.loan_ac_no = ""
        self.loan_customer_name = ""
        self.loan_amount = ""
        self.loan_interest = ""
    def loan_account_data(self):
        self.loan_ac_no = input("Enter Account.No : ")
        self.loan_customer_name = input("Enter Customer Name : ")
        self.loan_amount = input("Enter Loan Amount : ")
        self.loan_interest = input("Enter Interest Rate : ")
    def loan_account_info(self):
        print("_____Savings Account Details____")
        print("Account No       : ", self.loan_ac_no)
        print("Customer Name    : ", self.loan_customer_name)
        print("Loan Amount      : ", self.loan_amount)
        print("Interest Rate    : ", self.loan_interest)


obj1 = Savings_Account()
obj1.account_data()
obj1.account_info()
obj1.bank_data()
obj1.bank_info()

obj2 = Current_Account()
obj2.curr_account_data()
obj2.curr_account_info()
obj2.bank_data()
obj2.bank_info()

obj3 = Loan_Account()
obj3.loan_account_data()
obj3.loan_account_info()
obj3.bank_data()
obj3.bank_info()