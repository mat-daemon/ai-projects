import copy

from game_algorithms.move_generator import generate_moves, apply_move


# --------------------------------------------------
# Structures
# --------------------------------------------------
class Node:
    """Node represents a particular game state - that is a game board 8x8 with disks and a player who performs next
    move on that game board"""
    def __init__(self, state, player):
        self.player = player
        self.state = state
        self.children = []
        self.isLeaf = False
        self.result = None
        self.minimax = None
        self.expanded = False


    def expand(self, level):
        """Expand the decision tree starting from the current node. After the expansion next levels of nodes
        are created down the tree"""

        if level > 0:

            # Expand node for the first time
            if not self.expanded:
                moves = generate_moves(self.state, self.player.nr)
                self.expanded = True

                # if player can do a next move
                if len(moves) > 0:
                    for move in moves:
                        next_game_state = copy.deepcopy(self.state)
                        apply_move(next_game_state, move, self.player.nr)
                        node = Node(next_game_state, self.player.opponent)
                        self.children.append(node)
                        node.expand(level-1)

                # if player cannot do a next move
                else:
                    other_player_moves = generate_moves(self.state, self.player.opponent.nr)

                    # Neither player can do a move
                    # Game is over
                    if len(other_player_moves) == 0:
                        self.isLeaf = True
                    # Player does not perform a move and skip the round
                    else:
                        node = Node(self.state, self.player.opponent)
                        self.children.append(node)


            # Expand the tree further
            else:
                for child in self.children:
                    child.expand(level-1)


    def calculate_result(self):
        if self.result is None:
            if self.isLeaf:
                self.result = 0
                for row in self.state:
                    self.result += row.count(self.player.nr)
            else:
                # TODO use heuristic instead
                self.result = 0
                for row in self.state:
                    self.result += row.count(self.player.nr)
                # ---------------------------------------------
        return self.result


class DecisionTree:
    """Structure representing the pointer on current decision tree root node"""
    def __init__(self, initial_state, player):
        self.root = Node(initial_state, player)

    def expand(self, level):
        self.root.expand(level)

# --------------------------------------------------



# --------------------------------------------------
# Printers
# --------------------------------------------------
def print_tree(node):
    print_game_board(node.state)
    for child in node.children:
        print_tree(child)


def print_game_board(game_board):
    for row in game_board:
        print(row)
    print()