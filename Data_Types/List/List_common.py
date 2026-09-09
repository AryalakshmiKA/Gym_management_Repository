# Python program to find the common element in two List/array


a1 = [1,2,3,4,5,6]
a2 = [7,8,9,2,3,5]
common = []
for i in range(len(a1)):
    for j in range(len(a2)):
        if a1[i] == a2[j] and a1[i] not in common:
            common.append(a1[i])
print(common)