# to Create and Write A file

#f = open("Demo.txt","x")
#f.close()

file = open("Demo.txt","w")
file.write("File Handling in python.")
file.close()

a = open("Demo.txt")
print(a.read())
a.close()