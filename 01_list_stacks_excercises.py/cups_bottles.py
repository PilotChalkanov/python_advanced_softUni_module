from collections import deque

cups = deque([int(cup) for cup in input().split(' ')])
bottles = list([int(cup) for cup in input().split(' ')])
wasted_water = 0
while cups and bottles:
    current_bottle = bottles.pop()
    current_cup = cups[0]
    if current_bottle >= current_cup:
        cups.popleft()
        wasted_water += (current_bottle-current_cup)

    elif current_bottle <= current_cup:
        cups[0] -= current_bottle

if cups:
    print(f'Cups: {" ".join([str(x) for x in cups])}')
    print(f"Wasted litters of water: {wasted_water}")
if bottles:
    print(f'Bottles: {" ".join([str(x) for x in bottles])}')
    print(f"Wasted litters of water: {wasted_water}")

