# Write a program to find the frequency of each character in a string.
text = input("Enter the String :")
frequency_dict = { }
for char in text:
    if char in frequency_dict:
        frequency_dict[char] += 1
    else:
        frequency_dict[char] = 1
print(frequency_dict)