import sys
from collections import deque


def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return len(visited) - 1  # 1번 컴퓨터 제외


# 입력 처리
n = int(input())  # 컴퓨터 수
m = int(input())  # 연결된 쌍의 수

graph = {i: [] for i in range(1, n + 1)}
for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

print(bfs(graph, 1))
