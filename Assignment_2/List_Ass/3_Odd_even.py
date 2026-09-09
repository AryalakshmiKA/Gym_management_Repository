# 3. Write a program to separate even and odd numbers into two different lists.

list1 = [11,22,33,44,55,66,77,88,99]
even = []
odd = []
even = [num for num in list1 if num % 2 == 0]
odd = [num for num in list1 if num % 2 != 0]
print("Original List              :",list1)
print("Even Numbers from the list :",even)
print("Odd Numbers from the list  :",odd)