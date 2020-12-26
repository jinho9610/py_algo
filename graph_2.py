from collections import deque

n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def isInside(x, y):
    if 0 <= x < n and 0 <= y < m:
        return True
    else:
        return False


result = 0


def bfs(x, y):
    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if isInside(nx, ny) == True and arr[nx][ny] == 1:
                queue.append((nx, ny))
                arr[nx][ny] = arr[x][y]+1

    return arr[n-1][m-1]


print(bfs(0, 0))
