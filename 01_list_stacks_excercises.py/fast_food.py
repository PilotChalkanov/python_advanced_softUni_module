from collections import deque

total_food = int(input())
order_queue =  deque(input().split())

order_queue_map = map(int,order_queue)
print(max(order_queue_map))
while order_queue:
    if total_food < int(order_queue[0]):
        break
    else:
        total_food -= int(order_queue.popleft())

if not order_queue:
    print("Orders complete")
else:    
    print(f'Orders left: {" ".join(order_queue)}')
