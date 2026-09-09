# 2. Inverted Right-Angled Triangle in Python

n = int(input("Enetr the limit  :"))
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()