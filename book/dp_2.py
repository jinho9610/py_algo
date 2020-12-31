# p.220 개미전사
# 내 답
'''
n = int(input())

data = list(map(int, input().split()))

m = [0] * (n + 1)

for i in range(1, n+1):
    if i == 1:
        m[i] = data[i-1]
    elif i == 2:
        m[i] = data[i-1]
    else:
        m[i] = max(m[i-1], m[i-2]+data[i-1])

print(m[n])
'''
# 모범 답안, 거의 동일함
n = int(input())
array = list(map(int, input().split()))

d = [0]*(n+1)

d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2]+array[i])

print(d[n-1])
