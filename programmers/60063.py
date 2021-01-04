# 모범 답안, 개인 풀이 X
from collections import deque

board = [[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [
    0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]


def get_next_pos(pos, board):
    next_pos = []  # 반환 결과(이동 가능한 위치들)
    pos = list(pos)  # 현재 위치 정보를 리스트로 변환(집합 -> 리스트)
    pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    # (상, 하, 좌, 우)로 이동하는 경우에 대해서 처리
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        pos1_next_x, pos1_next_y, pos2_next_x, pos2_next_y = pos1_x + \
            dx[i], pos1_y+dy[i], pos2_x+dx[i], pos2_y+dy[i]
        # 이동하고자 하는 두 칸이 모두 비어 있다면
        if board[pos1_next_x][pos1_next_y] == 0 and board[pos2_next_x][pos2_next_y] == 0:
            next_pos.append({(pos1_next_x, pos1_next_y),
                             (pos2_next_x, pos2_next_y)})
    # 현재 로봇이 가로로 놓여 있는 경우
    if pos1_x == pos2_x:
        for i in [-1, 1]:
            if board[pos1_x+i][pos1_y] == 0 and board[pos2_x+i][pos2_y] == 0:
                # 위쪽 혹은 아래쪽 두 칸이 모두 비어 있다면
                next_pos.append({(pos1_x, pos1_y), (pos1_x+i, pos1_y)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x+i, pos2_y)})

    # 현재 로봇이 세로로 놓여 있는 경우
    elif pos1_y == pos2_y:
        for i in [-1, 1]:
            if board[pos1_x][pos1_y+i] == 0 and board[pos2_x][pos2_y+i] == 0:
                next_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y+i)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y+i)})

    return next_pos  # 현재 위치에서 로봇이 이동 및 회전 이후 "위치 가능한" 모든 좌표 순서쌍 반환


def solution(board):
    # 외곽에 벽이 있는 새로운 보드로 변경(편의를 위해서)
    n = len(board)
    new_board = [[1]*(n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            new_board[i+1][j+1] = board[i][j]

    # bfs
    q = deque()
    c = []
    pos = {(1, 1), (1, 2)}  # 시작 위치 설정
    q.append((pos, 0))
    c.append(pos)

    while q:
        pos, cost = q.popleft()
        # (n , n)에 로봇이 도달했다면 최단 거리이므로 반환
        if (n, n) in pos:
            return cost

        # 현재 위치에서 이동할 수 있는 위치 확인
        for next_pos in get_next_pos(pos, new_board):
            if next_pos not in c:  # 아직 로봇이 위치한 적 없는 모습이라면
                q.append((next_pos, cost+1))
                c.append(next_pos)
    return 0


print(solution(board))
