import sys
input = sys.stdin.readline


def main():
    # 입력 받기
    N = int(input())
    members = [input().strip().split() for _ in range(N)]

    # 정렬: 나이순, 가입 순서순 (입력 순서를 유지)
    members.sort(key=lambda x: int(x[0]))

    # 출력
    for age, name in members:
        print(age, name)


if __name__ == "__main__":
    main()
