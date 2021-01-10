import sys
from collections import deque


def case2(depth):
    for i in range(2**depth):
        b = format(i, 'b').zfill(depth)  # i를 2진수로 나타냄
        solve(list(map(int, b)))


def solve(check):
    def bfs(startV):
        q = deque()
        q.append(startV)
        visited[startV] = 1
        thisColor = check[startV-1]

        while q:
            nowV = q.popleft()
            for nextV in edges[nowV]:
                # 아직 방문한 적 없고, 같은 지역구인 것만 방문
                if visited[nextV] == 0 and check[nextV-1] == thisColor:
                    q.append(nextV)
                    visited[nextV] = 1
        return

    visited = [0 for _ in range(n+1)]

    if sum(check) == 0 or sum(check) == n:  # 선거구가 하나로 통일된 상황
        return

    cnt = 0
    for i in range(1, n+1):
        if visited[i] == 0:
            bfs(i)
            cnt += 1

        if cnt == 2:  # 딱 두번만 bfs돈다
            break

    for i in range(1, n+1):
        if visited[i] == 0:
            return  # bfs 두번 돌고도 방문안 한 구역이 있으면 none 반환

    ans = 0
    for i in range(n):
        if check[i] == 0:
            ans += people[i]
        else:
            ans -= people[i]

    global min_val
    if abs(ans) < min_val:
        min_val = abs(ans)


n = int(input())

people = list(map(int, sys.stdin.readline().rstrip().split()))
edges = [[]for _ in range(n+1)]

for i in range(1, n+1):
    temp = list(map(int, sys.stdin.readline().rstrip().split()))
    edges[i] = temp[1:]

min_val = sys.maxsize
case2(n)
print(-1 if min_val == sys.maxsize else min_val)
