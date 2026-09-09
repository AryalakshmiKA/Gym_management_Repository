# Without using List Comprehension
num = [1,2,3,4,5,6]
print("___Original List___")
print(num)
new_num = []
s = 0
for i in num:
    new_num.append(i**2)
print("___Squares of the List without using List Comprehension___")
print(new_num)


# With using List Comprehension
newlist = [i**2 for i in num]
print("___Squares of the List using List Comprehension___")
print(newlist)