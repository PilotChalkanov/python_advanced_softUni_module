def permutation(line, current_index = 0):

    if current_index == len(line):
        print("".join(line))
        return

    for index in range(current_index, len(line)):
        line[index],line[current_index] = line[current_index], line[index]

        permutation(line, current_index+1)
        line[index], line[current_index] = line[current_index], line[index]

line = list(input())
permutation(line)