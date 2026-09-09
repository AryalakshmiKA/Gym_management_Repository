# 5. Write a program to remove a key from a dictionary without using the pop()
# method.

sample_dict = {"Name":"Ammu","place":"Kochi","mailid":"ammu@gmail.com"}
print("The Dictionary :",sample_dict)
remove_key = input("Enter the Key that want to Remove from the Dictionary : ")

if remove_key in sample_dict:
    del sample_dict[remove_key]
print("Updated Dictionary : ",sample_dict)