# 12.Write a program to create a dictionary of numbers from 1 to 10 and their
# squares.

squar = {}
print("Squares of the Number 1 to 10 : ")
for i in range(1, 11):
    if i > 0:
        squar[i] = i ** 2
print(squar)