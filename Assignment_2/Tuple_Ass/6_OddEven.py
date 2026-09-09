# 6. Write a program to count the number of even and odd numbers in a tuple.

tuple1 = (12,33,42,55,66,71,86,99,36,15)

even = []
odd = []
for num in tuple1:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
print("Original Tuple              :",tuple1)
print("Even Numbers from the Tuple :",tuple(odd))
print("Odd Numbers from the Tuple  :",tuple(even))