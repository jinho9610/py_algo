# codeup 4503 바이러스
n = int(input())
m = int(input())

arr = [[] for _ in range(n+1)]  # 완전히 빈 2차원 리스트
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)


def dfs(v):
    global cnt
    visited[v] = True
    cnt += 1
    for i in arr[v]:
        if visited[i] == False:
            dfs(i)


cnt = -1
dfs(1)
print(cnt)
