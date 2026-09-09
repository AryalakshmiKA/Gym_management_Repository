# 6. Write a program to rotate a list to the left by k positions

list1 = [10,20,30,40,50]

k = 2
if not list1:
    print("List Empty")
k = k % len(list1)
new_list = list1[k:] + list1[:k]

print("Original List     :",list1)
print("Left Rotated List :",new_list)