# p.113, 구현 및 완전탐색 문제
'''
#내 답
n = int(input())

start_time = 0  # 0초
dest_time = n * 3600 + 59 * 60 + 59  # 'n시 59분 59초'의 초단위 표현

cnt = 0
for i in range(dest_time+1):
    time = i
    h = time//3600
    time %= 3600
    m = time//60
    time %= 60
    s = time
    if h % 10 == 3:
        cnt += 1
    elif 30 <= m < 40 or m % 10 == 3:
        cnt += 1
    elif 30 <= s < 40 or s % 10 == 3:
        cnt += 1

print(cnt)
'''

# 모범 답안, in을 사용한 문자열 비교, 시간을 초로 변경하는 내 답안에 비해서 효율적임
h = int(input())

cnt = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                cnt += 1
print(cnt)
