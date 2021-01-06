T = int(input())

for t in range(1, T+1):
    v = 0  # 속도 초기값 0
    n = int(input())  # 명령어 갯수
    result = 0  # 이동 거리
    for i in range(n):
        command = list(map(int, input().split()))
        if len(command) == 1:  # 속도 유지
            result += v
        else:
            if command[0] == 1:  # 속도 증가인 경우
                v += command[1]  # 가속도만큼 증가
                result += v
            else:
                if v < command[1]:
                    v = 0
                else:
                    v -= command[1]
                result += v

    print(f'#{t} {result}')
