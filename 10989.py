import sys
input = sys.stdin.readline

num = int(input())

count = [0] * 10001

for _ in range(num):
    K = int(input())
    count[K] += 1

# 정렬된 출력
for i in range(10001):
    if count[i] > 0:
        for _ in range(count[i]):
            print(i)
