from collections import deque

chocolate = [int(x) for x in input().split(', ')]
milk = deque([int(x) for x in input().split(', ')])
counter = 0
while counter < 5 and milk and chocolate:

    current_choc = chocolate[-1]
    current_milk = milk[0]
    if current_choc <= 0:
        chocolate.pop()

    elif current_milk <=0:
        milk.popleft()
    if not chocolate or not milk:
        break

    current_choc = chocolate[-1]
    current_milk = milk[0]
    if current_milk == current_choc:
        counter+=1
        chocolate.pop()
        milk.popleft()
    else:
        current_milk = milk.popleft()
        milk.append(current_milk)
        chocolate[-1] -= 5
if counter >= 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolate:
    print(f"Chocolate: {', '.join([str(x)for x in chocolate])}")
else:
    print("Chocolate: empty")
if milk:
    print(f"Milk: {', '.join([str(x)for x in milk])}")
else:
    print("Milk: empty")