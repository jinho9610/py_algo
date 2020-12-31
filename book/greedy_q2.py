# p.312
# 내 답
data = list(map(int, list(input())))
data.sort(reverse=True)

result = 1
for i in range(len(data)):
    if data[i] != 0:
        result *= data[i]
    else:
        result += data[i]

print(result)
