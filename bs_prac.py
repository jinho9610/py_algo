def binary_search_iterative(arr, target, start, end):
    while start <= end:
        mid = (start + end)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            start = mid + 1
        else:
            end = mid - 1
    return None


def binary_search_recursive(arr, target, start, end):
    if start > end:
        return None
    mid = (start + end)//2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, start, mid - 1)
    else:
        return binary_search_recursive(arr, target, mid + 1, end)


n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search_iterative(array, target, 0, n-1)

if result == None:
    print('원소가 존재하지 않습니다.')
else:
    print(result + 1)
