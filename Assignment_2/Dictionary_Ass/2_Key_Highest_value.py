# 2. Write a program to find the key with the highest value.

stud_mark = {"Anu":87,"Muna":55,"Anju":23,"Raju":99}
print("Entered Dictionary :",stud_mark)
max_value = max(stud_mark.values())

for key, value in stud_mark.items():
    if value == max_value:
        print("Key with Maximum Value :",key)

