import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

start = int(input())

graph = [[]for i in range(n+1)]

visited = [False]*(n+1)
distance = [INF]*(1+n)

for _ in range(m):  # 모든 간선 정보 입력받기
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    # a 노드에서 b노드로 가는 비용이 c이다.

# 방무나지 않은 노드 중에서 가장 최단 거리가 짧은 노드의 번호를 반환


def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:  # 순차 탐색
            min_value = distance[i]
            index = i

    return index


def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True

    for j in graph[start]:
        distance[j[0]] = j[1]  # start와 인접한 노드들에 대해서 cost를 distance로

    for i in range(n-1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서 방문 처리
        now = get_smallest_node()
        visited[now] = True

        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[0] = cost


dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print('INFINTIY')
    else:
        print(distance[i], end=' ')
