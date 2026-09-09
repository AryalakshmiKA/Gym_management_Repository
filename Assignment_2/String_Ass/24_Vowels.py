# 24. Write a program to print all words in a sentence that start with a vowel.

str1 = input("Enter the String : ")
s = str1.split()
print("The Original List : ",s)
res = []
vowels = "aeiouAEIOU"

for word in s:
    flag = False

    for sub in vowels:
        if word.startswith(sub):
            flag = True
            break

    if flag:
        res.append(word)

print("The Extracted words : ",str(res))