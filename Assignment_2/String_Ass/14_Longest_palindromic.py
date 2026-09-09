# Write a program to find the longest palindromic substring in a given string.

s = input("Enter the String : ")
n = len(s)
dp = [[False for _ in range(n)] for _ in range(n)]

    # All single characters are palindromes
for i in range(n):
    dp[i][i] = True

max_length = 1
start = 0

for length in range(2, n + 1):
    for i in range(n - length + 1):
        end = i + length - 1

        if length == 2:
            if s[i] == s[end]:
                dp[i][end] = True
                max_length = length
                start = i
        else:
            if s[i] == s[end] and dp[i + 1][end - 1]:
                dp[i][end] = True
                max_length = length
                start = i

    result = s[start:start + max_length]
print("Longest palindromic substring:", result)