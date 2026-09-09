class Calculater:
    def __init__(self):
        self.num1 = ""
        self.num2 = ""
    def numbers(self):
        self.num1 = int(input("Enter First Number : "))
        self.num2 = int(input("Enter Second Number : "))
    def addition(self):
        print(self.num1,"+",self.num2,"=",self.num1+self.num2)
    def subtract(self):
        print(self.num1, "-", self.num2, "=", self.num1 - self.num2)
    def multiply(self):
        print(self.num1, "*", self.num2, "=", self.num1 * self.num2)
    def division(self):
        if self.num2 == 0:
            print("Error: Division by Zero")
        print(self.num1, "/", self.num2, "=", self.num1 / self.num2)
calc = Calculater()
while True:
    print("1. Addition \n"
      "2. Subtraction \n"
      "3. Multiplication \n"
      "4. Division \n"
      "5. Exit")
    ch = int(input("Enter Your Choose : "))
    if ch == 1:
        calc.numbers()
        calc.addition()
    elif ch == 2:
        calc.numbers()
        calc.subtract()
    elif ch == 3:
        calc.numbers()
        calc.multiply()
    elif ch == 4:
        calc.numbers()
        calc.division()
    elif ch == 5:
        print("Exit")
        break
    else:
        print("Invalid Option")
        break

