# define the matrix, Alice-position and tea bags positions
n = int(input())
matrix = []
[matrix.append(input().split()) for row in range(n)]

position = [(row, col) for row in range(n) for col in range(n) if matrix[row][col] == 'A'].pop()
tea_bags = {(row, col) for row in range(n) for col in range(n) if matrix[row][col].isdigit()}
rabit_hole = [(row, col) for row in range(n) for col in range(n) if matrix[row][col] == 'R'].pop()


# check the positions inside
def check_inside(matrix, position, rabit_hole):
    y, x = position
    if y not in range(0, len(matrix)) or x not in range(0, len(matrix)):
        return False
    if position == rabit_hole:
        matrix[y][x] = '*'
        return False
    return True


# execute the commands from the input
def movement(position, command, matrix):
    y, x = position
    matrix[y][x] = '*'
    if command == 'down':
        position = y + 1, x
    elif command == 'up':
        position = y - 1, x
    elif command == 'right':
        position = y, x + 1
    elif command == 'left':
        position = y, x - 1
    return position


# update the field as neccessary with '*' markings
def playground_update(matrix, position, teabags_count, tea_bags):
    y, x = position

    if matrix[y][x].isdigit():
        teabags_count += int(matrix[y][x])
        tea_bags.remove((y, x))
        matrix[y][x] = '*'

    else:
        matrix[y][x] = '*'
    return matrix, teabags_count

command = input()
# the main loop, execute until bags >= 10 or if she goes out of the field
teabags_count = 0
while True:
    position = movement(position, command, matrix)
    if check_inside(matrix, position, rabit_hole):
        matrix, teabags_count = playground_update(matrix, position, teabags_count, tea_bags)
    else:

        print("Alice didn't make it to the tea party.")
        [print(" ".join(r)) for r in matrix]
        break
    if teabags_count >= 10:
        print("She did it! She went to the party.")
        [print(" ".join(r)) for r in matrix]
        break
    command = input()


a = 5
