# 14.Write a program to check whether two sets contain exactly the same elements.

set_a = {1, 2, 3, 4}
set_b = {4, 3, 2, 1}
set_c = {1, 2, 3, 5}

print("Set A : ",set_a)
print("Set B : ",set_b)
print("Set C : ",set_c)
print("Are set_a and set_b equal?  : ",set_a == set_b)
print(f"Are set_a and set_c equal? : ",set_a == set_c)

is_identical = len(set_a.symmetric_difference(set_b)) == 0
print(f"Are they identical via symmetric difference? {is_identical}")