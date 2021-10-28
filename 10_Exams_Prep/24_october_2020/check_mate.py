import itertools
n = 8
matrix = [[x for x in input().split()] for row in range(n)]

def check_inside(y,x):
    if y in range(0,8) and x in range(0,8):
        return True
    else:
        return False

def check_queen_game(row,col,matrix):
    """"check up"""
    for y in range(row, 0, -1):
        if check_inside(y-1,col) and matrix[y-1][col] == 'Q':
            break
        if check_inside(y-1,col) and matrix[y-1][col] == 'K':
            return True
    """"check down"""
    for y in range(row,8,1):
        if check_inside(y+1,col) and matrix[y+1][col] == 'Q':
            break
        if check_inside(y+1,col) and matrix[y+1][col] == 'K':
            return True
    """"check left"""
    for x in range(col,0,-1):
        if check_inside(row,x-1) and matrix[row][x-1] == 'Q':
            break
        if check_inside(row,x-1) and matrix[row][x-1] == 'K':
            return True
    """"check right"""
    for x in range(col,8,1):
        if check_inside(row,x+1) and matrix[row][x+1] == 'Q':
            break
        if check_inside(row,x+1) and matrix[row][x+1] == 'K':
            return True
    """"check diagonal_down_right"""
    for y,x in zip(range(row,8,1),range(col,8,1)):
        if check_inside(y+1,x+1) and matrix[y+1][x+1] == 'Q':
            break
        if check_inside(y+1,x+1) and matrix[y+1][x+1] == "K":
            return True
            """"check diagonal_up_left"""
    for y, x in zip(range(row,0,-1), range(col,0,-1)):
        if check_inside(y-1,x-1) and matrix[y-1][x-1] == 'Q':
            break
        if check_inside(y-1, x-1) and matrix[y-1][x-1] == "K":
            return True
            """"check diagonal_up_right"""
    for y, x in zip(range(row, 0, -1), range(col, 8, 1)):
        if check_inside(y-1,x+1) and matrix[y-1][x+1] == 'Q':
            break
        if check_inside(y-1, x+1) and matrix[y-1][x+1] == "K":
            return True

    """"check diagonal_down_left"""
    for y, x in zip(range(row,8,1), range(col, 0, -1)):
        if check_inside(y+1,x-1) and matrix[y+1][x-1] == 'Q':
            break
        if check_inside(y+1, x-1) and matrix[y+1][x-1] == "K":
            return True
    return False

result = []
for y in range(8):
    for x in range(8):
       if matrix[y][x] == 'Q':
           if check_queen_game(y,x,matrix):
               result.append((y,x))
if result:
    [print(f"[{el[0]}, {el[1]}]") for el in result]
else:
    print("The king is safe!")
