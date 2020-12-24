# 입력된 행별로 가장 작은 값을 고르고, 가장 작은 값들 중 가장 큰 값을 고르는 문제
# min, max 내장함수가 포인트
n, m = map(int, input().split())
arr = [[0] * (m+1) for _ in range(n+1)]

result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_val = min(data)
    result = max(result, min_val)

print(result)
