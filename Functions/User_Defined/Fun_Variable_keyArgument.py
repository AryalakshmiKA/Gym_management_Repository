# **kwargs - key word arguments

def myfunction(**data):
    print(data)
    for key,value in data.items():
        print(key," : ",value)
myfunction(Name="Anjana",Age=28,Place="Kochi")


