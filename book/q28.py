from bisect import bisect_left, bisect_right

n = int(input())

arr = list(map(int, input().split()))

idx_incli = 1
arr_incli = (arr[-1]-arr[0])/n

start, end = 0, n-1
while True:
    if start > end:
        print(-1)
        break
    mid = (start+end)//2
    if arr[mid] == mid:
        print(mid)
        break
    elif arr[mid] > mid:
        end = mid - 1
    else:
        start = mid + 1
