T = int(input())

for t in range(1, T+1):
    n = int(input())
    c = [0] * 10

    k = 1
    while True:
        nums = list(str(n * k))
        for i in range(len(nums)):
            if c[int(nums[i])] == 0:
                c[int(nums[i])] = 1
        if sum(c) == 10:
            print(f'#{t} {n*k}')
            break
        k += 1
