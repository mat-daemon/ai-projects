from validator import check_game_board
from decision_tree import DecisionTree, Node, print_tree


def start_game():
    game_board = []
    player = 1

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
    decision_tree = DecisionTree(game_board, player)
    decision_tree.root.state = game_board

    decision_tree.root.expand(4)

    print_tree(decision_tree.root)



