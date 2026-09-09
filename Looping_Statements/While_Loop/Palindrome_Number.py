num = int(input("Enter the number : "))
temp = num
s = 0
while num > 0:
    d = num % 10
    s = s * 10 + d
    num //= 10
if s == temp:
    print(temp," is a Palindrome Number")
else:
    print(temp, " is Not a Palindrome Number")