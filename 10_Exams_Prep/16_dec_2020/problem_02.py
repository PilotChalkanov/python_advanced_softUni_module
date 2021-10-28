text = input()
n = int(input())
matrix = [list(input()) for _ in range(n)]
player_position = [(y,x) for y in range(n) for x in range(n) if matrix[y][x] == 'P'].pop()
commands_count = int(input())

def check_inside(matrix,position):
    y,x = position
    if y in range(0,n) and x in range(0,n):
        return True
    else:
        return False

def movement(command,matrix,player_position,text):
    y,x = player_position
    matrix[y][x] = '-'
    directions = {
        "up" : lambda y,x: (y-1,x),
        "down": lambda y,x: (y+1,x),
        "right": lambda y,x: (y,x+1),
        "left" : lambda y,x: (y, x-1)
    }

    new_position = directions[command](y,x)
    y,x = new_position
    if check_inside(matrix, new_position):
        if matrix[y][x] != '-':
            text += matrix[y][x]
        matrix[y][x] = "P"
    else:
        y,x = player_position
        matrix[y][x] = "P"
        text = text[:-1]
    player_position = new_position
    return text,matrix, player_position

for _ in range(commands_count):
    command = input()
    text,matrix, player_position = movement(command,matrix,player_position,text)

print(text)
[print("".join(row)) for row in matrix]
