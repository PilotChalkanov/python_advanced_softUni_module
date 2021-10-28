n =  int(input())
matrix =[]
result_primary = 0
result_secondary = 0
primary_print = ''
secondary_print = ''
for row in range(n):
    matrix.append([int(el) for el in input().split(', ')])
    primary_print += f"{matrix[row][row]}, "
    secondary_print += f"{matrix[row][-row-1]}, "
    result_primary += matrix[row][row]
    result_secondary += matrix[row][-row-1]
# for row in range(n):
#     for col in range(n):
#         if row == col:
#             result += matrix[row][col]
print(f"Primary diagonal: {primary_print}. Sum: {result_primary}")
print(f"Secondary diagonal: {secondary_print}. Sum: {result_secondary}")


