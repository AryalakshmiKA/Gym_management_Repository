rows = int(input("Enter the row value : "))
for i in range(rows, 0, -1):       # outer loop for rows
    for j in range(i):   # inner loop for columns
        print(j,end=" ")
    print()