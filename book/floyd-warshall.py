INF = int(1e9)

n = int(input())
m = int(input())

# 2차원 리스트를 만들고, 모든 값을 무한으로 표현
graph = [[INF]*(n+1)for _ in range(n+1)]

# 자기 자신으로 가는 비용 0으로 초기화
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

# 간선정보 입력받고 graph 업데이트
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 알고리즘
for b in range(1, n+1):
    for a in range(1, n+1):
        for k in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print('INFINITY', end=' ')
        else:
            print(graph[a][b], end=' ')
    print()
