from collections import deque
from math import floor

class Robot:
    def __init__(self,name,processing_time):
        self.name = name
        self.processing_time = processing_time
        self.busy_until = 0

def get_time_in_seconds(string):
    h,min, sec = string.split(':')
    time_in_seconds = int(h) *60**2 + int(min)*60 + int(sec)
    return time_in_seconds

def get_time_from_seconds(sec):
    sec = sec % (24 * 3600)
    hour = sec // 3600
    min = floor((sec / 60) % 60)
    sec %= 60
    return f"{hour:02d}:{min:02d}:{sec:02d}"

robots = []
robots_input = input().split(';')
for robot_input in robots_input:
    robot_name,processing_time = robot_input.split('-')
    robots.append(Robot(robot_name,int(processing_time)))

time_in_sec = get_time_in_seconds(input())
items = deque()
while True:
    item = input()
    if item == 'End':
        break
    items.append(item)
while items:
    current_item = items.popleft()
    time_in_sec +=1
    found_robot = False
    for robot in robots:
        if time_in_sec >= robot.busy_until:
            robot.busy_until = time_in_sec + robot.processing_time
            found_robot = True
            print(f'{robot.name} - {current_item} [{get_time_from_seconds(time_in_sec)}]')
            break
    if not found_robot:
        items.append(current_item)


