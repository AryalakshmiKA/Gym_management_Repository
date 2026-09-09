# 3. Write a program to find the difference between two sets

set_a = {10,20,30,40,50}
set_b = {30,40,50,60,70}

print("Set 1 : ",set_a)
print("Set 2 : ",set_b)

diff_1 = set_a.difference(set_b)
diff_2 = set_b.difference(set_a)

print("Set difference between set 1 and set 2 : ",diff_1)
print("Set difference between set 2 and set 1 : ",diff_2)