import sys
import heapq
from heapq import heappop, heappush

input = sys.stdin.readline 

def prim(start):
    pq = [(0, start)]
    visited = [0] * (N+1)
    min_w = 0
    
    while pq:
        weight, node = heappop(pq)
        
        if visited[node]:
            continue
        
        visited[node] = 1
        min_w += weight
        
        for next_weight, next_node in graph[node]:
            if visited[next_node]:
                continue
            
            heappush(pq, (next_weight, next_node))
    
    return min_w

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))
result = prim(1)

print(result)