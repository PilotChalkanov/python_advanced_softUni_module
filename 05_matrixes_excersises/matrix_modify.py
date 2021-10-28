n = int(input())
matrix =[]
for i in range(n):
    matrix.append([int(x) for x in input().split()])
command = input()

def coord_valid(row,col):
    if row in range(0,len(matrix)) and col in range(0,len(matrix[0])):
        return True
    return False
while command != 'END':
    action,row,col,value = command.split()
    row = int(row)
    col = int(col)
    value = int(value)

    if action == "Add":
        if coord_valid(row, col):
            matrix[row][col] += value
        else:
            print("Invalid coordinates")
    else:
        if coord_valid(row, col):
            matrix[row][col] -= value
        else:
            print("Invalid coordinates")

    command = input()

for row in matrix:
    print(" ".join([str(x) for x in row]))