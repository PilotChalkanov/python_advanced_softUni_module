n = int(input())

spiral = [[j for j in range(n)] for i in range(n)]
matrix_end = n**2
def filling(n, first_el):
    current_position = (0,0)
    current_row_index, current_col_index = current_position
    current_row_beginning, current_col_beginning = (0,0)
    while first_el != matrix_end +1:
        for col in range(current_col_beginning,n,1):
            spiral[current_row_beginning][col] = first_el
            first_el += 1
            current_position = (current_row_beginning, col)

        current_row_index,current_col_index = current_position
        current_row_index+=1

        for row in range(current_row_index, n, 1):
            spiral[row][current_col_index] = first_el
            first_el += 1
            current_position = (row,current_col_index)
        current_row_index, current_col_index = current_position
        current_col_index -= 1
        for col in range(current_col_index,current_col_beginning-1,-1):

            spiral[current_row_index][col] = first_el
            first_el+=1
            current_position = (current_row_index,col)
        current_row_index,current_col_index = current_position
        current_row_index -=1
        for row in range(current_row_index,current_row_beginning,-1):
            spiral[row][current_col_index] = first_el
            first_el+=1
        current_position = (row,current_col_index)
        current_col_index -=1
        current_col_beginning +=1
        current_row_beginning +=1
        n-=1
filling(n, 1)
print([[str(el) for el in spiral[j]] for j in range(n)])

