def numbers_searching(*args):
    min_num = min(*args)
    max_num = max(*args)
    result = []
    seq_example = {x for x in range(min_num,max_num+1)}
    seq_actual = list(args)
    seq_actual_Set = set(seq_actual)

    missing_number = seq_example - seq_actual_Set
    result.append(missing_number.pop())

    list_result = sorted([item for item in seq_example if seq_actual.count(item)>1])
    result.append(list_result)
    return(result)



print(numbers_searching(1, 2, 4, 2, 5, 4))