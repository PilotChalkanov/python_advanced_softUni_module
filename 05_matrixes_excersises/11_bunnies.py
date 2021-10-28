from collections import deque
global n
global m
n,m = [int(x) for x in input().split()]

def check_inside(y, x):
    if  0 <= x < m and 0 <= y < n:
        return True
    return False
def bunny_collision(bunny_array: list, player_position:tuple):
    if player_position in bunny_array:
        return True
    return False
def new_bunnies(matrix):
    for x in range(n):
        for y in range(m):
            if matrix[x][y] == 'NB':
                matrix[x][y] = 'B'

def bunny_mutate(matrix,bunny_array):
    for i in range(n):
        for j in range(m):

            if matrix[i][j] == 'B':
                #bunny down check vald
                if check_inside(i+1,j) and matrix[i+1][j] != "B":
                    bunny_array.append((i+1,j))
                    matrix[i + 1][j] = 'NB'
                if check_inside(i -1, j) and matrix[i-1][j]!= "B":
                    bunny_array.append((i-1,j))
                    matrix[i - 1][j] = 'NB'
                if check_inside(i , j+1) and matrix[i][j+1]!= "B":
                    bunny_array.append((i,j+1))
                    matrix[i][j + 1] = 'NB'
                if check_inside(i, j - 1) and matrix[i][j-1]!= "B":
                    bunny_array.append((i,j-1))
                    matrix[i][j - 1] = 'NB'
    new_bunnies(matrix)
    return matrix


actions ={
    'U': lambda y,x: (y-1,x),
    'D': lambda y,x: (y+1,x),
    'L': lambda y,x: (y,x-1),
    'R': lambda y,x: (y,x+1),

}
matrix=[]
bunny_array = []
for r in range(n):
    matrix.append(list(input()))
commands = list(input())

current_position_player =(0,0)
for y in range(n):
    for x in range(m):
        if matrix[y][x] == "P":
            current_postion_player = (y,x)
        if matrix[y][x] == "B":
            bunny_array.append((y,x))
curr_y, curr_x = current_postion_player
for command in commands:

    changed_position_player = actions[command](curr_y,curr_x)
    new_y,new_x = changed_position_player
    if check_inside(new_y,new_x) and matrix[new_y][new_x] != 'B':
        matrix[new_y][new_x] = 'P'
        matrix[curr_y][curr_x] = '.'
        curr_y,curr_x = new_y,new_x
        bunny_mutate(matrix, bunny_array)
    elif not check_inside(new_y,new_x):
        matrix[curr_y][curr_x] = '.'
        bunny_mutate(matrix, bunny_array)
        for row in matrix:
            print("".join([el for el in row]))
        print(f"won: {curr_y} {curr_x}")
        break

    elif matrix[new_y][new_x] == 'B':
        matrix[curr_y][curr_x] = '.'
        bunny_mutate(matrix, bunny_array)
        for row in matrix:
            print("".join([el for el in row]))
        print(f"dead: {new_y} {new_x}")
        break

