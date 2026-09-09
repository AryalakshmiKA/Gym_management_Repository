# 5. Write a program to remove duplicate elements from a list using a set


orgl_list = [10,20,10,30,40,20,50,30]
print("Original List :",orgl_list)

seen = set()
uniq_list = []

for item in orgl_list:
    if item not in seen:
        uniq_list.append(item)
        seen.add(item)

print("Duplicates Removed List :",uniq_list)