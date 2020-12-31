# 개인 연습장
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))


def selection_sorting(arr):
    # 가장 첫 원소는 정렬되어 있다고 판단
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


selection_sorting(arr)
for i in arr:
    print(i, end=' ')
