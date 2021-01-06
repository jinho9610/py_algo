n = int(input())

arr = list(map(int, input().split()))

# 가장 긴 감소하는 수열의 길이를 찾는 문제
d = [1] * n

for i in range(1, n):
    for j in range(i):
        if arr[i] < arr[j]:
            d[i] = max(d[i], d[j] + 1)

print(n - max(d))
