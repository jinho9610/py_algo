# p.115
'''
# 내 답
arr = [[0]*9 for _ in range(9)]  # 체스판

pos = input()
x = ord(pos[0]) - ord('a') + 1 # 몇 번째 행인지
y = int(pos[1]) # 몇 번째 열인지

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

cnt = 0

for i in range(8):
    if 0 < x+dx[i] < 9 and 0 < y+dy[i] < 9:
        cnt += 1

print(cnt)
'''

# 모범 답안, 내 답과 완전히 동일함
input_data = input()
row = int(input_data[1])  # 몇 번째 행인지
column = int(ord(input_data[0]))-int(ord('a'))+1  # 몇 번째 열인지

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, 1), (-1, 2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한 지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row+step[0]
    next_column = column+step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)
