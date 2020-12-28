# 3중 d 배열 필요한 것으로 보임, 좀 더 공부하고 다시 도전 https://has3ong.github.io/boj-14722/
n = int(input())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

d = [[0]*n for _ in range(n)]

dx = [1, 0]
dy = [0, 1]

milk_type = [0, 1, 2]  # 0 - 딸기   1 - 초코   2 - 바나나

m = 0
if arr[0][0] == 0:
    d[0][0] = 1
    m = 0
else:
    d[0][0] = 0
    m = -1

for i in range(1, n):  # 가로 방향 초기화
    d[0][i] = d[0][i-1]
    if milk_type[arr[0][i]-1] == milk_type[arr[0][i-1]] == m:
        d[0][i] += 1
        m = arr[0][i]

for i in range(1, n):  # 가로 방향 초기화
    d[i][0] = d[i-1][0]
    if milk_type[arr[i][0]-1] == milk_type[arr[i-1][0]] == m:
        d[i][0] += 1
        m = arr[i][0]

for i in range(1, n):
    for j in range(1, n):
        if milk_type[arr[i][j]-1] == milk_type[arr[i][j-1]] == m:  # 서쪽에서 온 경우
            d[i][j] = max(d[i-1][j], d[i][j-1] + 1)
            m = arr[i][j]
            #print('{} {}: 서쪽 값 받아옴'.format(i, j))
        elif milk_type[arr[i][j]-1] == milk_type[arr[i-1][j]] == m:  # 북쪽에서 온 경우
            d[i][j] = max(d[i-1][j] + 1, d[i][j-1])
            m = arr[i][j]
            #print('{} {}: 북쪽 값 받아옴'.format(i, j))
        else:
            d[i][j] = max(d[i-1][j], d[i][j-1])
            #print('{} {}: 그냥 대소만 비교'.format(i, j))

# print(d)
print(d[n-1][n-1])
