# 4. Inverted Pyramid pattern in Python

n = int(input("Enter the row Count  :"))
for i in range(n):
    for s in range(i):
        print(" ", end=" ")
    for j in range(2 * (n - i) - 1):
        print("*", end=" ")
    print()