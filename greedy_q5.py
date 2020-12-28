# p.315 볼링공 고르기
'''
# 내 답, 조합이용 하여 풀이함
from itertools import combinations

n, m = map(int, input().split())

weight = list(map(int, input().split()))
weight.insert(0, 0)
nums = [i for i in range(1, n+1)]
combi = list(combinations(nums, 2))

m = []
for i in range(len(combi)):
    if weight[combi[i][0]] == weight[combi[i][1]]:
        m.append(i)
for i in range(len(m)):
    del combi[m[i]]

print(len(combi))
'''

# 모범 답안 참고하여 직접 작성한 답
n, m = map(int, input().split())

data = list(map(int, input().split()))
weight = [0] * 11

for d in data:
    weight[d] += 1

result = 0
for i in range(1, m+1):
    n -= weight[i]
    result += weight[i] * n

print(result)
