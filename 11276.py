import heapq
import sys
input = sys.stdin.readline

result = []
max_heap = []

num = int(input())

for i in range(num):
    K = int(input())
    if K != 0:
        heapq.heappush(max_heap, -K)
    else:
        if len(max_heap) > 0:
            p_num = -heapq.heappop(max_heap)
            result.append(p_num)
        else:
            result.append(0)
for i in result:
    print(i)

