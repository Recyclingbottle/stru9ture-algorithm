import sys

input = sys.stdin.read

brackets = input().strip()

stack = []
temp = 1
result = 0

for i in range(len(brackets)):
    if brackets[i] == '(':
        # 여는 소괄호를 만나면 스택에 추가하고, 현재 값에 2를 곱해준다.
        stack.append(brackets[i])
        temp *= 2
    elif brackets[i] == '[':
        # 여는 대괄호를 만나면 스택에 추가하고, 현재 값에 3을 곱해준다.
        stack.append(brackets[i])
        temp *= 3
    elif brackets[i] == ')':
        # 닫는 소괄호를 만나면
        if not stack or stack[-1] == '[':
            # 스택이 비어있거나, 스택의 top이 대괄호이면 잘못된 괄호열이므로 0을 반환한다.
            result = 0
            break
        if brackets[i-1] == '(':
            # 이전 문자가 여는 소괄호인 경우 현재의 temp 값을 결과에 더해준다.
            result += temp
        # 스택에서 여는 소괄호를 제거하고, 현재 값을 2로 나눈다.
        stack.pop()
        temp //= 2
    elif brackets[i] == ']':
        # 닫는 대괄호를 만나면
        if not stack or stack[-1] == '(':
            # 스택이 비어있거나, 스택의 top이 소괄호이면 잘못된 괄호열이므로 0을 반환한다.
            result = 0
            break
        if brackets[i-1] == '[':
            # 이전 문자가 여는 대괄호인 경우 현재의 temp 값을 결과에 더해준다.
            result += temp
        # 스택에서 여는 대괄호를 제거하고, 현재 값을 3으로 나눈다.
        stack.pop()
        temp //= 3

# 모든 과정을 마친 후 스택이 비어있지 않다면 잘못된 괄호열이므로 0을 반환한다.
if stack:
    result = 0

# 최종 결과를 출력한다.
print(result)
