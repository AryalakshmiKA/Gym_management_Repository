# 1. Write a program to remove duplicate elements from a list while preserving
# the original order.

list1 = [12,4,55,63,12,8,4,77,55]
unique_list = []
for item in list1:
    if item not in unique_list:
        unique_list.append(item)
print("Original List :",list1)
print("Unique List after removing duplicate elements :", unique_list)