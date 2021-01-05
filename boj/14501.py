# 모범 답안
n = int(input())
t = []  # 각 상담을 완료하는데 소요되는 일 수
p = []  # 각 상담을 완료했을 때 받을 수 있는 금액
dp = [0]*(n+1)
max_val = 0

for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

for i in range(n-1, -1, -1):  # (n-1)~0까지 역순으로 확인
    time = t[i] + i  # 오늘의 상담을 했을 때, 다음 상담을 진행할 수 있는 가장 빠른 시일
    if time <= n:  # 상담이 기간 안에 끝나는 경우
        # 현재까지의 최고 이익 계산
        dp[i] = max(p[i] + dp[time], max_val)
        max_val = dp[i]
    else:
        dp[i] = max_val

print(dp)
print(max_val)
