from collections import deque
green_light_dur = int(input())
free_window_dur = int(input())
current_green_light = green_light_dur
car_lane = deque()
is_crash = False
car_passed =0

car = input()


while car != 'END':



    if not car == 'green':
        
        car_lane.append(car)
    current_green_light = green_light_dur
    while car == 'green' and car_lane:
        total_time = current_green_light + free_window_dur
        current_car = car_lane[0]

        if len(car_lane[0]) < current_green_light:
            current_green_light -= len(car_lane[0])
            car_lane.popleft()
            car_passed+=1
            continue
        elif len(car_lane[0]) == current_green_light:
            car_lane.popleft()
            car_passed += 1
            break

        elif len(car_lane[0]) > current_green_light and len(car_lane[0]) <= total_time:
            car_lane.popleft()
            car_passed+=1
            break
        elif len(car_lane[0]) > total_time:
            print("A crash happened!")
            print(f"{car_lane[0]} was hit at {current_car[total_time]}.")
            is_crash = True
            break



    if is_crash:
        break
    car = input()
if not is_crash:
    print("Everyone is safe.")
    print(f"{car_passed} total cars passed the crossroads.")



