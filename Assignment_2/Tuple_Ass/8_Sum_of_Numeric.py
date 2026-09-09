# 8. Write a program to find the sum of all numeric elements in a tuple.

tuple1 = ("Apple",2,4,"Banana",6,8)

sum = 0
for item in tuple1:
    if (type(item) == int or type(item) == float and type(item) != bool or type(item) != str):
        sum += item

print("Original tuple                            :",tuple1)
print("Sum of the Numeric elements in the Tuple  :",sum)