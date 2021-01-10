P = [2]
for i in range(3, int(10000000**0.5), 2):  # 짝수 배제
    for p in P:
        if i % p == 0:
            break
    else:
        P.append(i)

ans = []
T = int(input())
for t in range(1, T+1):
    a = int(input())
    b = 1
    if a**0.5 != int(a**0.5):
        for p in P:
            cnt = 0
            while not a % p:
                a //= p
                cnt += 1
            if cnt % 2:
                b *= p
            print(p, a, b, cnt)
            if a == 1 or a < p:
                break
        if a > 1:
            b *= a  # 현재 a의 제곱근까지만 소수를 파악했는데, 이 범위를 벗어난 소수는 마지막에 곱셈처리
    ans.append(f'#{t} {b}')

for a in ans:
    print(a)
