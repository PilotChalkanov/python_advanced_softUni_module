nums_dict = {}

line = input()

while line != 'Search':
    num_as_str = line
    try:
        num = int(input())
        nums_dict[num_as_str] = num
    except ValueError:
        print("The variable number must be an integer")
    line = input()

line = input()
while line != 'Remove':
    searched_key = line
    try:
        print(nums_dict[searched_key])
    except KeyError:
        print("Number does not exist in dictionary")
    line= input()

line = input()
while line != "End":
    searched_key = line
    try:
        del nums_dict[searched_key]
    except KeyError:
        print("Number does not exist in dictionary")
    line = input()
print(nums_dict)
