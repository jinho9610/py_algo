from collections import deque

n, m, k, x = map(int, input().split())
arr = [[] for _ in range(n+1)]

for _ in range(m):
    i, j = map(int, input().split())
    arr[i].append(j)

c = [-1]*(n+1)


def bfs(x):
    q = deque()
    q.append(x)
    c[x] = 0
    while q:
        v = q.popleft()
        for node in arr[v]:
            if c[node] == -1:
                q.append(node)
                c[node] = c[v] + 1


bfs(x)

check = False
for i in range(1, n+1):
    if c[i] == k:
        print(i)
        check = True
if check == False:
    print(-1)
