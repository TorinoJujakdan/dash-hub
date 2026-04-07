import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def find(x):
    if x == parents[x]:
        return x

    parents[x] = find(parents[x])
    return parents[x] 


def union(x, y):
    rep_x = find(x)
    rep_y = find(y)

    if rep_x == rep_y:
        return
    
    parents[rep_x] = rep_y

n, m= map(int, input().split())
parents = list(range(n+1))
for _ in range(m):
    num, a, b = map(int, input().split())
    if num == 0:
        union(a, b)
    elif num == 1:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
