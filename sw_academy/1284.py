T = int(input())

for t in range(1, T+1):
    p, q, r, s, w = map(int, input().split())

    a = w * p

    if w <= r:
        b = q
    else:
        b = q + s*(w-r)

    print(f'#{t} {min(a, b)}')
