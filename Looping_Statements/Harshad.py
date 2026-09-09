num = int(input("Enter the number : "))
sum = 0
for i in str(num):
    sum += int(i)
print("Sum of its digits : ",sum)
if num % sum == 0:
    print(num," is a Harshad number")
else:
    print(num,"is not a Harshad number")