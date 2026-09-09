# 13. Inverted Number Right-Angled Triangle pattern in Python

n = int(input("Enetr the limit  :"))
for i in range(n+1, 1, -1):
    for j in range(1, i):
        print(j, end=" ")
    print()