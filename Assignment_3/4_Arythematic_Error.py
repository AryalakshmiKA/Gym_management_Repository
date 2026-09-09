def division():
    try:
        x = float(input("Enter the Dividend : "))
        y = float(input("Enter the Divisor : "))
        result = x / y
        print("Result : ",result)

    except ArithmeticError as error:
        print("Arithmetic Error caught : ",error)
    except ValueError:
        print("Error : Please Enter valid number....")


division()