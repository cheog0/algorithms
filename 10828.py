import sys

input = sys.stdin.readline

# 스택 선언
stack = []


# 명령 처리 함수
def process_command(command):
    if command[0] == "push":
        stack.append(int(command[1]))
    elif command[0] == "pop":
        print(stack.pop() if stack else -1)
    elif command[0] == "size":
        print(len(stack))
    elif command[0] == "empty":
        print(1 if not stack else 0)
    elif command[0] == "top":
        print(stack[-1] if stack else -1)


# 명령 입력 및 처리
n = int(input())
for _ in range(n):
    process_command(input().strip().split())
