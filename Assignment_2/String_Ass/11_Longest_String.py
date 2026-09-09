# Write a program to find the length of the longest substring without repeating
# characters.

str1 = input("Enter the String :")
last_idx = {}
max_len = 0
start_idx = 0
for i in range(0,len(str1)):
    if str1[i] in last_idx:
        start_idx = max(start_idx,last_idx[str1[i]]+1)
    max_len = max(max_len, i-start_idx+1)
    last_idx[str1[i]] = i
print("The length of longest non-repeating character substring is ",max_len)