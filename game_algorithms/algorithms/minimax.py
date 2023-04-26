import math


def minimax(node, level):
    """Minimax algorithm implementation"""

    if node.isLeaf or level == 0:
        return node.calculate_rate()

    if node.player.nr == 1:
        comp_function = lambda a, b: a < b
    else:
        comp_function = lambda a, b: a > b
    min_max_value = math.inf
    for child in node.children:
        minimax_result = minimax(child, level-1)
        if comp_function(minimax_result, min_max_value):
            min_max_value = minimax_result
    node.minimax = min_max_value
    return min_max_value


