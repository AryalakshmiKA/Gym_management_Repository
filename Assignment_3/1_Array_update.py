import array as arr

numbers = arr.array("i",[10,20,30,40])
print("Original Array : ",numbers)

new_item = int(input("Enter a New Number tobe Updated : "))
numbers.append(new_item)

print("Updated Array : ",numbers)

