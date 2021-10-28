global n
n = int(input)
def check_inside(y, x):
    if  0 <= x < n and 0 <= y < n:
        return True
    return False
def coal_collect(coal_position: list, player_position:tuple):
    if player_position in coal_position:
        return True
    return False
actions ={
    'up': lambda y,x: (y-1,x),
    'down': lambda y,x: (y+1,x),
    'left': lambda y,x: (y,x-1),
    'right': lambda y,x: (y,x+1),

}