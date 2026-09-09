num = int(input("Enter the number : "))
a = num
s = 0
while num > 0:
    r = num % 10
    s += r
    num = num // 10
print("Sum of digits : ",s)
h = a % s
if h == 0:
    print(a," is a Harshad number")
else:
    print(a,"is not a Harshad number")
