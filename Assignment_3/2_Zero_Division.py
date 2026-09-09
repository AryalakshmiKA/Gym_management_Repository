def Division(x, y):
    try:
        result = x / y
        print("Result = ",result)
    except ZeroDivisionError:
        print("Error : You cannot divide a number by Zero. ")


num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter Number 2 : "))
Division(num1, num2)
