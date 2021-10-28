init_presents = int(input())
n = int(input())
matrix = [input().split() for row in range(n)]
presents_delivered = 0
def check_inside(santa_position):
    y, x = santa_position
    if y not in range(0, len(matrix)) or x not in range(0, len(matrix)):
        return False
    return True

def santa_movement(position, command, matrix):
    y, x = position
    matrix[y][x] = '-'
    if command == 'down':
        position = y + 1, x
    elif command == 'up':
        position = y - 1, x
    elif command == 'right':
        position = y, x + 1
    elif command == 'left':
        position = y, x - 1
    return position

def field_update(santa_position,bad_kids,good_kids,cookies,matrix,presents):
    y,x = santa_position
    if santa_position in bad_kids:
        bad_kids.remove(santa_position)
        matrix[y][x] = 'S'
    elif santa_position in good_kids:
        good_kids.remove(santa_position)
        matrix[y][x] = 'S'
        presents -=1
    elif santa_position in cookies:
        matrix[y][x] = 'S'
        cookies.remove(santa_position)
        if (y+1,x) in good_kids:
            good_kids.remove((y+1,x))
            presents -= 1
        elif (y+1,x) in bad_kids:
            presents -=1
        matrix[y+1][x] == '-'
        if (y-1,x) in good_kids:
            presents -= 1
            good_kids.remove((y-1),x)
        elif (y-1,x) in bad_kids:
            presents -=1
        matrix[y-1][x] = '-'
        if (y,x+1) in good_kids:
            presents -= 1
            good_kids.remove((y,x+1))
        elif (y,x+1) in bad_kids:
            presents -=1
        matrix[y][x+1] = '-'
        if (y,x-1) in good_kids:
            good_kids.remove((y,x-1))
            presents -= 1
        elif (y,x-1) in bad_kids:
            presents -=1
        matrix[y][x-1] = '-'
    matrix[y][x] = 'S'
    return matrix,presents

def positioning(matrix):
    santa_position = [(row,col) for col in range(n) for row in range(n) if matrix[row][col] == 'S'].pop()
    bad_kids = [(row,col) for col in range(n) for row in range(n) if matrix[row][col] == 'X']
    good_kids = [(row,col) for col in range(n) for row in range(n) if matrix[row][col] == 'V']
    cookies = [(row,col) for col in range(n) for row in range(n) if matrix[row][col] == 'C']
    presents_to_give = len(good_kids)
    return santa_position,bad_kids, good_kids,cookies,presents_to_give

command = input()
santa_position, bad_kids, good_kids, cookies,presents_to_give = positioning(matrix)
while command != "Christmas morning":
    if check_inside(santa_position):
        santa_position = santa_movement(santa_position,command,matrix)
        matrix, init_presents = field_update(santa_position,bad_kids,good_kids,cookies,matrix,init_presents)

    if init_presents <= 0:
        print("Santa ran out of presents!")
        [print(" ".join(r)) for r in matrix]
        break
    command = input()


if not good_kids:
    [print(" ".join(r)) for r in matrix]
    print(f"Good job, Santa! {presents_to_give} happy nice kid/s.")

else:
    print(f"No presents for {len(good_kids)} nice kid/s.")