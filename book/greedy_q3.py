data = list(map(int, list(input())))

flag = data[0]

c = []
cnt = 1
for i in range(1, len(data)):
    if i == len(data)-1:
        if data[i-1] != data[i]:
            c.append(cnt)
            cnt = 1
        else:
            cnt += 1
        c.append(cnt)
    else:
        if data[i] == flag:
            cnt += 1
        else:
            flag = data[i]  # 플래그 변경
            c.append(cnt)
            cnt = 1
print(len(c)//2)

# 모범 답안, 내 답과 동일한 로직이지만 훨씬 간결함
# data = input()

# count0 = 0  # 전부 0으로 바꾸는 경우
# count1 = 0  # 전부 1로 바꾸는 경우

# if data[0] == '1':
#     count0 += 1
# else:
#     count1 += 1

# for i in range(len(data)-1):
#     if data[i] != data[i+1]:
#         if data[i+1] == '1':
#             count0 += 1
#         else:
#             count1 += 1

# print(min(count0, count1))
# 1000101010101111101001001110001101
