# 13. .Write a program to convert a tuple into a list, sort it, and convert it back into
# a tuple.

org_tuple = (42,11,90,4,75,23)
print("Orginal Tuple  :",org_tuple)

list1 = list(org_tuple)
list1.sort()

sort_tuple = tuple(list1)
print("Sorted Tuple  :",sort_tuple)