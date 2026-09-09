# Write a program to check whether two strings are anagrams.

str1 = input("Enter String 1 :")
str2 = input("Enter String 2 :")
clean_str1 = str1.replace(" ", "").lower()
clean_str2 = str2.replace(" ", "").lower()
if sorted(clean_str1) == sorted(clean_str2):
    print(f"'{str1}' and '{str2}' are anagrams!")
else:
    print(f"'{str1}' and '{str2}' are NOT anagrams.")