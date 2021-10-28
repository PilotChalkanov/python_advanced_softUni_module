from collections import deque
people = deque()
water_in_tank = int(input())
commands = input()
while not commands == 'Start':
    people.append(commands)

    commands = input()

commands = input()
while not commands == "End":
    commands = commands.split()
    if not len(commands) == 1:
        liters = int(commands[0])
        if liters <= water_in_tank:
            print(f"{people.popleft()} got water")
            water_in_tank -= liters
        else:
            print(f"{people.popleft()} must wait")
    else:
        action, liters = commands
        liters = int(liters)
        water_in_tank += liters
    commands = input()

print(f"{water_in_tank} liters left")


        
    
