formula = input()

par_indices =[]
for index,el in enumerate(formula):
    if el == "(":
        par_indices.append(index)

    elif el ==")":
        par_indices.append(index)
        end = par_indices.pop()
        start = par_indices.pop()
        print(formula[start:end+1])



