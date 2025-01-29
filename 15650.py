import sys
input = sys.stdin.readline

def backtrack(start, path):
    if len(path) == M:  # M개의 숫자를 선택했으면 출력
        print(*path)
        return

    for i in range(start, N+1):  # start부터 N까지 탐색
        backtrack(i + 1, path + [i])  # 선택한 숫자를 path에 추가하고 진행

N, M = map(int, input().split())  # N과 M 입력 받기
backtrack(1, [])  # 백트래킹 시작
