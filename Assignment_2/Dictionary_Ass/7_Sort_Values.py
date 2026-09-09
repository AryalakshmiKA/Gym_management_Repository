# 7. Write a program to sort a dictionary by its values.

my_dict = {'banana': 8, 'apple':2, 'cherry': 4,'dates': 6}

sort_value = dict(sorted(my_dict.items(), key = lambda item: item[1]))

print("Original Dictionary              :",my_dict)
print("Dictionary Sorted by its Values  :",sort_value)