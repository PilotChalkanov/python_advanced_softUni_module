matrix = [input().split() for row in range(5)]
n = int(input())

init_pos = [(row, col) for col in range(5) for row in range(5) if matrix[row][col] == 'A'].pop()
targets = [(row, col) for col in range(5) for row in range(5) if matrix[row][col] == 'x']
targets_count = len(targets)
targets_shot = []


def check_inside(matrix, position):
    y, x = position
    if y or x not in range(0, 5) or matrix[y][x] == 'x':
        return False
    return True

def movement(command, step, position, matrix):
    y, x = position

    action = {
        'up': lambda y, x, step: (y - step, x),
        'down': lambda y, x, step: (y + step, x),
        'left': lambda y, x, step: (y, x - step),
        'right': lambda y, x, step: (y, x + step)
    }

    new_position = action[command](y, x, step)
    if check_inside(matrix, new_position):
        matrix[new_position[0]][new_position[1]] = 'A'
        old_y, old_x = position
        matrix[old_y][old_x] = '.'

    else:
        new_position = position
    return new_position

def shooting(command, position, matrix, targets, targets_shot):
    y, x = position

    if command == 'right':
        for col in range(x, len(matrix)):
            if matrix[y][col] == 'x':
                matrix[y][col] = '.'
                targets.remove((y, col))
                targets_shot.append((y, col))
                break
    elif command == 'left':
        for col in range(x, 0, -1):
            if matrix[y][col] == 'x':
                matrix[y][col] = '.'
                targets.remove((y, col))
                targets_shot.append((y, col))
                break
    elif command == 'down':
        for row in range(y, len(matrix)):
            if matrix[row][x] == 'x':
                matrix[row][x] = '.'
                targets.remove((row, x))
                targets_shot.append((row, x))
                break
    elif command == 'up':
        for row in range(y, 0, -1):
            if matrix[row][x] == 'x':
                matrix[row][x] = '.'
                targets.remove((row, x))
                targets_shot.append((row, x))
                break
    return targets, targets_shot


for _ in range(n):
    line = input()
    command_line = line.split()
    command = command_line[0]
    if command == 'shoot':
        shooting_direction = command_line[1]
        targets, targets_shot = shooting(shooting_direction, init_pos, matrix, targets, targets_shot)
    elif command == 'move':
        direction = command_line[1]
        step = int(command_line[2])
        init_pos = movement(direction, step, init_pos, matrix)
    if not targets:
        print(f"Training completed! All {targets_count} targets hit.")
        break

if targets:
    print(f"Training not completed! {len(targets)} targets left.")
for el in targets_shot:
    print(f"[{el[0]}, {el[1]}]")
