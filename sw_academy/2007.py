T = int(input())

for t in range(1, T+1):
    data = input()

    for i in range(1, 11):  # 마디의 최대 길이 10이므로 모든 경우의 수 확인
        if data[:i] == data[i:i*2]:
            print(f'#{t} {i}')
            break
