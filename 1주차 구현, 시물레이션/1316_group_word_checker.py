# 1316번 그룹 단어 체커

# 먼저, 입력을 받는다. 
n = int(input())
input_words = []
for i in range(n):
    input_words.append(input())

result = 0 # 그룹 단어의 갯수
# 그룹 단어인지 아닌지 체크하고 그룹 단어라면 result에 1을 더하고 아니라면 다음 단어로 넘어간다
for word in input_words:
    is_group_word = True # 그룹 단어 인지 아닌 지 
    seen_characters = set() # 이때까지 나온 한 글자를 저장할 집합
    previous_char = '' # 이전에 나온 글자

    for char in word:
        # 한 단어의 한 글자 마다 
        if char != previous_char:
            # 선택된 한글자가 이전에 나온 글자와 다르면
            if char in seen_characters:
                # 또한, 이때까지 있는 단어 집합에 있으면 
                # 그룹 단어가 아님
                is_group_word = False # 아닌걸로 바꿔주고 
            seen_characters.add(char) # 선택된 한 글자를 집합에 넣어주고 
        previous_char = char # 현재 선택된 글자를 이전 글자로 바꿔줌
    if is_group_word: # 한 단어의 그룹 단어인지 아닌지 확인이 끝나면 
        result += 1 # 값을 증가 시킴

print(result)