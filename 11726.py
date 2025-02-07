import sys
input = sys.stdin.readline

n = int(input())

# DP 테이블 초기화
dp = [0] * (n + 1)
dp[1] = 1
if n > 1:
    dp[2] = 2

# 점화식 적용
for i in range(3, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 10007

print(dp[n])
