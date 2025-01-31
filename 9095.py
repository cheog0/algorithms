import sys
input = sys.stdin.readline

def li(num):
    li = [0] * (num + 1)
    li[0] = 1
    for i in range(1,num+1):
        if i >= 1:
            li[i] += li[i - 1]
        if i >= 2:
            li[i] += li[i - 2]
        if i >= 3:
            li[i] += li[i - 3]
    return li[num]

N = int(input())
for _ in range(N):
    K = int(input())
    result = li(K)
    print(result)