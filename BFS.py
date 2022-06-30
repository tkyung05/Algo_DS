from collections import deque

def bfs(graph, start, visited):
    deque_data = deque([start])
    visited[start] = True

    while deque_data:
        node = deque_data.popleft()
        print(node)
        for i in graph[node]:
            if not visited[i]:
                deque_data.append(i)
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

# 방문 처리 1차원 리스트
visited = [False] * 9

# 노드 1부터 탐색 시작
bfs(graph, 1, visited)
