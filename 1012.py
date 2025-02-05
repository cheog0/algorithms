import sys
from collections import deque

input = sys.stdin.readline

num = int(input())  # 테스트 케이스 개수

def BFS(k_map, visited, start_x, start_y, M, N):
    """ 주어진 배추밭에서 (start_x, start_y)에서 시작하는 BFS 탐색 """
    queue = deque()
    queue.append((start_x, start_y))
    visited[start_x][start_y] = True

    # 이동 방향 (상, 하, 좌, 우)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y = queue.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < M and 0 <= ny < N:  # 배추밭 범위 내에 있고
                if not visited[nx][ny] and k_map[nx][ny] == 1:  # 방문하지 않은 배추라면
                    visited[nx][ny] = True
                    queue.append((nx, ny))

for _ in range(num):
    M, N, count = map(int, input().split())

    # 배추밭 초기화
    k_map = [[0] * N for _ in range(M)]
    visited = [[False] * N for _ in range(M)]

    # 배추 위치 입력
    for _ in range(count):
        s, y = map(int, input().split())
        k_map[s][y] = 1

    worm_count = 0  # 지렁이 개수 (배추 덩어리 개수)

    for i in range(M):
        for j in range(N):
            if k_map[i][j] == 1 and not visited[i][j]:  # 배추가 있고, 방문하지 않았다면
                BFS(k_map, visited, i, j, M, N)
                worm_count += 1  # 새로운 배추 덩어리 발견

    print(worm_count)  # 현재 테스트 케이스의 지렁이 개수 출력
