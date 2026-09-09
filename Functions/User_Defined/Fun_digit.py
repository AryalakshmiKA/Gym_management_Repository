def count_digits(num):
    count = 0
    while num != 0:
        count += 1
        num //= 10
    return count

digit = int(input("Enter the Digits :"))
result = count_digits(digit)
print("Count of Digits :",result)