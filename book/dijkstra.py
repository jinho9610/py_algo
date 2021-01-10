import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())

graph = [[] for i in range(n+1)]  # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
visited = [False]*(n+1)  # 방문한적 있는 지 체크하기 위한 리스트
distance = [INF] * (n+1)  # 디스턴스 테이블, 최단 거리 기록

for _ in range(m):
    a, b, c = map(int, input().split())  # a노드에서 b노드로 가는 비용이 c이다.
    graph[a].append((b, c))

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환


def get_smallest_node():
    min_val = INF
    index = 0  # 가장 최단 거리가 짧은 노드의 인덱스
    for i in range(1, n+1):
        if distance[i] < min_val and not visited[i]:
            min_val = distance[i]
            index = i
    return index


def dijkstra(start):
    distance[start] = 0
    visited[start] = True  # 방문처리

    for j in graph[start]:
        distance[j[0]] = j[1]  # 디스턴스 테이블 초기화

    # 시작 노드를 제외한 n-1개 노드에 대해 반복
    for i in range(n-1):
        # 현재 최단 거리가 가장 짧은 노드 확인
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if distance[j[0]] > cost:
                distance[j[0]] = cost


dijkstra(start)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n+1):
    if distance[i] == INF:
        print('INFINITY')
    else:
        print(distance[i])
