n = int(input())

matrix = [[int(el) for el in input().split(', ')] for _ in range(n)]
flattened_matrix = [num for sublist in matrix for num in sublist]
print(flattened_matrix)