def calc_bmi(weight, height):
    bmi = weight/(height ** 2)
    return bmi

w = float(input("Enter the Weight(kg) : "))
h = float(input("Enter the Height(m) : "))
result = calc_bmi(w,h)
print("BMI Value : ",result)