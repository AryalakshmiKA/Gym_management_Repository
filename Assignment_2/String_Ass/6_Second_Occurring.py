# Write a program to find the second most frequently occurring character in a
# string.

str1 = input("Enter the String  :")
frequencie = {}
for char in str1:
    if char in frequencie:
        frequencie[char] += 1
    else:
        frequencie[char] = 1
print(frequencie.items())
max = -1
second_max = -1

max_char = None
second_max_char = None

for char, count in frequencie.items():
   # print(char,count)
    if count > max:
        second_max = max
        second_max_char = max_char
        max = count
        max_char = char
    elif count > second_max and count < max:
        second_max = count
        second_max_char = char
if second_max_char is not None:
    print("The second most frequent character is :", second_max_char)
    print("It appears",second_max,"times.")
else:
    print("There is no second Most frequent character.")
