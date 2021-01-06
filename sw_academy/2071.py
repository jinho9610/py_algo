T = int(input())


def avg(arr):
    return int(round(sum(arr)/len(arr), 0))


for t in range(1, T+1):
    data = list(map(int, input().split()))
    print(f'#{t} {avg(data)}')
