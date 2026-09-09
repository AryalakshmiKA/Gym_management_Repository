import  datetime

x = datetime.datetime.now()
print("Current Date and Time  : ",x)
print("Abbreviated weekday    : ",x.strftime("%a"))
print("Full Weekday           : ",x.strftime("%A"))
print("Abbreviated Month      : ",x.strftime("%b"))
print("Full Version of Month  : ",x.strftime("%B"))

#2026 - 07 - 22 09 : 50 : 23
print(x.strftime("%Y-%m-%d %H:%M:%S"))

# Today is Wednesday, July 22, 2026
print("Today is ",x.strftime("%A, %B %d, %Y"))