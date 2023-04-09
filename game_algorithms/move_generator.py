class Move:
    """Move represents a player move, that is x and y coordinates of the placed disk on the game board
    and all opponent disks coordinates that are reversed"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.reversed_disks = set()

    def add_reversed_disks(self, disks):
        for disk in disks:
            self.reversed_disks.add(disk)

    def is_valid(self):
        return len(self.reversed_disks) > 0


def generate_moves(game_state, player):
    """Generate all possible moves for the player.
    player - indicated by 1 or 2
    game_state - current game board 8x8"""

    moves = []
    for row_nr, row in enumerate(game_state):
        for col_nr, state in enumerate(row):
            if state == 0:
                possible_move = Move(row_nr, col_nr)
                possible_move.add_reversed_disks(check_move(game_state, player, row_nr, col_nr, 1, 0))   # right
                possible_move.add_reversed_disks(check_move(game_state, player, row_nr, col_nr, 1, 1))   # right down
                possible_move.add_reversed_disks(check_move(game_state, player, row_nr, col_nr, 0, 1))  # down
                possible_move.add_reversed_disks(check_move(game_state, player, row_nr, col_nr, -1, 1))  # left down
                possible_move.add_reversed_disks(check_move(game_state, player, row_nr, col_nr, -1, 0))  # left
                possible_move.add_reversed_disks(check_move(game_state, player, row_nr, col_nr, -1, -1)) # left up
                possible_move.add_reversed_disks(check_move(game_state, player, row_nr, col_nr, 0, -1))  # up
                possible_move.add_reversed_disks(check_move(game_state, player, row_nr, col_nr, 1, -1))  # right up

                if possible_move.is_valid():
                    moves.append(possible_move)

    return moves


def check_move(game_state, player, row_nr, col_nr, direction_x, direction_y):
    """Check whether empty field game_state[row_nr][col_nr] could be the player's next possible move.
    Move is possible when there is a straight line with player's disk on the beginning of the line
    and player's opponent disks on the rest of the line"""

    reversed_disks = []
    initial_row = row_nr
    initial_col = col_nr

    row_nr += direction_x
    col_nr += direction_y

    opponent = 3-player # For one give two and vice versa

    opponents_on_path = []
    player_on_end = False

    while row_nr >= 0 and row_nr < len(game_state) and col_nr >= 0 and col_nr < len(game_state):
        if game_state[row_nr][col_nr] == opponent:
            opponents_on_path.append((row_nr, col_nr))
            row_nr += direction_x
            col_nr += direction_y

        elif game_state[row_nr][col_nr] == player:
            player_on_end = True
            break

        else:
            break


    if opponents_on_path and player_on_end:
        return opponents_on_path

    else:
        return []



def apply_move(game_board, move, player):
    game_board[move.x][move.y] = player

    for (x,y) in move.reversed_disks:
        game_board[x][y] = player

