# 13. Write a program to convert a list into a set and then back into a list without
# duplicate elements.


original_list = [1, 2, 2, 3, 4, 4, 4, 5, 1, 6]
print("Original List:", original_list)

unique_set = set(original_list)
print("Converted to Set:", unique_set)

deduplicated_list = list(unique_set)
print("Back to List (No Duplicates):", deduplicated_list)