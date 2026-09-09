# 9. Write a program to check whether two tuples contain the same elements
# regardless of order.

tuple1 = (1,2,3,2,4)
tuple2 = (4,2,1,3,2)

list1 = []
for item in tuple1:
    list1.append(item)

list2 = []
for item in tuple2:
    list2.append(item)

is_equal = True
for item in list1:
    found = False
    for i in range(len(list2)):
        if list2[i] == item:
            list2.pop(i)
            found = True
            break
    if not found:
        is_equal = False
        break
if list2:
    is_equal = False

if is_equal:
    print("The tuples contain the same elements regardless of order.")
else:
    print("The tuple do not contain the same elements.")
