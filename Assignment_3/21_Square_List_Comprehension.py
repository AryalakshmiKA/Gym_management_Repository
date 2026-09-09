def squares(n):
    return [x ** 2 for x in range(1, n + 1)]

num = int(input("Enter the Limit : "))
result = squares(num)
print("Square of numbers : ",result)