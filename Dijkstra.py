import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미 하는 값으로 10억을 설정

v, e = map(int, input().split()) # 노드의 개수, 간선의 개수
start = int(input()) # 시작 노드 번호
`
graph = [[] for _ in range(v + 1)] # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트

distance = [INF] * (v + 1) # 각 노드의 최단 거리 테이블을 모두 무한으로 초기화

# 모든 간선 정보 받기
for _ in range(e):
    n1, n2, d = map(int, input().split())
    graph[n1].append((n2, d)) # n1번 노드에서 n2 노드로 가는 비용이 d 라는 의미  



def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

dijkstra(start)

for i in range(1, v + 1):
    if distance[i] == INF:
        print('infinity')
    else:
        print(distance[i])