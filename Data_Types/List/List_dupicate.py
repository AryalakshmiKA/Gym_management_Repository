# Python program to find the duplicate element in a List


array1 =[10,2,12,23,21,10,5,2,12,30]
new_list = []
print("Number of elements :",len(array1))
for i in range(len(array1)):
    for j in range(i+1,len(array1)):
        if array1[i] == array1[j] and array1[i] not in new_list:
            new_list.append(array1[i])
print(new_list)
