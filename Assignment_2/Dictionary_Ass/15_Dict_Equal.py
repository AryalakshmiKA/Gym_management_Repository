# 15. Write a program to check whether two dictionaries are equal.

dict_a = {'name':'Akhil','age':25,'place':'vipin'}
dict_b = {'name':'malu','age': 62,'city':'kochi'}
dict_c = {'place':'vipin','name':'Akhil','age':25}

print("Dictionary A : ",dict_a)
print("Dictionary B : ",dict_b)
print("Dictionary C : ",dict_c)
if dict_a == dict_b:
    print("\nDictionary A is Equal to Dictionary B")
else:
    print("\nDictionary A is Not Equal to Dictionary B")

if dict_a == dict_c:
    print("\nDictionary A is Equal to Dictionary C")
else:
    print("\nDictionary A is Not Equal to Dictionary C")