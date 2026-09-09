# Python program to find the smallest element in a List


list1 = [11,20,35,4,50,22,32,100,0]
print(list1)
small = list1[0]
for i in range(len(list1)):
    if list1[i] < small:
        small = list1[i]
print("Largest of the List :", small)
