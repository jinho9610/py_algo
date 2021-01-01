import copy
from itertools import combinations
from collections import deque

n, m = map(int, input().split())

arr = [[0]*m for _ in range(n)]
blanks = []

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(m):
        arr[i][j] = data[j]
        if data[j] == 0:
            blanks.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def infect(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < m and new_arr[nx][ny] == 0:
                q.append((nx, ny))
                new_arr[nx][ny] = 2


wall_candidates = list(combinations(blanks, 3))  # 벽 후보군

result = 0
for walls in wall_candidates:  # 모든 벽 후보군들에 대해서
    new_arr = copy.deepcopy(arr)
    for i in range(3):  # 벽 3개 설치
        new_arr[walls[i][0]][walls[i][1]] = 1

    for i in range(n):
        for j in range(m):
            if new_arr[i][j] == 2:
                infect(i, j)

    cnt = 0
    for i in range(n):
        for j in range(m):
            if new_arr[i][j] == 0:
                cnt += 1

    result = max(result, cnt)
print(result)
