from pprint import pprint
from math import *

n, k = map(int, input().split())

dp = [[]]

for i in range(1, n+1):
    tmp = []
    for j in range(i+1):
        if j == 0 or j == i:
            tmp.append(1)
        else:
            tmp.append(0)
    dp.append(tmp)

for i in range(2, n+1):
    for j in range(1, i):
        dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % 10007

print(dp[n][k] % 10007)
