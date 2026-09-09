def check_age(age):
    if age <18:
        raise ValueError("Not Eligible...!")
    return "Eligible"
print(check_age(20))