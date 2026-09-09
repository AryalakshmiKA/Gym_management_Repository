n = int(input("Enter the number :"))
temp = n
s = 0
while n >0:
    d = n % 10
    s += d ** 3
    n //= 10
if s == temp:
    print(s,"is an armstrong number")
else:
    print(s,"is not an armstrong number")