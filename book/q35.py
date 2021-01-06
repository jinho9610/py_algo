n = int(input())

dp = []
dp.append(1)
dp.append(2)
dp.append(3)
dp.append(4)
dp.append(5)

i = 6
while True:
    if len(dp) > n:
        print(dp[n-1])
        break
    if i % 2 == 0 and i % 2 in dp:
        dp.append(i)
        continue
    elif i % 3 == 0 and i % 3 in dp:
        dp.append(i)
        continue
    elif i % 5 == 0 and i % 5 in dp:
        dp.append(i)
        continue
    else:
        i += 1
