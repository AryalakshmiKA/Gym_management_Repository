# 12. Number Right-Angled Triangle pattern in Python
n = int(input("Enter the limit  : "))
for i in range(1,n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()