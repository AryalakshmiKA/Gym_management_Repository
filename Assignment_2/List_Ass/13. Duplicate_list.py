# 13. Write a program to create a new list containing only the duplicate elements
# from a given list.

my_list = [1,3,1,4,5,7,4,5,1,3,2,8,9]

list_dup = []
new_list = []
for num in my_list:
    if num in new_list:
        if num not in list_dup:
            list_dup.append(num)
    else:
        new_list.append(num)

print("Original List                   :",my_list)
print("Duplicate Elements in the List  :",list_dup)