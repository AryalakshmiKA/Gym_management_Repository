# 3. Write a program to count the frequency of each word in a sentence using a
# dictionary.

str1 = input("Enter the String :")

count_str = {}
for s in str1:
    if s in count_str:
        count_str[s] += 1
    else:
        count_str[s] = 1
print("Frequency of each word : ",count_str)