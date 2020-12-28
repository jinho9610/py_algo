# p.314 만들 수 없는 금액
'''
#내 답, 조합을 이용해서 모든 가능한 경우의 수를 d라는 배열에 기록
from itertools import combinations

n = int(input())

data = list(map(int, input().split()))

d = [0] * (sum(data)+1)

for i in range(1, n+1):
    a = list(combinations(data, i))
    for j in range(len(a)):
        d[sum(a[j])] = 1

for i in range(1, len(d)):
    if d[i] == 0:
        print(i)
        break
'''

n = int(input())

data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    if target < x:
        break
    target += x

print(target)
