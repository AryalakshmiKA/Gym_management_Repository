# Write a program to determine whether one string is a rotation of another
# string.

str1 = input("Enter the First String  :")
str2 = input("Enter the Second String :")

rotation = False
if len(str1) == len(str2):
    d_str = str1 + str1
    for i in range(len(d_str) - len(str2) + 1):
        match = True
        for j in range(len(str2)):
            if d_str[i + j] != str2[j]:
                match = False
                break
            if match:
                rotation = True
                break
if rotation:
    print("Is",str2,"a rotation of ",str1)