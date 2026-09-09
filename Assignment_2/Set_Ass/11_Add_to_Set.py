# 11. Write a program to add multiple elements to a set without using the update()
# method.

my_set = {1, 2, 3}
print("Original Set : ",my_set)
new_elements = [4, 5, 6, 2, 1]
print("Elements to Update :",new_elements)
for element in new_elements:
    my_set.add(element)

print("Updated set:", my_set)
