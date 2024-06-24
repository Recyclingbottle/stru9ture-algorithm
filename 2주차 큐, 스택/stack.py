import sys
input = sys.stdin.read

input_data = input().splitlines()
N = int(input_data[0])
commands = input_data[1:N+1]

stack = []
results = []

for command in commands:
    if command.startswith('push'):
        _, num = command.split()
        stack.append(int(num))
    elif command == 'pop':
        if stack:
            results.append(stack.pop())
        else:
            results.append(-1)
    elif command == 'size':
        results.append(len(stack))
    elif command == 'empty':
        results.append(1 if not stack else 0)
    elif command == 'top':
        if stack:
            results.append(stack[-1])
        else:
            results.append(-1)

for result in results:
    print(result)
