def count_digits(num):
    count = 0
    for i in num:
        if i.isnumeric():
            count += 1
    return count

digit = input("Enter the Digits :")
result = count_digits(digit)
print("Count of Digits :",result)
