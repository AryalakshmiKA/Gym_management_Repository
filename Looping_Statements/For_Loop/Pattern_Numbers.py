rows = int(input("Enter the row value : "))
for i in range(rows):       # outer loop for rows
    for j in range(1, i +1):   # inner loop for columns
        print(j,end=" ")
    print()