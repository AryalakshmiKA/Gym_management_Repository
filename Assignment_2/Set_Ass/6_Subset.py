# 6. Write a program to check whether one set is a subset of another.

set_a = {1, 2, 3}
set_b = {1, 2, 3, 4, 5}
set_c = {1, 2, 6}

print("Set A :",set_a)
print("Set B :",set_b)
print("Set C :",set_c)

print(f"Is Set A is the Subset of Set B? {set_a <= set_b}")
print(f"Is Set C is the Subset of Set B? {set_c <= set_b}")