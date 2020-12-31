# 내 답
n = int(input())

data = list(map(int, input().split()))
data.sort()

result = 0
count = 0

for i in data:
    count += 1  # 팀원 수 하나 증가
    if count >= i:  # 팀원의 수가 현재 공포도 이상이 되면
        result += 1  # 팀 하나 결성 완료
        count = 0  # 팀원의 수 초기화

print(result)
