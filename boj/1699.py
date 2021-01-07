n = int(input())

dp = [1e9]*(n+1)
dp[1] = 1
squares = [1]


def isSquare(n):
    return int(n**0.5)**2 == n


for i in range(2, n+1):
    if isSquare(i):
        squares.append(i)
        dp[i] = 1
    else:
        for j in range(len(squares)):
            dp[i] = min(dp[i-squares[j]]+1, dp[i])

print(dp[n])
