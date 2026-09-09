# Write a program to find the longest word in a sentence.

str1 = input("Enter the Sentence : ")
longest = ""
max_len = 0
words = str1.split()
print(words)
for word in words:
    length = 0
    for char in word:
        length += 1
    if length >max_len:
        max_len = length
        longest = word
print("Longest word is :",longest)