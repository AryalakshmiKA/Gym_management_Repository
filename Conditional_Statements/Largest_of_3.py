num1 = int(input("Enter the First Number : "))
num2 = int(input("Enter the Second Number : "))
num3 = int(input("Enter the Third Number : "))

if num1 > num2 and num1 > num3:
    print(num1," is Greater....")
elif num2 > num1 and num2 > num3:
    print(num2," is Greter....")
else:
    print(num3," is Greter....")
