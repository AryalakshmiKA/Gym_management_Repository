# 22. Write a program to remove all spaces from a string without using the replace()
# method.

str1 = input("Enter the String : ")
result = "".join(str1.split())

print("String Without Function : ",str1)