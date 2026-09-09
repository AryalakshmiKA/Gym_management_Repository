# Write a program to group a list of strings into anagram groups.
from traceback import print_tb

list1= ['cat', 'dog', 'fired', 'god', 'pat', 'tap', 'fried', 'tac']
print("Original List : \n",list1)

group = {}


for string in list1:
    sorted_string = str(sorted(string))

    if sorted_string in group:
        group[sorted_string].append(string)
    else:
        group[sorted_string] = [string]

print("Anagram Group from the List :\n",list(group.values()))