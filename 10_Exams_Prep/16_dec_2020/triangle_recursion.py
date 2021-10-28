def get_magic_triangle(n,triangle = [[1], [1, 1]], lenlen = 0):
    if n == lenlen:
        return triangle
    else:
        if lenlen == n-2:
            return 1
        last_row = triangle[-1]
        sreda = []
        for i in range(lenlen+1):
            sreda.append(last_row[i]+last_row[i+1])
        next_row = last_row[0:1] + sreda + last_row[0:1]
        triangle.append(next_row)
        get_magic_triangle(n, triangle, lenlen+1)
        return triangle

print(get_magic_triangle(0))