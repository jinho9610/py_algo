# p.259
# 내 답안이고, 모범답안과 완전히 동일하다.
n, m = map(int, input().split())
INF = int(1e9)


graph = [[INF]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0


for i in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

x, k = map(int, input().split())
print(graph[1][k]+graph[k][x]) if graph[1][k] + \
    graph[k][x] >= INF else print(-1)
