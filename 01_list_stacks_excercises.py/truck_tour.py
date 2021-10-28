from collections import deque
queue = deque()
pumps_count = int(input())

for _ in range(pumps_count):
    pump = [int(el) for el in input().split()]
    queue.append(pump)

for i in range(pumps_count):
    is_complete = True
    tank_fuel= 0
    for el in queue:
        fuel_pumped, distance = el
        tank_fuel += fuel_pumped
        if tank_fuel < distance:
            is_complete = False
            break
        else:
            tank_fuel -= distance            
       
    
    if is_complete:
        print(i)
        break
    else:
        queue.append(queue.popleft())

