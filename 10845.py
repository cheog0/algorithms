import sys
from collections import deque

input = sys.stdin.readline

queue = deque()

def choice_def(command):
    if command[0] == "push":
        queue.append(command[1])
    elif command[0] == 'pop':
        print(queue.popleft() if queue else -1)
    elif command[0] == "size":
        print(len(queue))
    elif command[0] == "empty":
        print(0 if queue else 1)
    elif command[0] == "front":
        print(queue[0] if queue else -1)
    elif command[0] == "back":
        print(queue[len(queue) - 1] if queue else -1)
    else:
        print("error")

num = int(input())
for _ in range(num):
    choice_def(input().strip().split())
