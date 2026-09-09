# Largest of Two Numbers

largest = lambda x, y : x if x > y else y
print("Largest of Two Numbers   :",largest(10,20))

# Largest of three Numbers using max() function

largest_3 = lambda x,y,z : max(x,y,z)
print("Largest of Three Numbers :",largest_3(10,40,30))

# Largest of three Numbers without using Functions

maximum = lambda x,y,z : x if (x >y and x > z) else (y if y > z else z)
print("Maximum  of Three Numbers :",maximum(20,50,60))