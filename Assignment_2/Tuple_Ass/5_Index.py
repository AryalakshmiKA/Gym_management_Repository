# 5. Write a program to find the index of a given element without using the index()
# method.

items = ("Apple","Banana","Cherry","Dates","Mango")
print("Original Tuple :",items)
target = input("Enter the Element to Search : ")
current_index = 0
search_index = -1

for num in items:
    if num == target:
        search_index = current_index
        break
    current_index += 1

if search_index != -1:
    print("Element found at index :",search_index)
else:
    print("Element no found in the tuple.")

