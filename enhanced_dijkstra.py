import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# n - 노드 개수   m - 간선 개수
n, m = map(int, input())

start = int(input())

graph = [[]for _ in range(n+1)]

distance = [INF]*(n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))  # 현재 최소 거리, 노드번호 순으로 삽입
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)  # 가장 최소 거리를 갖는 노드 선택(힙에서 자동으로 꺼내줌)
        if distance[now] > dist:  # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
            continue
        for i in graph[now]:  # 현재 노드와 연결된 다른 인접한 노드들을 확인
            cost = dist + i[1]
            if cost < distance[i[0]]:  # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
