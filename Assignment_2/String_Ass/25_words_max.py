# 25. Write a program to find the word with the maximum number of characters in
# a sentence.

sentence = input("Enter the Sentence : ")
clean_sentence = "".join(char for char in sentence if char.isalnum() or char.isspace())
word = clean_sentence.split()

if not word:
    print("No Words Found")
long_word = max(word,key=len)
print("Longest Word : ",long_word)

