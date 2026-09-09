# Write a program to find all substrings of a given string without using built-in
# libraries.

text = input("Enter the String  :")
substr = []
str_len = len(text)
for start in range(str_len):
    for end in range(start + 1, str_len + 1):
        current_str = text[start:end]
        substr.append(current_str)
print("All String  :",substr)
print("Total Count :",len(substr))