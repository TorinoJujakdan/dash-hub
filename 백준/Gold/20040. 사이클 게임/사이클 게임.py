import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

# unionfind
def find(x):
    if x == parents[x]:
        return x
    
    parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    rep_x = find(x)
    rep_y = find(y)

    if rep_x == rep_y:
        return False
    
    parents[rep_y] = rep_x
    return True

n, m = map(int, input().split())
parents = list(range(n))
result = 0
cnt = 0
for _ in range(m):
    s, e = map(int, input().split())
    cnt += 1

    if result != 0:
        continue

    if not union(s, e):
        result = cnt
        
    
print(result)

