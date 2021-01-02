from itertools import combinations
import copy
import sys

n = int(input())

arr = [[0]*(n+1) for i in range(n+1)]

teachers, students, blanks = [], [], []
for i in range(1, n+1):
    data = list(input().split())
    for j in range(1, n+1):
        arr[i][j] = data[j-1]
        if data[j-1] == 'T':
            teachers.append((i, j))
        elif data[j-1] == 'S':
            students.append((i, j))
        else:
            blanks.append((i, j))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]  # 북, 동, 남, 서 순서

students_num = len(students)


def isInside(x, y):
    return 0 < x <= n and 0 < y <= n


def security(new_arr, tmp_students, i, j):
    for k in range(4):
        x, y = i, j
        while True:
            nx, ny = x + dx[k], y+dy[k]
            if isInside(nx, ny) and new_arr[nx][ny] != 'O':
                if new_arr[nx][ny] == 'S':
                    tmp_students.remove((nx, ny))
                    return False
                x, y = nx, ny
            else:
                break
    return True


wall_candidates = list(combinations(blanks, 3))  # 벽을 설치한 세 군데 조합

for walls in wall_candidates:
    new_arr = copy.deepcopy(arr)
    tmp_students = copy.deepcopy(students)
    # 장애물 설치
    for i in range(3):
        new_arr[walls[i][0]][walls[i][1]] = 'O'

    for teacher in teachers:
        if security(new_arr, tmp_students, teacher[0], teacher[1]):
            continue
        else:
            break

    if len(tmp_students) == students_num:
        print('YES')
        sys.exit()

print('NO')

'''
#모범 답안
from itertools import combinations

n=int(input())

board = [] #복도 정보
teachers=[] #모든 선생님 위치 정보
spaces=[] #모든 빈 공간

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        if board[i][j] == 'T':
            teachers.append((i, j))
        if board[i][j]=='X':
            spaces.append((i, j))

#특정 방향으로 감시 진행, 학생 발견 - True, 학생 미발견 - False
def watch(x, y, direction):
    if direction == 0:
        while y>=0:
            if board[x][y]=='S': #학생이 있는 경우
                return True
            if board[x][y] =='O':
                return False
            y -= 1

    if direction ==1:#오른쪽 방향 감시
        while y<n:
            if board[x][y]=='S':
                return True
            if board[x][y]=='O':
                return False
            y += 1

    if direction == 2: #위쪽 방향 감시
        while x >=0:
            if board[x][y]=='S':
                return True
            if board[x][y]=='O':
                return False
            x -= 1

    if direction==3: #아래쪽 방향 감시
        while x <n:
            if board[x][y]=='S':
                return True
            if board[x][y]=='O':
                return False
            x += 1

    return False

def process():
    for x, y in teachers:
        for i in range(4):
            if watch(x, y, i): #학생 발견할 경우
                return True
    return False

for data in combinations(spaces, 3):
    for x, y in data:
        board[x][y]='O'
    if not process():
        find = True
        break

    for x, y in data:
        board[x][y]='X'

if find:
    print('YES')
else:
    print('NO')
'''
