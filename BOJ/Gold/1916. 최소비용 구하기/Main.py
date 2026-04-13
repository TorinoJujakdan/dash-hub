import sys
import heapq
from heapq import heappop, heappush

input = sys.stdin.readline

def dijkstra(start):
    pq = [(0, start)]
    dists = [INF] * (N + 1)
    dists[start] = 0
    
    while pq:
        dist, node = heappop(pq)
        
        if dists[node] < dist:
            continue
        
        for next_dist, next_node in graph[node]:
            new_dist = dist + next_dist
            
            if dists[next_node] <= new_dist:
                continue
            
            dists[next_node] = new_dist
            heappush(pq, (new_dist, next_node))
            
    
    return dists
    
    
N = int(input())
M = int(input())
INF = float(20e8)
graph = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, w = map(int, input().split())
    graph[s].append((w, e))

start, end = map(int, input().split())
result = dijkstra(start)

print(result[end])