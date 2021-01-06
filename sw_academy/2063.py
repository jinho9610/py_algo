n = int(input())

arr = list(map(int, input().split()))

arr.sort()  # 오름차순 정렬

print(arr[n//2])
