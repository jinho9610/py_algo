T = int(input())

for t in range(1, T+1):
    h1, m1, h2, m2 = map(int, input().split())
    h, m = h1+h2, m1+m2
    if h > 12:
        h -= 12
    if m > 60:
        m -= 60
        h += 1
    print(f'#{t} {h} {m}')
