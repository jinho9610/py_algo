n = int(input())

coin_types = [500, 100, 50, 10]
cnt = 0

# 내 답
# for i in range(4):
#     cnt += n//coin_types[i]
#     n -= (n//coin_types[i]) * coin_types[i]

# 모범 답안
for coin in coin_types:
    cnt += n // coin
    n %= coin

print(cnt)
