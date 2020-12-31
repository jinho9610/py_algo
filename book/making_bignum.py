'''
# 내 답
n, m, k = map(int, input().split())

nums = list(map(int, input().split()))

nums.sort(reverse=True)

first = nums[0]
second = nums[1]

sum = 0
cnt = 0
for i in range(m):
    if cnt == k:
        sum += second
        cnt = 0
    else:
        sum += first
        cnt += 1

print(sum)
'''

# 모범 답안
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

first = data[n-1]  # 가장 큰 수
second = data[n-2]  # 두 번째로 수

count = (m // (k+1)) * k
count += m % (k+1)  # 위 두줄은 '가장 큰 수'가 총 몇 번 더해지는 지 선제적으로 계산하는 과정임

result = 0
result += count * first
result += (m-count) * second
# (m-count)는 전체 m번의 덧셈 연산 중 '가장 큰 수'가 더해지는 횟수를 뺀 것 즉, '두번째로 큰 수'의 덧셈 횟수

print(result)
