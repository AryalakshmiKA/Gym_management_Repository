# 11. Write a program to find the largest and smallest elements in a list without
# using max() and min().

number = [34,12,89,5,67,21,90,2]
min = number[0]
max = number[0]

for num in number[1:]:
    if num < min:
        min = num
    elif num > max:
        max = num

print("Original List",number)
print("Largest Element in the list   :",max)
print("Smallest Element in the list  :",min)