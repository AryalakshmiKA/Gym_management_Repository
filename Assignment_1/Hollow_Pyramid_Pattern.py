# 9. Hollow Pyramid pattern in Python
n = int(input("Enter the Row Count : "))
for i in range(n):
    for s in range(n - i):
        print(" ", end=" ")
    for j in range(2 * i + 1):
        if j == 0 or j == 2 * i or i == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()