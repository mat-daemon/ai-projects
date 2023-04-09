import copy

from game_algorithms.move_generator import generate_moves, apply_move


class Node:
    def __init__(self, state, player):
        self.player = player
        self.state = state
        self.children = []

    def add_child(self, child):
        if child not in self.children:
            self.children.append(child)

    def expand(self, level):
        if level > 0:
            moves = generate_moves(self.state, self.player)
            for move in moves:
                next_game_state = copy.deepcopy(self.state)
                apply_move(next_game_state, move, self.player)
                node = Node(next_game_state, self.player)
                self.children.append(node)
                node.expand(level-1)


class DecisionTree:
    def __init__(self, initial_state, player):
        self.root = Node(initial_state, player)

    def expand(self, level):
        self.root.expand(level)




def print_tree(node):
    print_game_board(node.state)
    for child in node.children:
        print_tree(child)


def print_game_board(game_board):
    for row in game_board:
        print(row)
    print()