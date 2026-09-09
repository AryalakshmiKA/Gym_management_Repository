# 1. Write a program to find the union of two sets without using the union()
# method.

set_a = {1,2,3,4,4}
set_b = {3,4,5,6,7}

print("Set 1 : ",set_a)
print("Set 2 : ",set_b)

set_union = set_a.copy()

for element in set_b:
    set_union.add(element)

print("Union of Two Sets : ",set_union)
