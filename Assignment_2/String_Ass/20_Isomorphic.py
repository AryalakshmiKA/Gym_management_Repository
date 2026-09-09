# Write a program to determine whether two strings are isomorphic.

s1 = input("Enter first string  : ")
s2 = input("Enter second string : ")

n = len(s1)
isom = 0
for i in range(n):
    c1 = s1[i]
    c2 = s1[i]
    for j in range(n):
        if s1[j] == c1 and s2[j] != c2:
            isom = 0
        elif s2[j] == c2 and s1[j] != c1:
            isom = 0
        else:
            isom = 1
if isom < 1:
    print("Not Isomorphic")
else:
    print("Isomorphic")


