# 11.Hollow Diamond pattern in Python Rows = 5

n = int(input("Enter the number of rows : "))
for i in range(1, n + 1):
    for s in range(1, n - i + 1):
        print(" ", end="")
    for j in range(1, 2 * i):
        if j == 1 or j == (2 * i - 1):
            print("*", end="")
        else:
            print(" ", end="")
    print()
for i in range(n - 1, 0, -1):
    for s in range(1, n - i + 1):
        print(" ", end="")
    for j in range(1, 2 * i):
        if j == 1 or j == (2 * i - 1):
            print("*", end="")
        else:
            print(" ", end="")
    print()
