# 9. Write a program to create a dictionary from two lists (one containing keys
# and the other values).

keys = ['name','age','place']
value = ['Ammu',20,'Kochi']
print("Keys List    :",keys)
print("Values List  :",value)
comb_dict = {}
index = 0
for key in keys:
    comb_dict[key] = value[index]
    index += 1

print("Dictionary created from the two list :",comb_dict)
