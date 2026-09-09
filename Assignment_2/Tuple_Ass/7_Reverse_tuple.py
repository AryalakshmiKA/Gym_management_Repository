# 7. Write a program to reverse a tuple without using slicing

org_tuple = (10,20,30,40,50)

n = len(org_tuple)
rev = []
for i in range(n-1,-1,-1):
    rev.append(org_tuple[i])
rev_tuple = tuple(rev)

print("Original Tuple :",org_tuple)
print("Reversed Tuple :",rev_tuple) 