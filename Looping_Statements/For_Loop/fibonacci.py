limit = int(input("Enter the limit : "))
num1 = 0
num2 = 1
print("Fibonacci Series :")
print(num1)
print(num2)
for i in range(3,limit + 1):
    sum = num1 + num2
    num1 = num2
    num2 = sum
    print(sum)
