# 1138번 한 줄로 서기 

# 입력 받기 
n = int(input()) # 사람 수 
input_arr = list(map(int, input().split())) # 각 사람이 기억하는 왼쪽에 큰 사람 수 

result = [0] * n # 결과, 0이면 아직 비어있다는 뜻
# 키가 1부터 시작해서 왼쪽에 있어야 하는 큰 사람의 수만큼 빈자리 찾기 
for height in range(1, n+1):
    count = input_arr[height-1] #키가 height 인 사람의 왼쪽에 키 큰 사람 수 
    position = 0

    # 빈 자리 중에서 count 만큼 큰 사람이 있는 자리를 찾기
    while count > 0 or result[position] != 0:
        if result[position] == 0:
            count -= 1
        position += 1
    #해당 자리에 현재 사람의 키를 배치
    result[position] = height

print(" ".join(map(str, result)))
