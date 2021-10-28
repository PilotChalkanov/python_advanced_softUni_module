from collections import deque


def list_manipulator(num_list: deque, command: str, place: str, *args):
    num_list = num_list
    elements = list(args)

    if command == "add":
        if place == 'beginning':
            num_list = elements + num_list
        else:
            num_list.extend(elements)
            num_list = list(num_list)

    else:
        num_list = list(num_list)
        if args:
            indexes = int(*args)
            if place == 'beginning':
                num_list=num_list[indexes:len(num_list)]
            else:
                num_list=num_list[0:len(num_list)-indexes]
        else:
            if place == 'beginning':
                num_list = num_list[1:]
            else:
                num_list= num_list[:len(num_list)-1]
    return num_list



print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
