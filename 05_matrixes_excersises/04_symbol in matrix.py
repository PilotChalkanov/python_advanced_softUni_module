n = int(input())
matrix = []
for rows in range(n):
    matrix.append(list(input()))

symbol = input()
position = None
for rows in range(n):
    for cols in range(n):
        if matrix[rows][cols] == symbol:
            position = (rows,cols)
            break
    if position:
        break

print(position if position else f"{symbol} does not occur in the matrix")


