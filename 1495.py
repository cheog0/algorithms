# n = 곡의 개수 s=시작 볼륨 M=최대값

import sys

input = sys.stdin.readline

N, S, M = map(int, input().split())
vol_li = list(map(int, input().split()))

dp = [[False] * (M + 1) for _ in range(N + 1)]
dp[0][S] = True

for i in range(1, N + 1):
    for k in range(M + 1):
        if dp[i - 1][k]:
            num2 = k + vol_li[i - 1]
            if 0 <= num2 <= M:
                dp[i][num2] = True
            num = dp[i - 1][k] - vol_li[i - 1]
            if 0 <= num <= M:
                dp[i][num] = True

result = -1
for i in range(M + 1):
    if dp[N][i]:
        result = max(result, i)
print(result)
