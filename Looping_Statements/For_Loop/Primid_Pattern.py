rows = int(input("Enter the rows : "))
for i in range(rows):                      # Outer loop Control rows
    for s in range(rows - i):              # Print Space for alignment
        print(" ", end=" ")
    for j in range(2 * i + 1):             # Print Stars
        print("*", end=" ")
    print( )                               # Move to Next Line
