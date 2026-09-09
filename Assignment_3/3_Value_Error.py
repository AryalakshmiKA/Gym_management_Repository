try:
    user_input = input("Enter an integer : ")
    number = int(user_input)
    print("Success!...You entered a vaild integer : ",number)
except ValueError:
    print("Error : Invalid Input. ")