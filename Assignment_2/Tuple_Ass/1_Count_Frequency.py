# 1, Write a program to count the frequency of each element in a tuple.
my_tuple = (1,3,5,1,3,3,7,5,1,9)

frequency = {}

for num in my_tuple:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print("Original Tuple                      :",my_tuple)
print("Count of Elements Repeat Frequently :",frequency)