input_list = reversed(input().split("|"))
result =[]
for el in input_list:
    sublist = el.split()
    result.append(sublist)
flatened = [flat for row in result for flat in row]
print(*flatened, end = " ")
