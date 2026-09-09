# Write a program to check whether a string is a palindrome without using
# slicing.

str1 = input("Enter the String  :")
if str1 == str1[::-1]:
    print(str1, "is Palindrome")
else:
    print(str1,"is not Palindrome")