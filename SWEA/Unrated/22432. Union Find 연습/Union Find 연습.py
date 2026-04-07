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


T = int(input())
for tc in range(1, T + 1):
    
    n, q = map(int, input().split())
    parents = list(range(n+1))
    print(f"#{tc}", end=" ")
    for _ in range(q):
        k, A, B = map(int, input().split())

        if k == 1:
            union(A, B)
        
        elif k == 0:
            if find(A) == find(B):
                print("YES", end=" ")
            else:
                print("NO", end=" ")