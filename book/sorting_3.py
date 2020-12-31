# 182, 두 배열의 원소 교체
'''
#내 답
n, k = map(int, input().split())

a, b = [], []
for i in range(2):
    data = list(map(int, input().split()))
    for j in range(n):
        if i == 0:
            a.append(data[j])
        else:
            b.append(data[j])

for _ in range(k):
    a.sort()  # a를 오름차순 정렬
    b.sort(reverse=True)  # b를 내림차순 정렬
    a[0], b[0] = b[0], a[0]  # a에서 가장 작은 값과 b에서 가장 큰 값을 swap

print(sum(a))  # a의 모든 원소의 합 출력
'''

# 모범 답안, 정렬을 단 한번만 시행하기 때문에 내 답보다 효율적임
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()  # a는 오름차순 정렬
b.sort(reverse=True)  # b는 내림차순 정렬

# 첫 번째 인덱스부터 확인하며, 두 배열의 원소를 최대 k번 비교
for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))
