# 2. Write a program to merge two tuples without using the + operator.

tuple1 = (10,20,30)
tuple2 = ("one","two","three")

print("Original Tuple 1 :",tuple1)
print("Original Tuple 2 :",tuple2)
list1 = list(tuple1)
list2 = list(tuple2)
list1.extend(list2)
tuple1 = tuple(list1)
print("Merged Tuple  : ",tuple1)