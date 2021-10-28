n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(input()))
food = 0
burrows = []
position = 0, 0


def check_inside(position):
    y, x = position
    if x in range(0, len(matrix)) and y in range(0, len(matrix)):
        return True
    else:
        return False


def move(command, y, x):
    matrix[y][x] = '.'
    if command == 'down':
        position = (y + 1, x)
        return position

    elif command == 'up':
        position = (y - 1, x)
        return position
    elif command == 'right':
        position = (y, x + 1)
        return position
    elif command == 'left':
        position = (y, x - 1)
        return position


for row in range(n):
    for col in range(n):
        if matrix[row][col] == 'S':
            position = (row, col)
        elif matrix[row][col] == 'B':
            burrows.append((row, col))
y, x = position
command = input()
while food < 10:

    new_position = move(command, y, x)

    if not check_inside(new_position):
        print("Game over!")
        print(f"Food eaten: {food}")
        for row in range(n):
            print("".join([x for x in matrix[row]]))
        break
    matrix[y][x] = '.'
    y, x = new_position

    if matrix[y][x] == '*':
        matrix[y][x] = 'S'
        food += 1
    elif new_position in burrows:
        burrows.remove(new_position)
        matrix[y][x] = '.'
        new_position = burrows.pop()
        y, x = new_position
        matrix[y][x] = 'S'
    elif matrix[y][x] == '-':
        matrix[y][x] = 'S'
    if food >= 10:
        print("You won! You fed the snake.")
        print(f"Food eaten: {food}")
        for row in range(n):
            print("".join([x for x in matrix[row]]))
        break
    command = input()


