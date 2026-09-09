# 5. Write a program to merge two sorted lists into a single sorted list.

list1 = [1,3,5,7]
list2 = [2,4,6,8,10]

i = 0
j = 0

merge_list = []

while i < len(list1) and j < len(list2):
    if list1[i] <= list2[j]:
        merge_list.append(list1[i])
        i += 1
    else:
        merge_list.append(list2[j])
        j += 1
merge_list.extend(list1[i:])
merge_list.extend(list2[j:])
print("First List         :",list1)
print("Second List        :",list2)
print("Merged Sorted List :",merge_list)
