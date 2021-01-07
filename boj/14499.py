import copy

n, m, x, y, k = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

commands = list(map(int, input().split()))

dice = [0, 0, 0, 0, 0, 0]  # 앞에서부터 위, 아래, 앞, 뒤, 좌, 우


def rot_dice(dir):
    dum_dice = copy.copy(dice)
    if dir == 1:  # 오른쪽으로 굴리는 경우
        dice[5] = dum_dice[0]  # t->r
        dice[1] = dum_dice[5]  # r->d
        dice[4] = dum_dice[1]  # d->l
        dice[0] = dum_dice[4]  # l->t
        # 앞, 뒤는 그대로
    elif dir == 2:  # 왼쪽으로 굴리는 경우
        dice[0] = dum_dice[5]  # r->t
        dice[5] = dum_dice[1]  # d->r
        dice[1] = dum_dice[4]  # l->d
        dice[4] = dum_dice[0]  # t->l
        # 앞, 뒤는 그대로
    elif dir == 3:  # 위쪽으로 굴리는 경우
        dice[0] = dum_dice[2]  # f->t
        dice[3] = dum_dice[0]  # t->b
        dice[1] = dum_dice[3]  # b->d
        dice[2] = dum_dice[1]  # d->f
        # 좌, 우는 그대로
    else:  # 아래쪽으로 굴리는 경우
        dice[2] = dum_dice[0]  # t->f
        dice[0] = dum_dice[3]  # b->t
        dice[3] = dum_dice[1]  # d->b
        dice[1] = dum_dice[2]  # f->d
        # 좌, 우는 그대로


def isInside(x, y):
    return -1 < x < n and -1 < y < m


for i in range(k):
    nx, ny = x, y
    dir = commands[i]
    if dir == 1:
        ny += 1
    elif dir == 2:
        ny -= 1
    elif dir == 3:
        nx -= 1
    else:
        nx += 1

    if not isInside(nx, ny):
        continue  # x, y 업데이트 없이 명령 무시하고 for문 돌기

    else:
        rot_dice(dir)  # 명령대로 주사위 굴리기
        print(dice[0])  # 윗 칸 출력

    if arr[nx][ny] == 0:  # 도착한 칸이 0인 경우
        arr[nx][ny] = dice[1]  # 주사위 바닥 칸 복사
    else:
        dice[1] = arr[nx][ny]
        arr[nx][ny] = 0

    x, y = nx, ny  # 주사위 위치 좌표 업데이트
