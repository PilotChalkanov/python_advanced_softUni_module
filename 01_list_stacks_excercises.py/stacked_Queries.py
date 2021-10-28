n = int(input())
stack =[]
commands = {
    '1' : lambda x: stack.append(x),
    '2' : stack.pop(),
    '3' : max(stack),
    '4' : min(stack),
}

for _ in range(n):
    line = input().split()
    command = line[0]
    if len(line) > 1:
        num = int(line[1])
    action = commands[command]
    if len(line)>1:
        action(num)
    else:   
        action()


    print(action)