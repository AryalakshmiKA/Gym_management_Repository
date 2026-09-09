# Write a program to replace all occurrences of a given word with another word
# in a sentence without using the replace() method.


text = input("Enter the Text : ")
old_text = input("Enter the old word to be replace :")
new_text = input("Enter the New word :")

words = text.split()
modified_word = []
for word in words:
    if word == old_text:
        modified_word.append(new_text)
    else:
        modified_word.append(word)
result = " ".join(modified_word)
print(result)