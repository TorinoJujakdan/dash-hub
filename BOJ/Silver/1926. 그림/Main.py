from collections import deque

n, m = map(int, input().split())

# 입력 값
board = [list(map(int, input().split())) for _ in range(n)]

# BFS 활용 위해 방문 여부 배열 만들기
visited = [[False] * m for _ in range(n)]

# 방향 탐색을 위한 delta 값 - 상하좌우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# 배열 안 범위 설정 함수
def in_range(y, x):
    return 0 <= y < n and 0 <= x < m

# BFS 함수 정의
def bfs(y, x):
    q = deque()
    q.append((y, x))
    visited[y][x] = True
    area = 1

    while q:
        cy, cx = q.popleft() # 현재 탐색할 위치를 큐에서 꺼냄

        for i in range(4):
            # 다음 이동할 곳 확인
            ny, nx = cy + dy[i], cx + dx[i]

            if in_range(ny, nx): # 범위 안이고
                if board[ny][nx] == 1 and not visited[ny][nx]: # 배열에 그림이 있고 아직 탐색 안했으면
                    visited[ny][nx] = True # 탐색한 것으로 수정
                    q.append((ny, nx)) # 다음 탐색할 위치를 큐에 추가
                    area += 1 # 그림의 넓이 증가
    return area

cnt = 0
max_area = 0

for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and not visited[i][j]:
            visited[i][j] = True
            cnt += 1
            max_area = max(max_area, bfs(i, j))

print(cnt)
print(max_area)