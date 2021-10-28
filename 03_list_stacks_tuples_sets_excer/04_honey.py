from collections import deque
import math
bees = deque([int(x) for x in input().split()])
nectar = [int(x) for x in input().split()]
symbols = deque(input().split())

honey = 0
operators = {
    '+': lambda x,y:x + y ,
    '-': lambda x,y:x - y ,
    '*': lambda x,y:x * y ,
    '/': lambda x,y:x / y ,
}
while bees and nectar:
    cur_bee = bees[0]
    cur_nectar = nectar[-1]
    if cur_bee > cur_nectar:
        nectar.pop()
        continue
    elif cur_bee <= cur_nectar:
        cur_symbol = symbols.popleft()
        honey += abs(operators[cur_symbol](bees.popleft(),nectar.pop()))

print(f"Total honey made: {honey}")
if bees:
    print(f"Bees left: {', '.join([str(x) for x in bees])}")
elif nectar:
    print(f"Nectar left: {', '.join([str(x) for x in nectar])}")




