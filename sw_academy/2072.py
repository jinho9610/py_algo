T = int(input())

for t in range(1, T+1):
    data = list(map(int, input().split()))
    sum = 0
    for d in data:
        if d % 2 == 1:
            sum += d
    print('#{} {}'.format(t, sum))
