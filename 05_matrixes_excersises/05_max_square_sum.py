rows,cols = [int(el) for el in input().split(', ')]
matrix =[]

for row in range(rows):
    matrix.append([int(el) for el in input().split(', ')])

max_sum =0
position = None
for row in range(rows-1,0,-1):
    for col in range(cols-1,0,-1):
        sum = matrix[row][col] + matrix[row][col-1] + matrix[row-1][col] + matrix[row-1][col-1]
        if sum >= max_sum:
            max_sum = sum
            position = (row,col)
output_row,output_col = position
print(matrix[output_row-1][output_col-1],matrix[output_row-1][output_col])
print(matrix[output_row][output_col-1],matrix[output_row][output_col])
print(max_sum)

