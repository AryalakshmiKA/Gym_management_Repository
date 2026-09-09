# 7. Write a program to find all prime numbers present in a list.

my_list = [1,2,3,4,11,15,20,23,29,33,37,40]

prime = []
for num in my_list:
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            prime.append(num)
print("Original List             :",my_list)
print("Prime Numbers in the List :",prime)