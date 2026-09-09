str1 = "Hello I am Aryalakshmi K A"
upper = 0
lower = 0
special = 0
for i in str1:
    if i.isupper():
        u += 1
    elif i.islower():
        l += 1
    else:
        s = s + 1
print("No: of Upper Case letters : ", upper)
print("No: of Lower Case letters : ", lower)
print("No: of Special letters    : ", special)