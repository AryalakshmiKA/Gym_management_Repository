# 3. Pyramid pattern in Python

n = int(input("Enter the Row Count : "))
for i in range(n):
    for s in range(n - i):
        print(" ", end=" ")
    for j in range(2 * i + 1):
        print("*", end=" ")
    print()