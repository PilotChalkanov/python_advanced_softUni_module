n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(input()))


def inside_the_field(x, y):
    if x in range(0, len(matrix[0])) and y in range(0, len(matrix)):
        return True
    return False


def knights_in_conflict(current_pos, matrix):
    y = current_pos[0]
    x = current_pos[1]
    max_counter = 0
    if inside_the_field(y - 2, x - 1) and matrix[y - 2][x - 1] == 'K':
        max_counter += 1
    if inside_the_field(y - 2, x + 1) and matrix[y - 2][x + 1] == 'K':
        max_counter += 1
    if inside_the_field(y + 2, x - 1) and matrix[y + 2][x - 1] == 'K':
        max_counter += 1
    if inside_the_field(y + 2, x + 1) and matrix[y + 2][x + 1] == 'K':
        max_counter += 1

    if inside_the_field(y - 1, x + 2) and matrix[y - 1][x + 2] == 'K':
        max_counter += 1
    if inside_the_field(y - 1, x - 2) and matrix[y - 1][x - 2] == 'K':
        max_counter += 1
    if inside_the_field(y + 1, x - 2) and matrix[y + 1][x - 2] == 'K':
        max_counter += 1
    if inside_the_field(y + 1, x + 2) and matrix[y + 1][x + 2] == 'K':
        max_counter += 1

    return max_counter



conflicts_valid = True
knights_count = 0
while conflicts_valid:

    max_count,max_y,max_x = 0,0,0
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            current_pos = (y, x)
            if matrix[y][x] == 'K':
                init_count = knights_in_conflict(current_pos, matrix)
                if init_count>max_count:
                    max_count,max_y,max_x = init_count,y,x
            else:
                continue
    if max_count == 0:
        break
    matrix[max_y][max_x] = '0'
    knights_count +=1



print(knights_count)
