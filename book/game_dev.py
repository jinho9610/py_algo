# p.119, 시뮬레이션 문제
'''
# 내 답, 방향 이동치를 실수로 기재하고 x, y를 헷갈려서 40분 초과
n, m = map(int, input().split())
arr = [[0]*m for _ in range(n)]
c = [[0]*m for _ in range(n)]

x, y, d = map(int, input().split())  # d는 바라보는 방향
arr[x][y], c[x][y] = 1, 1

steps = [(0, -1), (1, 0), (0, 1), (-1, 0)]

for i in range(n):
    map_data = list(map(int, input().split()))
    for j in range(m):
        arr[i][j] = map_data[j]
        c[i][j] = map_data[j]

cnt, result = 0, 1
while True:
    d -= 1
    if d == -1:
        d = 3
    if arr[y+steps[d][1]][x+steps[d][0]] == 0 and c[y+steps[d][1]][x+steps[d][0]] == 0:  # 다음 칸이 가보지 않았고 육지라면
        x += steps[d][0]
        y += steps[d][1]
        c[y][x] = 1
        result += 1
    else:
        cnt += 1
        if cnt == 4:
            if d == 0 or d == 1:
                x += steps[d+2][0]
                y += steps[d+2][1]
                cnt = 0
            else:
                x += steps[d-2][0]
                y += steps[d-2][1]
                cnt = 0
            if arr[x][y] == 1:  # 근데 후진 이동한 칸이 바다라면 종료
                break
            else:
                continue

print(result)
'''

# 모범 답안
n, m = map(int, input().split())

c = [[0]*m for _ in range(n)]  # 방문 위치 저장하기 위한 맵
x, y, direction = map(int, input().split())
c[x][y] = 1  # 현재 좌표 방문 처리

# 전체 맵 정보 입력받기
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의, 수학에서의 x, y랑 코딩에서 x, y는 반전
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전


def turn_left():
    global direction  # 함수 밖의 변수 direction을 가져온다
    direction -= 1
    if direction == -1:
        direction = 3  # 이 부분은 내 답과 일치


# 시뮬레이션 시작
count = 1
turn_time = 0  # 내 답에서의 cnt와 동등
while True:
    # 먼저 왼쪽회전 처리
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 회전 이후 정면에 '가보지 않은 육지'가 존재하면 전진
    if arr[nx][ny] == 0 and c[nx][ny] == 0:
        x, y = nx, ny
        c[x][y] = 1  # 이동 이후 해당 칸 방문 처리
        count += 1  # 방문한 칸 수 하나 증가
        turn_time = 0  # 회전 횟수 0으로 초기화
        continue  # 무한 루프 while문 다시 시작
    else:
        turn_time += 1

    if turn_time == 4:  # 회전을 4번 하여 전방위로 이동이 불가하다면
        nx = x-dx[direction]
        ny = y-dx[direction]  # 파이썬은 음수 인덱스 지원
        if arr[nx][ny] == 0:  # 육지라면 이동하고 다시 루프 시작
            x, y = nx, ny
            turn_time = 0  # 회전 횟수도 초기화
        else:  # 바다라면
            break

print(count)
