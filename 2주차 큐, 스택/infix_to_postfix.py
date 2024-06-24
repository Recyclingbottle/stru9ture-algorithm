import sys
input = sys.stdin.read

# 연산자 우선순위를 정의합니다.
precedence = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '(': 0  # '('는 우선순위가 가장 낮습니다.
}

# 중위 표기식을 입력 받습니다.
infix_expression = input().strip()

stack = []  # 연산자를 저장할 스택입니다.
postfix = []  # 결과 후위 표기식을 저장할 리스트입니다.

for char in infix_expression:
    if char.isalpha():  # 피연산자 (알파벳)일 경우
        postfix.append(char)
    elif char == '(':  # 여는 괄호일 경우
        stack.append(char)
    elif char == ')':  # 닫는 괄호일 경우
        while stack and stack[-1] != '(':
            postfix.append(stack.pop())
        stack.pop()  # 여는 괄호를 스택에서 제거합니다.
    else:  # 연산자일 경우
        while stack and precedence[stack[-1]] >= precedence[char]:
            postfix.append(stack.pop())
        stack.append(char)

# 스택에 남아있는 모든 연산자를 후위 표기식에 추가합니다.
while stack:
    postfix.append(stack.pop())

# 결과 후위 표기식을 출력합니다.
print(''.join(postfix))
