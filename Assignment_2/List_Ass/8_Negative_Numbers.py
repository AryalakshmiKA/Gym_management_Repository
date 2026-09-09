# 8. Write a program to remove all negative numbers from a list.

list1 = [-1,9,-8,2,-3,7,-6,4,-5]

postive_list = []
for num in list1:
    if num < 0:
        continue
    else:
        postive_list.append(num)
print("Original List                        :",list1)
print("List After Removing Negative Numbers : ",postive_list)