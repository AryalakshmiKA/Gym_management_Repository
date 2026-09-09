n = int(input("Enter the number :"))
temp = n
s = 0
l = 0
l = len(str(n))
print("Number if digits : ", l)
while n >0:
    d = n % 10
    s += d ** l
    n //= 10
if s == temp:
    print(temp,"is an armstrong number")
else:
    print(temp,"is not an armstrong number")