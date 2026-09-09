def addition(a,b):
    return a + b
def subtraction(a,b):
    return a - b
def multiply(a,b):
    return a * b
def division(a,b):
    return a // b

print(" A. Addition \n B. Subtraction \n C. Multiplication \n D. Division")
num1 = int(input("Enter the First Number    :"))
num2 = int(input("Enter the Second Number   :"))
ch = input("Enter your Choice :")

if ch == "A" or ch == "a":
    print("Sum of Two Numbers         :",addition(num1,num2))
elif ch == "B" or ch == "b":
    print("Difference of Two Numbers  :",subtraction(num1,num2))
elif ch == "C" or ch == "c":
    print("Product of Two Numbers     :",multiply(num1,num2))
elif ch == "D" or ch == "d":
    print("Division of Two Numbers    :",division(num1,num2))
else:
    print("You Entered an Invalid Option")