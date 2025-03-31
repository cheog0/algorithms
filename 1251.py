def split_and_reverse(word):
    n = len(word)
    min_word = word  # 초기값은 원래 단어로 설정 (나중에 비교용)

    # 두 지점 i, j를 정하여 세 부분으로 나누기
    for i in range(1, n - 1):  # i는 첫 번째 부분의 끝 (1부터 n-2까지)
        for j in range(i + 1, n):  # j는 두 번째 부분의 끝 (i+1부터 n까지)
            # 세 부분으로 나누기
            part1 = word[:i]  # 첫 번째 부분
            part2 = word[i:j]  # 두 번째 부분
            part3 = word[j:]  # 세 번째 부분

            # 각 부분을 뒤집고 합치기
            new_word = part1[::-1] + part2[::-1] + part3[::-1]

            # 사전순으로 가장 작은 단어 찾기
            if new_word < min_word:
                min_word = new_word

    return min_word


# 입력
word = input().strip()

# 결과 출력
print(split_and_reverse(word))
