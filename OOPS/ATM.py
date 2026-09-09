class Atm:
    def __init__(self):
        self.account_number = ""
        self.account_holder_name = ""
        self.balance = 0
    def create_account(self):
        print("_____Enter Your Details____")
        self.account_number = input("Enter the Account Number : ")
        self.account_holder_name = input("Enter Account Holder Name : ")
        self.balance = float(input("Enter your Initial Balance : "))
        print("Account Creates Successfully......")
    def deposit(self):
        print("_____Deposit_____")
        deposit_amt = float(input("Enter the Deposit Amount : "))
        self.balance += deposit_amt
        print("Deposited Successfully....")
    def withdraw(self):
        print("_____Withdraw______")
        withdraw_amt = float(input("Enter the Amount you have to Withdraw : "))
        if withdraw_amt <= self.balance:
            self.balance -= withdraw_amt
            print("Amount Withdraw Successfully...")
        else:
            print("Insufficient Balace ....")
    def balance_enquire(self):
        print("____Balance Enquire_____")
        print("Current Balance : ",self.balance)
    def mini_statement(self):
        print("_____Mini Statement_____")
        print("Account Number        :  ",self.account_number)
        print("Account Holder Name   :  ",self.account_holder_name)
        print("Current Balance       :  ",self.balance)


obj = Atm()
while True:
    print("*****_WELCOME_*****")
    print("1. Create Account \n"
      "2. Deposit\n"
      "3. Withdraw\n"
      "4. Balance Enquire\n"
      "5. Mini Statement\n"
       "6. Exit")
    ch = int(input("Enter Your Option : "))
    if ch == 1:
        obj.create_account()
    elif ch == 2:
        obj.deposit()
    elif ch == 3:
        obj.withdraw()
    elif ch == 4:
        obj.balance_enquire()
    elif ch == 5:
        obj.mini_statement()
    elif ch == 6:
        print("Thanks fro Using ATM....")
        break
    else:
        print("Invalid.....")
        break



