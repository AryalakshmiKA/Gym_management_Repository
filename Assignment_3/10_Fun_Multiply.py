def list_multiply(numbers):
    result = 1
    for num in numbers:
        result *= num
    print("Product of the List : ",result)

sample_list = [8,2,3,1,7]
print("List : ",sample_list)
list_multiply(sample_list)