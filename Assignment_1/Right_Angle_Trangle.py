# 1. Right-Angled Triangle Pattern in Python


n = int(input("Enter the limit  : "))
for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print()