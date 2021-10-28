from collections import deque
males = [int(x) for x in input().split()]
females = deque([int(x) for x in input().split()])
matches = 0

while males and females:
    current_male = males[-1]
    current_female = females[0]

    if current_female <= 0:
        females.popleft()

    elif current_male <= 0:
        males.pop()

    elif current_female == current_male:
        females.popleft()
        males.pop()
        matches +=1
    elif current_male % 25 == 0:
        males.pop()
        if males:
            males.pop()
        else:
            break
    elif current_female % 25 == 0:
        females.popleft()
        if females:
            females.popleft()
        else:
            break
    else:
        if females:
            females.popleft()
        if males:
            males[-1]-=2
print(f"Matches: {matches}")
if males:
    print(f"Males left: {', '.join([str(males[x]) for x in range(len(males)-1,-1,-1)])}")
else:
    print("Males left: none")
if females:
    print(f"Females left: {', '.join([str(x) for x in females])}")
else:
    print("Females left: none")


