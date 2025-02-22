import math

num = int(input())

li = list(map(int,input().split()))

T,P = map(int,input().split())

count = sum(math.ceil(size / T) for size in li)

print(count)

a = num // P
b = num % P

print(a, b)