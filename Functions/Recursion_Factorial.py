def factorial(n):
    if n ==0:
        return 1
    else:
        return n * factorial(n - 1)

num1 = int(input("Enter the Number  :"))
result = factorial(num1)
print("Factorial of ",num1,"is : ",result)