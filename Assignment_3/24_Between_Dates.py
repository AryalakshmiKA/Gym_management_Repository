from datetime import date

date1 = date(2026,1,1)
date2 = date(2026,8,19)

between_date = date2 - date1
print("Dates Between is : ",between_date.days)