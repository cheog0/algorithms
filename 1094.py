def solve(X):
    # X의 이진수 표현에서 1이 있는 자리의 개수를 세면 그게 답입니다.
    return bin(X).count('1')

# 입력 받기
X = int(input())

# 결과 출력
print(solve(X))
