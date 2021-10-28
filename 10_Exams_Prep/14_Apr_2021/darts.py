from collections import deque
player1,player2 = input().split(', ')
matrix = [[x for x in input().split()] for y in range(7)]

def check_inside(matrix,throw):
    y,x = throw
    if y in range(0,len(matrix)) and x in range(0,len(matrix[0])):
        return True
    else:
        return False
def results(matrix,throw):
    y,x = throw

    if matrix[y][x] == "T":
        result = (int(matrix[0][x]) + int(matrix[-1][x]) + int(matrix[y][0]) + int(matrix[y][-1])) * 3
    elif matrix[y][x] == "D":
        result = (int(matrix[0][x]) + int(matrix[-1][x]) + int(matrix[y][0]) + int(matrix[y][-1])) * 2
    elif matrix[y][x] == "B":
        result = "won"
    else:
        result = int(matrix[y][x])
    return result
players_score = {
    player1 : 501,
    player2 : 501

}
player_trows = {
    player1: 0,
    player2:0,
}
current_player_turn = deque()
current_player_turn.append(player1)
current_player_turn.append(player2)

line = input()

while True:
    throw = [int(x) for x in line[1:-1].split(', ')]
    current_player = current_player_turn.popleft()
    current_player_turn.append(current_player)
    if check_inside(matrix,throw):
        current_result = results(matrix,throw)
        player_trows[current_player] +=1
        if current_result == "won":
            print(f"{current_player} won the game with {player_trows[current_player]} throws!")
            break

        else:
            players_score[current_player]-=current_result

        if players_score[current_player] <= 0:
            print(f"{current_player} won the game with {player_trows[current_player]} throws!")
            break
    else:
        player_trows[current_player] += 1
        line = input()
        continue

    line = input()


