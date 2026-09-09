# 11. Write a program to count the occurrence of a given element in a tuple without
# using the count() method.

tuple1 = (10,8,5,2,10,8,5,10)
print("Original Tuple :",tuple1)
search = int(input("Enter the Element : "))
count = 0
for item in tuple1:
    if item == search:
        count += 1
print("The Count of ",search,"in the tuple is",count)