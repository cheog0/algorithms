import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
sorted_indices = sorted(range(N), key=lambda i: B[i],reverse=True)
result = 0
for i in range(N):
    result += A[i] * B[sorted_indices[i]]

print(result)
