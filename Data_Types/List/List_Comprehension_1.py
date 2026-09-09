# without using List Comprehension

student = ["Arya","Keerthi","Kannan","Rishi","Naomika","Thumbi"]
newlist = []
for name in student:
    if 'a' in name or 'A' in name:
        newlist.append(name)
print("___Names with latter 'A' Without using List Comprehension___")
print(newlist)


# With using List Comprehension

new_data = [name for name in student if 'a' in name or 'A' in name]
print("___Names with latter 'A' With using List Comprehension___")
print(new_data)