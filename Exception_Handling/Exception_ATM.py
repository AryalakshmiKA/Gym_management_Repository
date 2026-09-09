def atm():
    correct_pin = 1234
    balance = 5000

    try:
        pin = int(input("Enter Pin Number :"))
        if pin != correct_pin:
            raise ValueError("Wrong Pin Number")
        print("Login Successfil...!")

        amount = int(input("Enter Amount to withdraw : "))
        if amount > balance:
            raise ValueError("Insufficient Balance..!")
        balance -= amount
        print("Withdrawal Successful   !")
        print("Remaining balance : ",balance)

    except Exception as e:
        print("Error : ",e)
    finally:
        print("Thank You for Your Time....!")
atm()