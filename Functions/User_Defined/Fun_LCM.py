


def cal_lcm(x,y):
    if x > y:
        greater = x
    else:
        greater = y
    while(True):
        if greater % x == 0 and greater % y == 0:
            lcm = greater
            break
        greater += 1
    return lcm

num1 = int(input("Enter a Number       :"))
num2 = int(input("Enter another number :"))
print("LCM Of ",num1,"and",num2,"is",cal_lcm(num1,num2))