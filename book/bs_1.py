# 197, 부품찾기

# 내 답, 이진 탐색 이용
def binary_search(arr, target, start, end):
    if start > end:
        return None

    mid = (start + end)//2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, end)


n = int(input())
N = list(map(int, input().split()))
m = int(input())
M = list(map(int, input().split()))

N.sort()

for i in M:
    if binary_search(N, i, 0, n-1) == None:
        print('no', end=' ')
    else:
        print('yes', end=' ')

'''
# 모범 답안 중 계수 정렬 이용한 답
n = int(input())
array = [0] * 1000001

for i in input().split():
    array[int(i)] += 1

m = int(input())

x = list(map(int, input().split()))

for i in x:
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')
'''

'''
#모범 답안 중 집합 자료형 이용, 특정 데이터의 존재 판단 시 가장 효율적
n = int(input())
array = set(map(int, input().split())) # set 함수를 이용한 집합 초기화

m = int(input())
x= list(map(int, input().split()))

for i in x:
    if i in array: print('yes', end=' ')
    else: print('no', end=' ')
'''
