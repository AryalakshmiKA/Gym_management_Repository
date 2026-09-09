# 9. Write a program to find the missing number from a list containing numbers
# from 1 to N.

my_list = [1,2,4,6,9,10]

max = my_list[0]
min = my_list[0]

for i in my_list:
    if i > max:
        max = i

for i in my_list:
    if i < min:
        min = i

missing_list = []

for num in range(min, max + 1):
    if num not in my_list:
        missing_list.append(num)
print("Original List                         :",my_list)
print("Missing Numbers in the Original List  :",missing_list)