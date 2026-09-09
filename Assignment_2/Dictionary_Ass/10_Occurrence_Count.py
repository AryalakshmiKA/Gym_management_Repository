# 10. Write a program to count the number of occurrences of each character in a
# string using a dictionary.

text = input("Enter the String : ")
freq = {}

for i in text:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print("Count of Characters in the Sting",freq)