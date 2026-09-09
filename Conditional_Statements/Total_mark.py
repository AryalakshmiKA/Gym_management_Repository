phy = float(input("Enter the mark of physics : "))
che = float(input("Enter the mark of Chemistry : "))
mat = float(input("Enter the mark of Maths : "))
eng = float(input("Enter the mark of English : "))
cs = float(input("Enter the mark of Computer : "))

total = phy+che+mat+eng+cs
percentage = (total/500)*100
print("Total Marks : ",total)
print("Percentage = ",percentage)
if percentage >= 90:
    print("Gread : A")
elif percentage >= 80:
    print("Gread :B")
elif percentage >= 70:
    print("Grade : C")
elif percentage >= 60:
    print("Gread : D")
else:
    print("Failed...!")