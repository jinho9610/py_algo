T = int(input())

for t in range(1, T+1):
    n = int(input())

    arr = []
    for _ in range(2):
        arr.append(list(map(int, input().split())))
    dp = [[0]*n for _ in range(2)]
    dp[0][0] = arr[0][0]
    dp[1][0] = arr[1][0]
    dp[0][1] = arr[0][1]+dp[1][0]
    dp[1][1] = arr[1][1]+dp[0][0]

    for j in range(2, n):
        for i in range(2):
            if i == 0:
                dp[i][j] = arr[i][j]+max(dp[0][j-2], dp[1][j-2], dp[1][j-1])
            else:
                dp[i][j] = arr[i][j]+max(dp[0][j-2], dp[1][j-2], dp[0][j-1])

    print(max(dp[0][n-1], dp[1][n-1]))
