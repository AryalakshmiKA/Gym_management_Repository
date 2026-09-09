import datetime

x = datetime.datetime.now()
print("Current Date and Time   :  ",x)

# 22/07/2026
print(x.strftime("%d/%m/%Y"))

print(x.strftime("%m-%d-%Y"))

print(x.strftime("%B %d, %Y"))

print(x.strftime("%Y %b %d"))

print(x.strftime("%Y %B %d, %I.%M %p"))

print(x.strftime("%A, %d-%B-%Y"))

print(x.strftime("%d %B %Y | %I:%M %p"))

print(x.strftime("%Y/%m/%d %I:%M"))

print("Today is ",x.strftime("%A the %dnd of %B %Y"))