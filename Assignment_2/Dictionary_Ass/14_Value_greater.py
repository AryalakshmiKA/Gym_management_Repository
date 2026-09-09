# 14. Write a program to print all keys whose values are greater than a given
# number.

stud_mark = {'Malayalam':85,'Maths':45,'English': 40,'Science':77}
print(f"_____Student Mark Details_____\n",stud_mark)
pass_mark = int(input("Enter the Pass Mark :"))
print("List of Subject Pass   :  ")
for key,value in stud_mark.items():
    if value > pass_mark:
        print(key)