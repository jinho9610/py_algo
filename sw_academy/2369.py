T = int(input())

for t in range(1, T+1):
    n = int(input())
    result = 0
    for _ in range(n):
        li, ri = map(int, input().split())
        result += ri - li + 1

    print(f'#{t} {result}')
