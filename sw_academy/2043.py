p, k = map(int, input().split())

cnt = 1
while True:
    if k == p:
        break
    else:
        k += 1
        cnt += 1

print(cnt)
