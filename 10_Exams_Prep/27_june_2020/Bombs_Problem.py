
# 5, 25, 25, 115
# 5, 15, 25, 35

from collections import deque
bomb_effects = deque([int(x) for x in input().split(', ')])
bomb_casing = list([int(x) for x in input().split(', ')])
bombs={
    40: 'Datura Bombs' ,
    60: 'Cherry Bombs' ,
    120: 'Smoke Decoy Bombs' ,
}
bomb_pouch = {'Datura Bombs':0,
              'Cherry Bombs':0,
               'Smoke Decoy Bombs':0
              }


while bomb_casing or bomb_effects:
    current_el_bomb_effect = bomb_effects[0]
    if bomb_casing:
        current_el_bomb_casing = bomb_casing[-1]
    current_points = current_el_bomb_effect + current_el_bomb_casing
    if current_points in bombs.keys():
        bomb_effects.popleft()
        bomb_casing.pop()
        bomb_pouch[bombs[current_points]] += 1
    else:
        if bomb_casing:
            bomb_casing[-1] -= 5
        else:
            break
    if bomb_pouch['Datura Bombs'] >= 3 and bomb_pouch['Cherry Bombs'] >= 3 and bomb_pouch['Smoke Decoy Bombs'] >= 3:
        break

if bomb_pouch['Datura Bombs'] >= 3 and bomb_pouch['Cherry Bombs'] >= 3 and bomb_pouch['Smoke Decoy Bombs'] >= 3:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")
if bomb_effects:
    print(f"Bomb Effects: {', '.join([str(x) for x in bomb_effects])}")
else:
    print("Bomb Effects: empty")
if bomb_casing:
    print(f"Bomb Casings: {', '.join([str(x) for x in bomb_casing])}")
else:
    print("Bomb Casings: empty")
for k,v in sorted(bomb_pouch.items()):
    print(f"{k}: {v}")