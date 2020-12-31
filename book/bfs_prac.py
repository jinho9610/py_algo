from collections import deque


def bfs(graph, start, visited):
    queue = deque([start])  # 가장 첫 노드 삽입하고
    visited[start] = True  # 현재 노드 방문 처리

    while queue:  # 큐가 빌 때 까지
        v = queue.popleft()  # 원소 하나 뽑고
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False]*9

bfs(graph, 1, visited)
