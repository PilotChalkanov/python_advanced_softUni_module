
set_one = set([int(el) for el in input().split()])
set_two = set([int(el) for el in input().split()])
n = int(input())
for _ in range(n):
    line = input().split()
    command = line[0]
    command_param = line[1]
    if command == 'Add' and command_param == 'First':
        [set_one.add(int(x)) for x in line[2:]]
    elif command == 'Add' and command_param == 'Second':
        [set_two.add(int(x)) for x in line[2:]]
    elif command == 'Remove' and command_param == 'First':
        curr_set = {int(x) for x in line[2:]}
        set_one = set_one.difference(curr_set)
    elif command == 'Remove' and command_param == 'Second':
        curr_set = {int(x) for x in line[2:]}
        set_two = set_two.difference(curr_set)
    else:
        print(set_one.issubset(set_two) or set_two.issubset(set_one))

print(f", ".join([str(x) for x in sorted(set_one)]))
print(f", ".join([str(x) for x in sorted(set_two)]))
