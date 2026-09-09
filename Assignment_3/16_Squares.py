def sum_squares(n):
    sum_total = 0
    for i in range(1,n + 1):
        sum_total += i * i
    return sum_total

num = int(input("Enter the Limit : "))
if num < 1:
    print("Please enter a positive natural number.")
else:
    result = sum_squares(num)
    print("The sum of squares of first ",num,"natural number is ",result)