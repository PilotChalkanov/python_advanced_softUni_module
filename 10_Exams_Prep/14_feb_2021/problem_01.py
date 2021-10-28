from collections import deque

fire_works = deque([int(x) for x in input().split(', ')])
explosive_power = [int(x) for x in input().split(', ')]
completed = {
    "Palm Fireworks": 0,
    "Willow Fireworks" : 0,
    "Crossette Fireworks" : 0
}

while fire_works and explosive_power:
    current_fire_work = fire_works[0]
    current_explosive_power = explosive_power[-1]

    if current_explosive_power <=0:
        explosive_power.pop()

    elif current_fire_work <= 0:
        fire_works.popleft()

    elif (current_explosive_power+current_fire_work) % 15 ==0:
        fire_works.popleft()
        explosive_power.pop()
        completed["Crossette Fireworks"] += 1

    elif (current_explosive_power+current_fire_work) % 5 == 0:
        fire_works.popleft()
        explosive_power.pop()
        completed["Willow Fireworks"]+=1
    elif (current_explosive_power+current_fire_work) % 3 ==0:
        fire_works.popleft()
        explosive_power.pop()
        completed["Palm Fireworks"]+=1
    else:

        current_fire_work = fire_works.popleft() -1
        fire_works.append(current_fire_work)


    ready_bombs = [int(x) for x in completed.values() if int(x) >= 3]
    if len(ready_bombs) >=3:
        print("Congrats! You made the perfect firework show!")
        break

if len(ready_bombs) < 3:
    print("Sorry. You can't make the perfect firework show.")
if fire_works:
    print(f"Firework Effects left: {', '.join(str(x) for x in fire_works)}")
if explosive_power:
    print(f"Explosive Power left: {', '.join(str(x) for x in explosive_power)}")

[print(f"{k}: {v}") for k,v in completed.items()]


