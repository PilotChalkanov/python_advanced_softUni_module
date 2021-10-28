# 50
# 2
# 11 10 5 11 10 20
# 15 13 16
# 1500
# #
from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = [int(x) for x in input().split(' ')]
locks = deque([int(x) for x in input().split(' ')])
money = int(input())

reloaded = gun_barrel_size
while bullets and locks:

    current_bullet = bullets.pop()
    current_lock = locks[0]

    if current_lock >= current_bullet:

        print('Bang!')
        locks.popleft()
        reloaded -= 1
        money -= bullet_price
        if reloaded == 0:
            print('Reloading!')
            reloaded = gun_barrel_size


    else:

        print('Ping!')
        money -= bullet_price
        reloaded -= 1
        if reloaded == 0:
            print('Reloading!')
            reloaded = gun_barrel_size





if locks:
   print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    print(f"{len(bullets)} bullets left. Earned ${money}")
