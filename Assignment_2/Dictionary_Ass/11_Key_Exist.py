# 11. Write a program to check whether a given key exists in a dictionary.

dict1 = {'name': 'Athul','age': 25,'email': 'athul@123','place':'pala'}
print("Existing Dictionary  :",dict1)
item = input("Enter the Key to be Search : ")

if item in dict1.keys():
    print("Search Success!")
else:
    print("Search not Success")