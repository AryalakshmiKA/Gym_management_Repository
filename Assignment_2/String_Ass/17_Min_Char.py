# Write a program to find the minimum number of character insertions required
# to make a string a palindrome.

str1 = input("Enter the String :")
n = len(str1)
dp = [[0] * n for _ in range(n)]
for length in range(2, n + 1):
    for l in range(n - length + 1):
        h = l + length - 1
        if str1[l] == str1[h]:
            dp[l][h] = dp[l + 1][h - 1]
        else:
            dp[l][h] = min(dp[l + 1][h], dp[l][h - 1] + 1)
result = dp[0][n - 1]
print("The Count :",result)