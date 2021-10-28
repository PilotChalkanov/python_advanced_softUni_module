rows,cols = [int(el) for el in input().split()]
def init_matrix():
    matrix = []

    for _ in range(rows):
        matrix.append([el for el in input().split()])
    return matrix

matrix = init_matrix()
def check_index_valid(index_row, index_col,row,col):
    if 0 <= index_row < row and 0 <= index_col < col:
        return True
    return False

def valid_command(command,coords,rows,cols):
    if len(coords) == 4 and command == 'swap':
        for index in range(0,len(coords),2):
            if not check_index_valid(coords[index],coords[index+1],rows,cols ):
                print("Invalid input!")
                return False
        return True
    else:
        print("Invalid input!")
def print_matrix(matrix,rows,cols):
    for row in range(rows):
        matrix_row = [str(el) for el in matrix[row]]
        print(' '.join(matrix_row))


line = input()
while not line == "END":
    line_splitted = line.split()
    command = line_splitted[0]
    coordinates = [int(el) for el in line_splitted[1:]]
    if valid_command(command, coordinates, rows,cols):
        matrix[coordinates[0]][coordinates[1]],matrix[coordinates[2]][coordinates[3]] = \
            matrix[coordinates[2]][coordinates[3]],matrix[coordinates[0]][coordinates[1]]
        print_matrix(matrix,rows,cols)
    line = input()