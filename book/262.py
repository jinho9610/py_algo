# p.262
import sys
from heapq import *

input = sys.stdin.readline
INF = int(1e9)

n, m, start = map(int, input().split())

graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

distance = [INF] * (n+1)


def dijkstra(start):
    q = []
    heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:  # i[0]이 노드, i[1]이 거리
            if dist + i[1] < distance[i[0]]:
                distance[i[0]] = dist+i[1]
                heappush(q, (distance[i[0]], i[0]))


dijkstra(start)
print(distance)

cnt = 0
max_distance = 0
for d in distance:
    if d != INF:
        cnt += 1
        max_distance = max(max_distance, d)

print(cnt - 1, max_distance)

'''
3 2 1
1 2 4
1 3 2

답: 2 4
'''
