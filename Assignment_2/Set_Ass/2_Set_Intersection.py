# 2. Write a program to find the intersection of two sets without using the
# intersection() method.

set_a = {1,2,3,4,5,8}
set_b = {3,4,5,6,7,9}

print("Set 1 : ",set_a)
print("Set b : ",set_b)

set_inter = []
for i in set_a:
    if i in set_b:
        set_inter.append(i)
print("Intersection of two Sets : ",set(set_inter))

