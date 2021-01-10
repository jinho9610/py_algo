# 특정 원소가 속한 집합을 찾기(루트 노드 찾기)
def find_parent(parent, x):
    if parent[x] != x:
        # return find_parent(parent, parent[x])
        # 이렇게 하면 '경로 압축'을 통해서 복잡도 줄일 수 있음
        parent[x] = find_parent(parent, parent[x])
    return x


def union_parent(parent, a, b):  # 두 원소가 속한 집합을 합치기
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


# 노드 개수와 간선 개수(union 연산의 수) 입력 받기
v, e = map(int, input().split())
parent = [i for i in range(v+1)]

# union 연산 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합', end='')
for i in range(1, v+1):
    print(find_parent(parent, i), end=' ')

print()

# 부모 테이블 내용 출력
print('부모 테이블: ', end='')
for i in range(1, v+1):
    print(parent[i], end=' ')
