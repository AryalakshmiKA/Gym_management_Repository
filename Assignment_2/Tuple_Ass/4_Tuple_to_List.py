# 4. Write a program to convert a tuple into a list and remove duplicate elements

org_tuple = (10,20,30,40,20,50,40)
unique_list = []
for num in org_tuple:
    if num not in unique_list:
        unique_list.append(num)
print("Original Tuple : ",org_tuple)
print("List with out Duplicates :",unique_list)