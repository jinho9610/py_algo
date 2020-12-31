# p. 201 떡볶이 떡 만들기
'''
# 내 답
n, m = map(int, input().split())
tteok = list(map(int, input().split()))

start, end = 0, max(tteok)
while True:
    result = 0
    mid = (start+end)//2
    for i in range(len(tteok)):
        if tteok[i] - mid >= 0:
            result += tteok[i] - mid
    #print('mid: {0}   전체 떡 길이: {1}'.format(mid, result))
    if result == m:
        break
    elif result < m:
        end = mid - 1
    else:
        start = mid + 1

print(mid)
'''

# 모범 답안
n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 0  # 절단기 탐색 시작 값
end = max(array)  # 절단기 탐색 끝 값

result = 0
while start <= end:
    total = 0
    mid = (start+end)//2
    for x in array:
        # 절단 이후 떡 양 계산
        if x > mid:
            total += x - mid

    if total < m:  # 떡 양이 부족한 경우
        end = mid - 1
    else:
        result = mid  # 최대한 덜 잘랐을 때가 정답이므로, 임시 기록 # 사실 이 부분에 대해 생각하지 못해서 고민하느라 많은 시간을 보냄
        start = mid + 1

print(result)
