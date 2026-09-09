# 5. Diamond pattern in Python

n  = int(input("Enetr the Row Count :"))
for i in range(n):
    for s in range(n - i):
        print(" ", end=" ")
    for j in range(2 * i + 1):
        print("*", end=" ")
    print()
n -= 1
for i in range(n):
    for s in range(i + 2):
        print(" ", end=" ")
    for j in range(2 *  (n - i)- 1):
        print("*", end=" ")
    print()