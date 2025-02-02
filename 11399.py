import sys

input = sys.stdin.readline

num = int(input())
li = list(map(int, input().split()))

li.sort()

for i in range(1, num):
    li[i] += li[i - 1]
print(sum(li))
