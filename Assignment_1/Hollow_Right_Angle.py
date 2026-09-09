# 7. Hollow Right-Angled Triangle in Python
size = int(input("Enter the Size :"))
for i in range(1, size+1):
    for j in range(1, i + 1):
        if j == 1 or j == i or i == size:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()