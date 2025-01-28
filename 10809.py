import sys
input = sys.stdin.readline

alphabet = "abcdefghijklmnopqrstuvwxyz"

word = input().strip()

for i in alphabet:
    A = word.find(i)    # find는 처음으로 발견된 위치를 반환하고 존재하지 않으면 -1 리턴
    print(A, end = ' ')