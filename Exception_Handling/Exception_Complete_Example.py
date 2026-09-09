try:
    num = int(input("Enetr a Number  : "))
    result = 200 / num
except ValueError:
    print("Invalid Input....")
except ZeroDivisionError:
    print("Division By Zero....")
else:
    print("Result is : ",result)
finally:
    print("Division Completed...!")