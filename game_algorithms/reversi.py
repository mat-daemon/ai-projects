import math
import random

from game_algorithms.player import Player, maximum_disks_strategy, mobility_strategy, stability_weights_strategy
from validator import check_game_board
from decision_tree import DecisionTree, Node, print_tree, print_game_board
from algorithms.minimax import minimax
from algorithms.minimax_alfa_beta_prune import minimax_with_alfa_beta_prune


def start_game(verbose = True, alfa_beta_prune = True):
    game_board = []


    player1 = Player(1, stability_weights_strategy)
    player2 = Player(2, stability_weights_strategy)

    player2.game_strategy = maximum_disks_strategy

    player1.opponent = player2
    player2.opponent = player1

    print("Enter initial game state:")


    # ------------------------------------------------
    # Get input from user and create Game Board
    # ------------------------------------------------
    line = input()
    while line != "END":
        game_board.append([int(state) for state in line.split(" ")])
        line = input()


    # ------------------------------------------------
    # Validate game board
    # ------------------------------------------------
    (game_board_valid, message) = check_game_board(game_board)

    if not game_board_valid:
        print(message)
        return


    # ------------------------------------------------
    # Create decision tree
    # ------------------------------------------------
    decision_tree = DecisionTree(game_board, player1)
    decision_tree.root.state = game_board


    # ------------------------------------------------
    # Game simulation
    # From the player 1 perspective
    # ------------------------------------------------
    # level 4 approx 2 seconds first run, then ap. 1 sec
    # level 5 approx 25 seconds first run, then ap. 15 sec
    level = 4
    while True:
        if decision_tree.root.isLeaf:
            break

        decision_tree.expand(level)

        # with alfa-beta prune
        if alfa_beta_prune:
            max_value = minimax_with_alfa_beta_prune(-math.inf, math.inf, decision_tree.root, level)

        # without alfa-beta prune
        else:
            max_value = minimax(decision_tree.root, level)

        # player 1
        for child in decision_tree.root.children:
            if child.minimax == max_value:
                decision_tree.root = child

        if verbose:
            print("Player 1 move")
            print_game_board(decision_tree.root.state)

        if decision_tree.root.isLeaf:
            break

        # player 2
        best_move_rate = -math.inf
        next_move = 0
        for child_nr, child in enumerate(decision_tree.root.children):
            # move_rate = child.calculate_rate()
            move_rate = player2.game_strategy(child.state, player2.nr)

            if move_rate > best_move_rate:
                best_move_rate = move_rate
                next_move = child_nr

        decision_tree.root = decision_tree.root.children[next_move]

        if verbose:
            print("Player 2 move")
            print_game_board(decision_tree.root.state)

    game_result = calculate_result(decision_tree.root.state)
    print(f"Player 1 result is: {game_result[0]}. Player 2 result is: {game_result[1]}")


def calculate_result(game_board):
    player_1_result = 0
    player_2_result = 0

    for row in game_board:
        player_1_result += row.count(1)
        player_2_result += row.count(2)

    return (player_1_result, player_2_result)


