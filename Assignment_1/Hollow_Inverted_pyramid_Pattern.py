# 10. Hollow Inverted Pyramid Pattern in Python

n = int(input("Enter the Row Count : "))
for i in range(n, 0, -1):
    for s in range(n - i):
        print(" ", end=" ")
    for j in range(1, (2 * i)):
        if i == n or j == 1 or j == (2 * i - 1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


