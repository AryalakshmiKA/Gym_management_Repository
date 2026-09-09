# Write a program to find the first non-repeating character in a string using a
# dictionary.

str1 = input("Enter the String : ")
text = {}
for char in str1:
    text[char] = text.get(char,0)+1
for char in str1:
    if text[char] == 1:
        result = char
print("The first non-repeating character in ",str1,"is",result)
