from itertools import combinations
import math

# 메모리 초과 발생...
n = int(input())

liquids = list(map(int, input().split()))

combi = list(combinations(liquids, 2))
mixed = []
for i in range(len(combi)):
    tmp = []
    tmp.insert(0, abs(combi[i][0]+combi[i][1]))
    tmp.insert(1, combi[i][0])
    tmp.insert(2, combi[i][1])
    mixed.append(tmp)

mixed = sorted(mixed, key=lambda item: item[0])
print(mixed[0][1], mixed[0][2])
