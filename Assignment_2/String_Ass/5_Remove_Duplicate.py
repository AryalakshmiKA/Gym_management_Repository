# Write a program to remove all duplicate characters from a string while
# preserving their first occurrence.

str1 = input("Enter the String  :")
print("Original String                  : ",str1)
result_str = ""
for char in str1:
    if char not in result_str:
        result_str += char
print("String after removing Duplicates : ",result_str)