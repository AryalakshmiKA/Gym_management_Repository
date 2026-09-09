rows = int(input("Enter the rows : "))
for i in range(rows):
    for s in range(i):
        print(" ", end=" ")
    for j in range(2 * (rows - i) - 1):
        print("*", end=" ")
    print()