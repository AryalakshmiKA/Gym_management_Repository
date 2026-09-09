def cal_hcf(x,y):
    if x < y:
        small = x
    else:
        small = y
    for i in range(1, small+1):
        if x % i == 0 and y % i == 0:
            hcf = i
    return hcf

num1 = int(input("Enter a number        :"))
num2 = int(input("Enter another Number  :"))
result = cal_hcf(num1,num2)
print("HCF of ",num1,"and",num2,"is",result)