import sys

input = sys.stdin.readline

num = int(input())
stair = [0] * (num + 1)
for i in range(1, num + 1):
    stair[i] = int(input())

dp = [0] * (num + 1)

if num == 1:
    print(stair[1])
    exit()
elif num == 2:
    print(stair[1] + stair[2])
    exit()
elif num == 3:
    print(max(stair[1] + stair[3], stair[2] + stair[3]))
    exit()

dp[1] = stair[1]
dp[2] = stair[1] + stair[2]
dp[3] = max(stair[1] + stair[3], stair[2] + stair[3])

for i in range(4, num + 1):
    dp[i] = max(dp[i - 2] + stair[i], dp[i - 3] + stair[i - 1] + stair[i])

print(dp[num])
