def min_expression(expression):
    # '-' 기준으로 나누기
    groups = expression.split('-')

    # 첫 번째 그룹은 더하기 연산 후 그대로 사용
    first_sum = sum(map(int, groups[0].split('+')))

    # 나머지 그룹은 모두 더한 후 빼기
    result = first_sum - sum(sum(map(int, group.split('+'))) for group in groups[1:])

    return result

# 입력 받기
expression = input().strip()
print(min_expression(expression))
