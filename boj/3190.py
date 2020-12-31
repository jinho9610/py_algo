n = int(input())  # 보드 크기
arr = [[0]*n for _ in range(n)]

k = int(input())  # 사과 정보
for i in range(k):
    x, y = map(int, input().split())
    arr[x-1][y-1] = 100  # 사과는 100으로 표시

l = int(input())  # 방향 변환 정보
dir = []
for i in range(l):
    x, c = input().split()
    dir.append((int(x), c))


def isInside(x, y):
    return -1 < x < n and -1 < y < n


def isMyself(x, y):
    if arr[x][y] == 1:
        return True
    else:
        return False


def change_dir(cur_dir, c):  # 0 - 동쪽, 1 - 남쪽, 2 - 서쪽, 3 - 북쪽
    new_dir = 0
    if c == 'L':
        new_dir = cur_dir - 1
        if new_dir == -1:
            new_dir = 3
    elif c == 'D':
        new_dir = cur_dir + 1
        if new_dir == 4:
            new_dir = 0
    return new_dir


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

sec = 0
dir_idx = 0
cur_dir, prev_dir = 0, 0
head_x, head_y = 0, 0
length = 1
arr[0][0] = 1  # 뱀위 위치하는 곳은 1
q = [(0, 0)]  # 뱀의 위치 정보, 리스트 index 0 값이 꼬리
while True:
    sec += 1

    head_x, head_y = head_x+dx[cur_dir], head_y+dy[cur_dir]  # 다음 뱀머리가 이동할 좌표

    if isInside(head_x, head_y) == False or isMyself(head_x, head_y) == True:  # 뱀 머리가 벽과 닿거나 자신과 닿는다면
        break  # 게임 오버

    if arr[head_x][head_y] == 100:  # 다음 칸에 사과가 있다면
        arr[head_x][head_y] = 1
        q.append((head_x, head_y))
        # 뱀꼬리 좌표는 변화 없음
    else:  # 다음 칸에 뭐 별거없다면
        arr[head_x][head_y] = 1
        q.append((head_x, head_y))
        tail_x, tail_y = q.pop(0)
        arr[tail_x][tail_y] = 0  # 원래 뱀꼬리 있던 곳 떠난다

    if dir_idx < l and dir[dir_idx][0] == sec:  # 새로운 방향 부터 정하기
        cur_dir = change_dir(cur_dir, dir[dir_idx][1])
        dir_idx += 1
print(sec)


# def simulate():
#     x, y = 0, 0
#     arr[x][y] = 1  # 뱀이 존재하는 위치는 2로 표시
#     direction = 0  # 최초에는 동쪽을 바라봄
#     time = 0  # 시작한 뒤에 지난 sec
#     index = 0  # 다음에 회전할 정보
#     q = [(x, y)]  # 뱀이 차지하고 있는 위치 정보(꼬리가 앞쪽)
#     while True:
#         nx, ny = x+dx[direction], y+dy[direction]
#         # 맵 범위 안에 있고, 뱀의 몸통이 없는 위치라면
#         if 0 <= nx <= n-1 and 0 <= ny <= n-1 and arr[nx][ny] != 1:
#             # 사과가 없ㄷ면 이동 후에 꼬리 제거
#             if arr[nx][ny] == 0:
#                 arr[nx][ny] = 1
#                 q.append((nx, ny))
#                 px, py = q.pop(0)  # 꼬리 좌표
#                 arr[px][py] = 0
#             # 사과가 있다면 이동 후에 꼬리 그대로 두기
#             if arr[nx][ny] == 100:
#                 arr[nx][ny] = 1
#                 q.append((nx, ny))
#         # 벽이나 뱀의 몸통과 부딪히면
#         else:
#             time += 1
#             break
#         x, y = nx, ny  # 다음 위치로 머리를 이동
#         time += 1
#         if index < l and time == dir[index][0]:
#             direction = change_dir(direction, dir[index][1])
#             index += 1
#     return time


# print(simulate())
