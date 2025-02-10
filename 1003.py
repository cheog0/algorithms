import sys


def fibonacci_counts(n, memo):
    if n == 0:
        return (1, 0)
    elif n == 1:
        return (0, 1)
    if memo[n] != (-1, -1):
        return memo[n]

    count1 = fibonacci_counts(n - 1, memo)
    count2 = fibonacci_counts(n - 2, memo)
    memo[n] = (count1[0] + count2[0], count1[1] + count2[1])
    return memo[n]


def main():
    T = int(sys.stdin.readline().strip())
    test_cases = [int(sys.stdin.readline().strip()) for _ in range(T)]

    max_n = max(test_cases)
    memo = [(-1, -1)] * (max_n + 1)

    results = [fibonacci_counts(n, memo) for n in test_cases]

    for result in results:
        print(result[0], result[1])


if __name__ == "__main__":
    main()
