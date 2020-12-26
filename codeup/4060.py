# codeup 4060, 전광판 전구 조작
import copy

n, m = map(int, input().split())

arr_on = []
for _ in range(n):
    arr_on.append(list(map(int, input().split())))
arr_off = copy.deepcopy(arr_on)
# 1이 켜진 상태, 0이 꺼진 상태

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def isInside(x, y):
    if 0 <= x < n and 0 <= y < m:
        return True
    else:
        return False


def dfs_on(x, y):
    if arr_on[x][y] == 1:
        return False  # 이미 켜져있다면
    else:
        arr_on[x][y] = 1  # 킨 것으로 표시
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if isInside(nx, ny) and arr_on[nx][ny] == 0:
                dfs_on(nx, ny)
        return True


def dfs_off(x, y):  # 모두 끄기 위한 최소 횟수 구하는 함수
    if arr_off[x][y] == 0:
        return False  # 이미 꺼져있다면
    else:
        arr_off[x][y] = 0  # 끈 것으로 표시
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if isInside(nx, ny) and arr_off[nx][ny] == 1:
                dfs_off(nx, ny)
        return True


result_on, result_off = 0, 0
for i in range(n):
    for j in range(m):
        if dfs_on(i, j) == True:
            result_on += 1

for i in range(n):
    for j in range(m):
        if dfs_off(i, j) == True:
            result_off += 1

print(result_on, result_off)
