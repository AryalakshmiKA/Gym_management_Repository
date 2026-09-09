# Python program to find the largest element in a List


list1 = [11,20,35,4,50,22,32,100]
print(list1)
largest = list1[0]
for i in range(len(list1)):
    if list1[i] > largest:
        largest = list1[i]
print("Largest of the List :", largest)
