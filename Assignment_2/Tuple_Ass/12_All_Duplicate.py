# 12. Write a program to find all duplicate elements in a tuple.

tuple1 = (10,20,60,10,30,20)
dupli = []
seen = []
for num in tuple1:
    if num in seen:
        dupli.append(num)
    else:
        seen.append(num)
dupl_tuple = tuple(dupli)
print("Original Tuple     :",tuple1)
print("Duplicate Elements :",dupl_tuple)
