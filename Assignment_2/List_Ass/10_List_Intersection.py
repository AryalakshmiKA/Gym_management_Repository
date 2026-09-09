# 10. Write a program to find the intersection of two lists without using sets

list1 = [1,2,2,3,4]
list2 = [2,3,5,6]

intersection = []

for num in list1:
    if num in list2 and num not in intersection:
        intersection.append(num)
print("Original List1    :",list1)
print("Original List2    :",list2)
print("Intersection List :",intersection)