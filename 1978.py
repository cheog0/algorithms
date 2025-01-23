import math
import sys
input = sys.stdin.readline

def isPrime(x):
    if x == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True

N, M = map(int, input().split())

for i in range(N,M+1):
    if isPrime(i):
        print(i)
    else:
        pass