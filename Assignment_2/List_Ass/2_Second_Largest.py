# 2. Write a program to find the second largest and second smallest elements in a
# list without using the sort() method.

numbers = [12,35,1,10,34,9,32]

new_list = []
for num in numbers:
    new_list.append(num)
if len(new_list) < 2:
    print("List must contain at least two elements.")
else:
    smallest = second_smallest = float('inf')
    largest = second_largest = 0

    for num in new_list:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num

        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest:
            second_smallest = num
print("Original List           :",numbers)
print("Second Smallest Element :",second_smallest)
print("Second Largest Element  :",second_largest)