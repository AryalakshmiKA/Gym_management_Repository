# Write a program to compress a string by replacing consecutive repeated
# characters with their occurrence count.

text = input("Enter the String : ")
compressed_dict = {}
item_index = 0
current_char = text[0]
current_count = 1
for i in range(1, len(text)):
    if text[i] == current_char:
        current_count += 1
    else:
        compressed_dict[item_index] = (current_char, current_count)
        item_index += 1
        current_char = text[i]
        current_count = 1

compressed_dict[item_index] = (current_char, current_count)
compressed_text = ""
for key in sorted(compressed_dict.keys()):
    char, count = compressed_dict[key]
    compressed_text += char + str(count)
print("Original string:", text)
print("Compressed string:", compressed_text)
