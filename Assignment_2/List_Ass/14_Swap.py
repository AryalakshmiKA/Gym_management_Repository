# 14. .Write a program to swap the first and last elements of a list

list1 = [10,20,30,40,50]
print("Original List  :",list1)
n = len(list1)

if n >= 2:
    temp = list1[0]
    list1[0] = list1[-1]
    list1[-1] = temp

print("Swaped List    :",list1)
