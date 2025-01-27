import sys
from collections import Counter

input = sys.stdin.readline

M = int(input())
M_li = input().strip().split()

N = int(input())
N_li = input().strip().split()

check_count = Counter(M_li)

result = [check_count[word] for word in N_li]

print(' '.join(map(str,result)))