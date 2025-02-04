import sys
input = sys.stdin.readline

num = int(input())
li = []
for i in range(num):
    K = list(map(int,input().split()))
    li.append(K)
li.sort()
for i in li:
    print(' '.join(map(str,i)))