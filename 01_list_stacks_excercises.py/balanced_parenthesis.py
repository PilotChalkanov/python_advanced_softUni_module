expression = input()

stack = []
is_balanced = True
for ch in expression:
    if ch in '({[':
        stack.append(ch)
    else:
        if len(stack) == 0:
            is_balanced = False
            break
        last_open_bracket = stack.pop()
        pair = f"{last_open_bracket}{ch}"
        if pair not in '(){}[]':
            is_balanced = False
            break
    if is_balanced == False:
        break

if is_balanced and len(stack) == 0:
    print('YES')
else:
    print("NO")
    

            




    
        
