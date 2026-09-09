# 8. Write a program to count the number of keys and values in a nested
# dictionary.

nest_dict = {
    'key1': 1,
    'key2': {
        'n_key1': 1,
        'n_key2': {
            'd_key1': 1
        }
    },
    'key3': 4}

tot_key = 0
tot_values = 0

stack = list(nest_dict.values())
tot_key += len(nest_dict)

while stack:
    current_value = stack.pop()
    if isinstance(current_value,dict):
        tot_key += len(current_value)
        stack.extend(current_value.values())
    else:
        tot_values += 1
tot_values = tot_key

print("Total Keys    :", tot_key)
print("Total Values  :", tot_values)