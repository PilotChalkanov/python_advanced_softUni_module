from collections import deque
kids = deque(input().split())
n= int(input())

red = []
while kids:

    for _ in range(n-1):
        current_kid = kids.popleft()
        kids.append(current_kid)
    red.append(kids.popleft())


for i in range(len(red)-1):
    print(f"Removed {red[i]}");
print(f"Last is {red.pop()}")