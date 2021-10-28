from collections import deque
expression = deque(input().split())
actions = {
    '+': lambda x,y:x + y ,
    '-': lambda x,y:x - y ,
    '*': lambda x,y:x * y ,
    '/': lambda x,y:x // y ,

}

nums = deque()
for el in expression:
    if el not in actions:
        nums.append(int(el))
    if el in actions:
        while len(nums) != 1:
            x=nums.popleft()
            y=nums.popleft()
            result = actions[el](x,y)
            nums.appendleft(result)
print(result)



