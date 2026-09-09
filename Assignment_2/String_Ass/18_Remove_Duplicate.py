# Write a program to remove all duplicate words from a sentence while
# maintaining their original order.

text = input("Enter the Sentence  : ")
words = text.split()
unique_word = []
for word in words:
    if word not in unique_word:
        unique_word.append(word)
result = " ".join(unique_word)
print("Text After Remove All Duplicate  : ",result)