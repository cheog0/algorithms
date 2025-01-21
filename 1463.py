def make_one(n):
    # DP 테이블 초기화
    dp = [0] * (n + 1)

    # 2부터 n까지 계산
    for i in range(2, n + 1):
        # 1을 뺀 경우
        dp[i] = dp[i - 1] + 1

        # 2로 나누어 떨어질 경우
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)

        # 3으로 나누어 떨어질 경우
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)

    return dp[n]

# 입력
n = int(input())
print(make_one(n))
