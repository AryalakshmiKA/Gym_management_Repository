# Convert the Original List to Upper And Lower Case using List Comprehension
mylist = ["Arya","Keerthi","Kannan","Rishi","Naomika","Thumbi"]
print("Original List")
print(mylist)

stud = [name.upper() for name in mylist]
print("Upper Case List")
print(stud)

stud2 = [name.lower() for name in mylist]
print("Lower Case List")
print(stud2)