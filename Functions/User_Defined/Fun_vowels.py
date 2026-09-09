# Print The count of vowels in a string


def count_vowels(str1):
    str2 = str1.lower()
    count = 0
    for char in str2:
        if char == "a" or char == "e" or char == "i" or char == "u" or char =="o":
            count += 1
    return count

text = input("Enter the String :")
result = count_vowels(text)
print("No.of Vowels in the string :",result)