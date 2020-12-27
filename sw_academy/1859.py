T = int(input())

for t in range(T):
    n = int(input())
    costs = list(map(int, input().split()))
    gain = 0
    cur_out = 0
    days = 0
    for i in range(n):
        if i == n-1:
            gain += costs[i] * days - cur_out
        else:
            if costs[i] <= costs[i+1]:
                cur_out += costs[i]
                days += 1
            else:
                gain += costs[i] * days - cur_out
                days = 0
                cur_out = 0
    print('#{0} {1}'.format(t + 1, gain))
'''
n = int(input())
ans = []
for i in range(n):
    sum = 0
    m = int(input())
    price = list(map(int, input().split()))
    last = price[-1]
    for j in range(len(price) - 1, -1, -1):
        if last > price[j]:
            sum += (last-price[j])
        else:
            last = price[j]
    ans.append(sum)
    print('#{} {}'.format(i + 1, sum))

for i in range(len(ans)):
    print(ans[i], end=' ')
'''
