#Write a program to reverse each word in a sentence without changing the
#order of the words.


s = input("Enter the String :")
words = s.split()
print(words)
a = []
for word in words:
    a.append(word[::-1])
res = " ".join(a)
print(res)
