# Write a program to capitalize the first letter of each word without using the
# title() method.

str1 = input("Enter the String  :")
words = str1.split()
capital = []
for word in words:
    x = word.capitalize()
    capital.append(x)
new_str = " ".join(capital)
print("Capitalized String :",new_str)
