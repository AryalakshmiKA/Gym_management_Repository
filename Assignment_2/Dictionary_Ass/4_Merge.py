# 4. Write a program to merge two dictionaries. If a key exists in both, add their
# values.

dict1 = {'a':10,'b':30,'c':20}
dict2 = {'a':40,'d':60,'c':20}

merge_dict = dict1.copy()

for key,value in dict2.items():
    if key in merge_dict:
        merge_dict[key] += value
    else:
        merge_dict[key] = value
print(merge_dict)