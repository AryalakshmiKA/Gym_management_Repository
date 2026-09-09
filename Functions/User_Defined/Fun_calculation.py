def addition(a,b):
    return a + b
def subtraction(a,b):
    return a - b
def multiply(a,b):
    return a * b
def division(a,b):
    return a // b

num1 = int(input("Enter the First Number    :"))
num2 = int(input("Enter the Second Number   :"))
print("Sum of Two Numbers         :",addition(num1,num2))
print("Difference of Two Numbers  :",subtraction(num1,num2))
print("Product of Two Numbers     :",multiply(num1,num2))
print("Division of Two Numbers    :",division(num1,num2))