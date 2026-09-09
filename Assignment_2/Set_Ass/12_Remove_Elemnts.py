# 12. Write a program to remove all elements from a set one by one.

fruits = {"apple", "banana", "cherry", "date"}
print("Original set : ",fruits)

while fruits:
    removed_item = fruits.pop()
    print("Removed : ", removed_item,"Remaining Set : ",fruits)

print("Final set is empty.")