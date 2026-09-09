# 23. Write a program to check whether two strings are equal without using the ==
# operator.


str1 = input("Enter string 1 : ")
str2 = input("Enter string 2 : ")

if len(str1) != len(str2):
    print("String 1 not Equal to String 2")

for i in range(len(str1)):
    if str1[i] != str2[i]:
        print("String 1 not Equal to String 2")

print("String 1 is equal to String 2")