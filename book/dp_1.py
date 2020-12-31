# p.217 1로 만들기, 다이나믹 프로그래밍
x = int(input())

d = [0] * 30001  # 이래야 인덱스 1 ~ 30000 이용 가능

for i in range(2, x+1):
    d[i] = d[i-1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2]+1)
    elif i % 3 == 0:
        d[i] = min(d[i], d[i//3]+1)
    elif i % 5 == 0:
        d[i] = min(d[i], d[i//5]+1)

print(d[x])
