# 7. Write a program to check whether two sets are disjoint.

set_a = {1, 2, 3}
set_b = {4, 5, 6}
set_c = {3, 7, 8}

print("Set A : ",set_a)
print("Set B : ",set_b)
print("Set C : ",set_c)

if set_a.isdisjoint(set_b):
    print("The sets are disjoint (no common elements).")
else:
    print("The sets are not disjoint (they have common elements).")

print(f"Are set_a and set_c disjoint? {set_a.isdisjoint(set_c)}")