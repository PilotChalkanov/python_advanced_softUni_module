n = int(input())
matrix = []
for r in range(n):
    matrix.append(input().split())
start_position = 0, 0
for y in range(n):
    for x in range(n):
        if matrix[y][x] == 'B':
            start_position = y, x

def is_safe(y, x, matrix):
    if x in range(0, n) and y in range(0, n) and matrix[y][x] != 'X':
        return True
    else:
        return False

#down,up,right,left
start_y,start_x = start_position
track = {
    'up': {'path':[],'points': 0},
    'down': {'path':[],'points': 0},
    'left': {'path':[],'points': 0},
    'right': {'path':[],'points': 0},
}
path_list = [0,'up','down','left','right']
command = path_list.pop()
while path_list:
    curr_points = 0
    if command == 'right':
        start_x +=1
        if is_safe(start_y,start_x,matrix):
            track['right']['path'].append((start_y,start_x))
            current_num = int(matrix[start_y][start_x])
            curr_points += current_num
            track['right']['points'] += curr_points
        else:
            command = path_list.pop()
            start_y, start_x = start_position
            continue
    elif command == 'left':
        start_x -=1
        if is_safe(start_y,start_x,matrix):
            track['left']['path'].append((start_y,start_x))
            current_num = int(matrix[start_y][start_x])
            curr_points += current_num
            track['left']['points'] = curr_points
        else:
            command = path_list.pop()
            start_y,start_x = start_position
            continue
    elif command == 'down':
        start_y +=1
        if is_safe(start_y,start_x,matrix):
            track['down']['path'].append((start_y,start_x))
            current_num = int(matrix[start_y][start_x])
            curr_points += current_num
            track['down']['points'] += curr_points
        else:
            command = path_list.pop()
            start_y, start_x = start_position
            continue
    elif command == 'up':
        start_y -=1
        if is_safe(start_y,start_x,matrix):
            track['up']['path'].append((start_y,start_x))
            current_num = int(matrix[start_y][start_x])
            curr_points += current_num
            track['up']['points'] += curr_points
        else:

            start_y,start_x = start_position
            command=path_list.pop()
track_in_list = track.items()
track_in_list_sorted = sorted(track_in_list, key=lambda x: -x[1]['points'])
print(track_in_list_sorted[0][0])
for v in track_in_list_sorted[0][1]['path']:
    y1,x1 = v
    print(f"[{y1}, {x1}]")
print(track_in_list_sorted[0][1]['points'])



