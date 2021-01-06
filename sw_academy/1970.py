T = int(input())

coin_types = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for t in range(1, T+1):
    n = int(input())
    result = []
    for coin in coin_types:
        result.append(n//coin)
        n %= coin
    print(f'#{t}')
    for i in result:
        print(i, end=' ')
    print()
