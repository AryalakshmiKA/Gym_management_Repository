num = int(input("Enter the number : "))
temp = num
s = 0
l = len(str(num))
while num > 0:
    d = num % 10
    s += d ** l
    num //= 10
    l -= 1
if s == temp:
    print(temp," is Disarium Number")
else:
    print(temp, " is Not  Disarium Number")
