import heapq
import sys

input = sys.stdin.readline

n = int(input())

hq = []
for i in range(n):
    info = int(input())
    if info > 0:
        heapq.heappush(hq, -info)
    else:
        if len(hq) == 0:
            print(0)
        else:
            print(-heapq.heappop(hq))