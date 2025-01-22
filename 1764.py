# 입력 받기
import sys
input = sys.stdin.readline


N,M = map(int,input().split())

heard = {input().strip() for _ in range(N)}
seen = {input().strip() for _ in range(M)}

# 듣보잡 구하기
intersection = sorted(heard & seen)

# 결과 출력
print(len(intersection))
print("\n".join(intersection))
