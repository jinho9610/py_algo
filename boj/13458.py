n = int(input())

arr = list(map(int, input().split()))

b, c = map(int, input().split())

result = []
for i in range(n):
    x, y = 0, 0
    cnt = 0
    if arr[i]-b <= 0:
        result.append(1)
    else:
        if (arr[i]-b) % c == 0:
            result.append((arr[i]-b)//c + 1)
        else:
            result.append((arr[i]-b)//c + 1 + 1)

print(sum(result))
