def combinations(names,n,comb=[]):
    if len(comb) == n:
        print(", ".join(comb))
        return

    for i in range(len(names)):
        name = names[i]
        comb.append(name)
        combinations(names[i+1:],n,comb)
        comb.pop()


names = input().split(', ')
n = int(input())
combinations(names,n)