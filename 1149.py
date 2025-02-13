import sys
input = sys.stdin.readline

n = int(input())  # 집 개수
costs = [list(map(int, input().split())) for _ in range(n)]  # 각 집의 색칠 비용

# DP 테이블 초기화
dp = [[0] * 3 for _ in range(n)]
dp[0] = costs[0]  # 첫 번째 집의 색칠 비용은 그대로 사용

# DP 진행
for i in range(1, n):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]  # 현재 빨강 선택
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]  # 현재 초록 선택
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]  # 현재 파랑 선택

# 최종 최소 비용 출력
print(min(dp[n-1]))
