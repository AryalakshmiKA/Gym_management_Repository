# 4. Write a program to find the frequency of each element in a list

my_list = [1,2,2,2,4,4,6,7,8,8,8]

frequency = {}
for num in my_list:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1
print("Original List  : ",my_list)
print("__Element Frequencies__")
for num, count in frequency.items():
    print("Element :",num,"- Count",count)
