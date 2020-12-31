# p.226 효율적인 화폐 구성
'''
# 내 답
n, m = map(int, input().split())
costs = []
for _ in range(n):
    costs.append(int(input()))

costs.sort()

d = [10001] * (m+1)

for j in range(n):
    for i in range(1, m+1):
        if i % costs[j] == 0:
            d[i] = i // costs[j]
for i in range(1, m+1):
    for j in costs:
        if i > j and d[i-j] != 10001 and i % j != 0:
            d[i] = min(d[i], d[i-j]+1)
if d[m] == 10001:
    print(-1)
else:
    print(d[m])
'''
# 모범 답안
n, m = map(int, input())

array = []
for i in range(n):
    array.append(int(input()))

d = [10001]*(m+1)

d[0] = 0
for i in range(n):
    for j in range(array[i], m+1):
        if d[j-array[i]] != 10001:
            d[j] = min(d[j], d[j-array[i]]+1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])
