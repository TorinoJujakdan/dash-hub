import sys
input = sys.stdin.readline

import heapq
from heapq import heappop, heappush

def dijkstra(start):
    pq = [(0, start)]
    dists = [INF] * (V+1)
    dists[start] = 0

    while pq:
        weight, node = heappop(pq)

        if dists[node] < weight:
            continue

        for next_weight, next_node in graph[node]:
            new_weight = weight + next_weight

            if dists[next_node] <= new_weight:
                continue

            dists[next_node] = new_weight
            heappush(pq, (new_weight, next_node))
    
    return dists

V, E = map(int, input().split())
INF = float(10e8)
graph = [[] for _ in range(V+1)]
K = int(input())
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))


result = dijkstra(K)

for i in range(1, V+1):
    if result[i] == float(10e8):
        print("INF")
    else:
        print(result[i])
