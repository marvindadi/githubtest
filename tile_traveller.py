# Global variables
BORDERS =  {(0, 0): [(0, 1)], (0, 1): [(0, 0), (0, 2)], (0, 2): [(0, 1)],
            (1, 0): [], (1, 1): [(1, 2), (2, 1)], (1, 2): [(1,1)], 
            (2, 0): [], (2, 1): [(1, 1)], (2, 2): []}

DIRECTIONS = {"N": "(N)orth", "E": "(E)ast", "S":"(S)outh", "W":"(W)est"}

def intitialize_board():
    board = []
    for i in range(3):
        sublist = []
        for j in range(3):
             sublist.append('o')
        board.append(sublist)
    board[0][0] = 'x'
    current_pos = (0, 0)
    return board, current_pos


def get_valid_moves(current_pos):
    pos_line = current_pos[0]
    pos_col = current_pos[1]

    valid_move_list = []

    if pos_line > 0:
        move = (pos_line - 1, pos_col)
        if move not in BORDERS[current_pos]:
            valid_move_list.append("N")
    if pos_line < 2:
        move = (pos_line + 1, pos_col)
        if move not in BORDERS[current_pos]:
            valid_move_list.append("S")
    if pos_col > 0:
        move = (pos_line, pos_col - 1)
        if move not in BORDERS[current_pos]:
            valid_move_list.append("W")
    if pos_col < 2:
        move = (pos_line, pos_col + 1)
        if move not in BORDERS[current_pos]:
            valid_move_list.append("E")

    return valid_move_list

def get_direction(current_pos, valid_moves):
    print("You can travel: ", end='')
    counter = 0
    for direction in valid_moves:
        print(DIRECTIONS[direction], end='')
        counter += 1
        if counter < len(valid_moves):
            print(end=' or ')
    print(".")

    valid = False
    while valid == False:
        choice = input("Direction: ").upper()
        if choice in valid_moves:
            return choice
        else:
            print("Not a valid direction!")

def make_move(board, move, current_pos):
    pos_line = current_pos[0]
    pos_col = current_pos[1]
    board[current_pos[0]][current_pos[1]] == 'o'

    if move == 'N':
        new_pos = (pos_line - 1, pos_col)
        board[pos_line - 1][pos_col] = 'x'
    elif move == 'E':
        new_pos = (pos_line, pos_col + 1)
        board[pos_line][pos_col + 1] = 'x'
    elif move == 'S':
        new_pos = (pos_line + 1, pos_col)
        board[pos_line + 1][pos_col] = 'x'
    elif move == 'W':
        new_pos = (pos_line, pos_col - 1)
        board[pos_line][pos_col - 1] = 'x'

    return board, new_pos

# Main
def main():
    board, current_pos = intitialize_board()
    while current_pos != (0, 2):
        valid_moves = get_valid_moves(current_pos)
        move = get_direction(current_pos, valid_moves)
        board, current_pos = make_move(board, move, current_pos)
        if current_pos == (0, 2):
            print("Victory!")


main()