nums = tuple([float(el) for el in input().split()])
result ={}
for el in nums:
    if el not in result:
        result[el] = 1
    else:
        result[el] +=1
for k,v in result.items():
    print(f'{k} - {v} times')
