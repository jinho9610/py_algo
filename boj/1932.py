n = int(input())

arr = [[0]*n for _ in range(n)]
d = [[0]*n for _ in range(n)]

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if j < len(data):
            arr[i][j] = data[j]
        if j == 0:
            d[i][j] = d[i-1][j]+arr[i][j]
        if j == len(data)-1:
            d[i][j] = d[i-1][j-1]+arr[i][j]

for i in range(1, n):
    for j in range(1, i):
        d[i][j] = max(d[i-1][j]+arr[i][j], d[i-1][j-1]+arr[i][j])

print(max(d[n-1]))
