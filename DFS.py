def dfs(graph, v, visited):
    visited[v] = True # 현재 노드 방문 처리
    
    for i in graph[v]: # 현재 노드와 연결된 노드 탐색
        if not visited[i]: # 방문 하지 않은 노드가 있다면
            dfs(graph, i, visited) # 재귀 함수 실행

# 그래프 노드 연결 관계 2차원 리스트
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
dfs(graph, 1, visited)





