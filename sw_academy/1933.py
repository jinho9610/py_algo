from math import *

n = int(input())

result = []

for i in range(1, int(sqrt(n))+1):
    if n % i == 0:
        result.append(i)
        result.append(n//i)
    else:
        continue

result.sort()
for i in result:
    print(i, end=' ')
