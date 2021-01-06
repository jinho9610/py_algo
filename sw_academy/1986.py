T = int(input())

for t in range(1, T+1):
    result = 0
    n = int(input())
    for i in range(1, n+1):
        if i % 2 == 0:
            result -= i
        else:
            result += i
    print(f'#{t} {result}')
