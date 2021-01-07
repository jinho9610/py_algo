import sys
n = int(input())
if n == 1:
    print(1)
    sys.exit()

dp = [0]*(n+1)
dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
    dp[i] = (dp[i-2]+dp[i-1]) % 15746

print(dp[n] % 15746)
