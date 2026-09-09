# 21. Write a program to count the number of uppercase and lowercase letters in a
# string.

str_input = input("Enter the String : ")
upper_count = 0
lower_count = 0

for char in str_input:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1
print("Count of Upper Case Letters : ",upper_count)
print("Count of Lower Case Letters : ",lower_count)