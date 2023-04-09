import random

from game_algorithms.player import Player
from validator import check_game_board
from decision_tree import DecisionTree, Node, print_tree, print_game_board
from algorithms.minimax import minimax


def start_game():
    game_board = []
    player1 = Player(1)
    player2 = Player(2)

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
    # ------------------------------------------------
    r = random.Random()
    level = 3
    while True:
        if decision_tree.root.isLeaf:
            break

        decision_tree.expand(level)
        min_value = minimax(decision_tree.root, level)

        # player 1
        for child in decision_tree.root.children:
            if child.minimax == min_value:
                decision_tree.root = child

        if decision_tree.root.isLeaf:
            break

        # player 2
        next_move = r.randint(0, len(decision_tree.root.children)-1)
        print_game_board(decision_tree.root.state)
        decision_tree.root = decision_tree.root.children[next_move]

    print_tree(decision_tree.root)
    print(decision_tree.root.calculate_result())


