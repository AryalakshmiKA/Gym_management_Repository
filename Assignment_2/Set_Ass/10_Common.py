# 10. Write a program to find the common elements among three sets.

set1 = {1, 5, 10, 20, 40, 80}
set2 = {6, 7, 20, 80, 100}
set3 = {3, 4, 15, 20, 30, 70, 80}

print("Set 1 :",set1)
print("Set 2 :",set2)
print("Set 3 :",set3)


common_elements = set1.intersection(set2, set3)
print("Common elements :", common_elements)
