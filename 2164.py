from collections import deque

num = int(input())

queue = deque()

for i in range(1, num + 1):
    queue.append(i)

while len(queue) >= 2:
    for _ in range(2):
        num = queue.popleft()
    queue.append(num)

print(queue)
