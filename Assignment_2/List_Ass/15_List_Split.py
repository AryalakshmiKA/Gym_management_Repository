# 15. Write a program to split a list into two equal halves

my_list = [10,20,30,40,50,60,70,80,90,100]

mid = len(my_list) // 2

first_list = my_list[:mid]
second_list = my_list[mid:]

print("Original List           :",my_list)
print("First Half of the List  :",first_list)
print("Second Half of the List :",second_list)