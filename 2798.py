import sys
from itertools import combinations

input = sys.stdin.readline

def blackjack(N, M, cards):
    max_sum = 0
    for comb in combinations(cards, 3):
        card_sum = sum(comb)
        if card_sum <= M and card_sum > max_sum:
            max_sum = card_sum
    return max_sum


# 입력
N, M = map(int, input().split())
cards = list(map(int, input().split()))

# 출력
print(blackjack(N, M, cards))
