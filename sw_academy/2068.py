T = int(input())

for t in range(T):
    arr = list(map(int, input().split()))
    print(f'#{t+1} {max(arr)}')
