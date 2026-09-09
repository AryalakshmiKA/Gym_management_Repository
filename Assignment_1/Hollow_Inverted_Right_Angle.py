# 8. Hollow Inverted Right-Angled Triangle Pattern
size = int(input("Enter the Size :"))
for i in range(size,0,-1):
    for j in range(1, i + 1):
        if j == 1 or j == i or i == size:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()