# Given Number is Odd or Even

odd_even = lambda x : "Even" if x % 2 == 0 else "Odd"

x = int(input("Enter a Number  :"))
print(odd_even(x))