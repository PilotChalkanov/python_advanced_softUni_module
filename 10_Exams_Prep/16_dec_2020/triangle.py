def get_magic_triangle(n):

    triangle = [[1], [1, 1]]
    #2 how to know what number to append - for first position take previous row adjacent position values and store it

      # continue doing it until triangle.len == n
    row = 1
    while row < n-1:
        # take the last row and append 2 from position 1 until position current n-1 or len na current row
        last_row = triangle[-1]
        sreda = []
        for i in range(row):
            sreda.append(last_row[i]+last_row[i+1])
        next_row = last_row[0:1] + sreda + last_row[0:1]
        triangle.append(next_row)
        row +=1
    return triangle

get_magic_triangle(5)