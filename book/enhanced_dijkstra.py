import sys
from heapq import *

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())

graph = [[] for i in range(n+1)]  # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
visited = [False]*(n+1)  # 방문한적 있는 지 체크하기 위한 리스트
distance = [INF]*(n+1)  # 디스턴스 테이블, 최단 거리 기록

for _ in range(m):
    a, b, c = map(int, input().split())  # a노드에서 b노드로 가는 비용이 c이다.
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heappop(q)  # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기

        if distance[now] < dist:  # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heappush(q, (cost, i[0]))


dijkstra(start)
for i in range(1, n+1):
    print(distance[i]) if distance[i] != INF else print('INIFITY')
