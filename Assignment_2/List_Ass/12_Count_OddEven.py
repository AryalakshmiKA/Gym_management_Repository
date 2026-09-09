# 12. Write a program to count the number of even and odd numbers in a list.

list1 = [1,23,44,55,67,22]
even = 0
odd = 0

for num in list1:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Original List          :",list1)
print("Count of Even Numbers  :",even)
print("Count of Odd Numbers   :",odd)