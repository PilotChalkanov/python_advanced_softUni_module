n = int(input())
max_intersection = set()
for _ in range(n):
    first, second = input().split('-')
    first_start, first_end = [int(el) for el in first.split(',')]
    second_start, second_end = [int(el) for el in second.split(',')]
    first_set = {num for num in range(first_start,first_end+1)}
    second_set = {num for num in range(second_start,second_end+1)}
    temp_intersection = first_set.intersection(second_set)
    if len(temp_intersection) > len(max_intersection):
        max_intersection = temp_intersection
print(f"Longest intersection is {list(max_intersection)} with length {len(max_intersection)}")