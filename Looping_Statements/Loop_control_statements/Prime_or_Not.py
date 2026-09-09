num = int(input("Enter a number : "))
if num < 0:
    print("Enter a Positive number..!")
elif num == 0:
    print("Number is Zero...!")
elif num == 1:
    print("Number is Composite number")
else:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a Prime Number")
            break
    else:
        print(num,"is a Prime Number")
