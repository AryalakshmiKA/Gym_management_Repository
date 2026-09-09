list1 = ["Django", "HTML", "Python", "Java", "C++"]
print(list1)
del list1[0]
print(list1)

del list1[1:3]
print(list1)

list1.remove("C++")
print(list1)

list1.pop(0)
print(list1)

list1.insert(0,"Django")
print(list1)

list1.clear()
print(list1)

list1.insert(0,"Java")
print(list1)

del list1