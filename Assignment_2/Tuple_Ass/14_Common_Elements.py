# 14. Write a program to compare two tuples and display the common elements.

tuple1 = (10,20,30,40,50)
tuple2 = (30,50,60,70,10)

com_element = []
for item in tuple1:
    if item in tuple2:
        if item not in com_element:
            com_element.append(item)
result_tuple = tuple(com_element)
print("Original Tuple 1  :",tuple1)
print("Original Tuple 2  :",tuple2)
print("Common Elements in the Tuple  :",result_tuple)