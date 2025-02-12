import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[0] for _ in range(N + 1)]
in_degree = [0] * (N + 1)

for i in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    in_degree[B] += 1

pq = []
for i in range(1, N + 1):
    if in_degree[i] == 0:
        heapq.heappush(pq, i)

result = []
while pq:
    now = heapq.heappop(pq)
    result.append(now)

    for nxt in graph[now]:
        in_degree[nxt] -= 1
        if in_degree[nxt] == 0:
            heapq.heappush(pq, nxt)

print(' '.join(map(str, result)))
