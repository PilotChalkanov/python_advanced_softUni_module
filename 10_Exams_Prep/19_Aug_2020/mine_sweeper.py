
n = int(input())
mines_count = int(input())
mines = []
for _ in range(mines_count):
        mines.append(input())
matrix = [[0 for col in range(n)] for row in range(n)]
for y in range(n):
    for x in range(n):
        if f"({y}, {x})" in mines:
            matrix[y][x] = '*'
            mines.remove(f"({y}, {x})")

def check_inside(y,x):
    if x in range(0, len(matrix)) and y in range(0, len(matrix)):
        return True
    else:
        return False

# [print(row) for row in matrix]

for y in range(n):

    for x in range(n):
        count = 0
        if matrix[y][x] != '*':
            if check_inside(y-1, x-1) and matrix[y-1][x-1] == '*':
                count+=1
            if check_inside(y-1,x) and matrix[y-1][x] == '*':
                count += 1
            if check_inside(y-1,x+1) and matrix[y-1][x+1] == '*':
                count +=1
            if check_inside(y,x+1) and matrix[y][x+1] == '*':
                count += 1
            if check_inside(y,x-1) and matrix[y][x-1] == '*':
                count += 1
            if check_inside(y+1,x+1) and matrix[y+1][x+1] == '*':
                count += 1
            if check_inside(y+1,x)and matrix[y+1][x] == '*':
                count += 1
            if check_inside(y+1,x-1) and matrix[y+1][x-1] == '*':
                count += 1
            matrix[y][x] = count

[print(*row) for row in matrix]
