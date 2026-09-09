# 13. Write a program to update the value of a key only if the key exists in the
# dictionary.

data = {"name": 'Paru','Role': 'Coder','salary': 30000}
print("Existing Data : ",data)

key = input("Enter the key to be Updated : ")
value = input("Enter the new value       : ")

if key in data:
    data[key] = value
    print("Update Successfully")
else:
    print("Update Cannot Possible, Key not Exist")

print("Updated Data :  ",data)