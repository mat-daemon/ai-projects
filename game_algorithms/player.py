from move_generator import generate_moves


class Player:
    def __init__(self, nr, strategy):
        self.nr = nr
        self.strategy = strategy
        self.opponent: Player = None


# STRATEGIES

# The most natural strategy that many primitive
# computer Othello players employed was to base
# their move on a greedy strategy that tried to
# maximize the number of coins of a player at any
# point. Such strategies failed miserably, and
# obviously so.
# An Analysis of Heuristics in Othello
# Vaishnavi Sannidhanam and Muthukaruppan Annamalai
# https://courses.cs.washington.edu/courses/cse573/04au/Project/mini1/RUSSIA/Final_Paper.pdf
def maximum_disks_strategy(game_board, player_nr):
    result_player = 0
    result_opponent = 0
    opponent = 3-player_nr

    for row in game_board:
        result_player += row.count(player_nr)
        result_opponent += row.count(opponent)

    return 0 if result_player + result_opponent == 0 else 100*(result_player - result_opponent)/(result_player + result_opponent)


# Mobility comes in two flavors [1], (i) actual
# mobility and (ii) potential mobility. Actual
# mobility is the number of next moves a player
# has, given the current state of the game.
# Potential mobility is the number of possible
# moves the player might have over the next few
# moves.
def mobility_strategy(game_board, player_nr):
    result_player = 0
    result_opponent = 0
    opponent = 3 - player_nr

    for row_nr, row in enumerate(game_board):
        for state_nr, state in enumerate(row):
            if state == 0:
                opponent_disk_neighbor = False
                player_disk_neighbor = False

                for direction_x, direction_y in [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]:
                    if (0 <= row_nr + direction_y < 8 and 0 <= state_nr + direction_x < 8):
                            if game_board[row_nr + direction_y][state_nr + direction_x] == opponent:
                                opponent_disk_neighbor = True
                            if game_board[row_nr + direction_y][state_nr + direction_x] == player_nr:
                                player_disk_neighbor = True

                if opponent_disk_neighbor:
                    result_player += 1
                if player_disk_neighbor:
                    result_opponent += 1

    return 0 if result_player + result_opponent == 0 else 100*(result_player - result_opponent)/(result_player + result_opponent)


# The static board implicitly captures the
# importance of each square on the board, and
# encourages the game play to tend towards
# capturing corners
def stability_weights_strategy(game_board, player_nr):
    static_weights = [[ 4, -3,  2,  2,  2,  2, -3,  4],
                      [-3, -4, -1, -1, -1, -1, -4, -3],
                      [ 2, -1,  1,  0,  0,  1, -1,  2],
                      [ 2, -1,  0,  1,  1,  0, -1 , 2],
                      [ 2, -1,  0,  1,  1,  0, -1 , 2],
                      [ 2, -1,  1,  0,  0,  1, -1,  2],
                      [-3, -4, -1, -1, -1, -1, -4, -3],
                      [ 4, -3,  2,  2,  2,  2, -3,  4]]

    result_player = 0
    result_opponent = 0
    opponent = 3 - player_nr

    for row_nr, row in enumerate(game_board):
        for state_nr, state in enumerate(row):
            if state == player_nr:
                result_player += static_weights[row_nr][state_nr]
            if state == opponent:
                result_opponent += static_weights[row_nr][state_nr]

    return result_player-result_opponent


