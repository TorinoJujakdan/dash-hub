from itertools import combinations
from collections import deque

n = int(input())
pop = [0] + list(map(int, input().split()))
case_list = list(range(1, n + 1))

# 인접 리스트 그래프
graph = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    info = list(map(int, input().split()))
    graph[i] = info[1:]

def bfs(group):
    start = group[0]
    q = deque([start])
    visited = set([start])

    while q:
        curr = q.popleft()
        for next_node in graph[curr]:
            if next_node in group and next_node not in visited:
                visited.add(next_node)
                q.append(next_node)
    
    return len(visited) == len(group)

ans = float('inf')

for i in range(1, n//2 + 1):
    for a_comb in combinations(case_list, i):
        a = list(a_comb)
        b = [x for x in case_list if x not in a]

        if bfs(a) and bfs(b):
            sum_a = sum(pop[node] for node in a)
            sum_b = sum(pop[node] for node in b)

            ans = min(ans, abs(sum_a - sum_b))

if ans == float('inf'):
    print(-1)
else:
    print(ans)
