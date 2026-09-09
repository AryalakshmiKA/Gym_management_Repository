# Smallest of three Numbers


# Using min() Function
smallest = lambda a,b,c : min(a,b,c)
print("Smallest of Three Numbers  :",smallest(10,4,67))

# Without Using min()

min = lambda a,b,c : a if(a <b and a < c) else (b if b < c else c)
print("Smallest of Three Numbers  :",min(8,40,17))