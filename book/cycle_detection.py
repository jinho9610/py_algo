def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())
parent = [i for i in range(v+1)]

cycle = False  # 사이클 발생 여부

for i in range(e):
    a, b = map(int, input().split())
    if find_parent(a) == find_parent(b):
        cycle = True
        break
    else:
        union_parent(parent, a, b)

print('사이클이 발생했습니다') if cycle else print('사이클이 발생하지 않았습니다.')
