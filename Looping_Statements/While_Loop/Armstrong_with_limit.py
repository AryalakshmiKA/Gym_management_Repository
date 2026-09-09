lb = int(input("Enter the Lower Bound :"))
ub = int(input("Enter the Upper Bound :"))
print("Armstrong Number Between",lb,"and",ub)
for i in range(lb,ub+1):
    t = i
    s = 0
    l = len(str(i))
    while i>0:
        d = i % 10
        s += d ** l
        i //= 10
    if s == t:
        print(t)