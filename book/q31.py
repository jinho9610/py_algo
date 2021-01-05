# 본인 답변
n, m = map(int, input().split())

data = list(map(int, input().split()))

arr = [[0]*m for _ in range(n)]
d = [[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        arr[i][j] = data[i*m+j]
        if j == 0:
            d[i][j] = arr[i][j]


def isInside(x, y):
    return -1 < x < n and -1 < y < m


for j in range(1, m):
    for i in range(n):
        if i == 0:
            d[i][j] = max(d[i][j-1]+arr[i][j], d[i+1][j-1]+arr[i][j])
        elif i == n-1:
            d[i][j] = max(d[i-1][j-1]+arr[i][j], d[i][j-1]+arr[i][j])
        else:
            d[i][j] = max(d[i-1][j-1]+arr[i][j], d[i][j-1] +
                          arr[i][j], d[i+1][j-1]+arr[i][j])

print(d)

result = 0
for i in range(n):
    result = max(result, d[i][m-1])
print(result)


for tc in range(int(input())):
    # 금광 정보 입력
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    dp = []
    index = 0
    for i in range(n):
        dp.append(arr[index:index+m])
        index += m

    # 다이나믹 프로그래밍 진행
    for j in range(1, m):
        for i in range(n):
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i-1][j-1]
            # 왼쪽 아래에서 오는 경우
            if i == n-1:
                left_down = 0
            else:
                left_down = dp[i+1][j-1]

            # 왼쪽에서 오는 경우
            left = dp[i][j-1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)

    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])

    print(result)
