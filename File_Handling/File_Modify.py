import os

#os.mkdir("New_Folder")
#os.rmdir("New_Folder")

#os.remove("Abc.py")
if os.path.exists("Demo.py"):
    os.remove("Demo.py")
    print("The file has been removed")
else:
    print("The File does not exist...")
print(os.getcwd())