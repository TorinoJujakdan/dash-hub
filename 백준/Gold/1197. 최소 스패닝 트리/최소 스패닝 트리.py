import sys
input = sys.stdin.readline

import heapq
from heapq import heappop, heappush

def prim(start):
    pq = [(0, start)]
    visited = [0] * (V+1)
    min_w = 0

    while pq:
        weight, node = heappop(pq) # 가장 작은거 빼기

        if visited[node]:
            continue

        visited[node] = 1
        min_w += weight

        for next_weight, next_node in graph[node]:
            if visited[next_node]:
                continue

            heappush(pq, (next_weight, next_node))
    
    return min_w

V, E = map(int, input().split())
graph = [[] * (V+1) for _ in range(V+1)]
for _ in range(E):
    a, b, w = map(int, input().split())
    graph[a].append((w, b))
    graph[b].append((w, a))

result = prim(1)
print(result)