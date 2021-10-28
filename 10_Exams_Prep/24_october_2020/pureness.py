from collections import deque
def best_list_pureness(*test):
    queue = deque(test[0])
    k = int(test[1])
    pureness_list = []
    for _ in range(k+1):
        pure = [int(queue[i])*i for i in range(len(queue))]
        pureness = sum(pure)
        pureness_list.append(pureness)
        el = queue.pop()
        queue.appendleft(el)
    result = max(pureness_list)
    if result:
        return f"Best pureness {result} after {pureness_list.index(result)} rotations"
    else:
        return None
test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)