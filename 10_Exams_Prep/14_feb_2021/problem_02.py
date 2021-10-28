import math

n = int(input())
matrix = [input().split() for y in range(n)]

player_position = [(y,x) for y in range(n) for x in range(n) if matrix[y][x]=='P'].pop()

def check_inside(player_position,matrix):
    y,x = player_position
    if y in range(0,len(matrix)) and x in range(0,len(matrix)) and matrix[y][x] != 'X':
        return True
    else:
        return False
def movement(matrix,player,command):
    pass


move = {
    "up" : lambda y,x : (y-1,x),
    "down": lambda y,x : (y+1,x),
    "right": lambda y,x : (y,x+1),
    "left" : lambda y,x : (y,x-1)

}
path = []
coins = 0
y,x = player_position

while coins < 100:
    command = input()
    player_position = move[command](y,x)

    if check_inside(player_position,matrix):
        y,x = player_position
        coins += int(matrix[y][x])
        path.append(player_position)
    else:
        coins = math.floor(coins/2)
        print(f"Game over! You've collected {coins} coins.")
        break


if coins >=100:
    print(f"You won! You've collected {coins} coins.")
print("Your path:")
for el in path:
    print(f"[{el[0]}, {el[1]}]")