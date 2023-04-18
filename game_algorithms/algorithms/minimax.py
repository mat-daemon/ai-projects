import math


def minimax(alfa, beta, node, level):
    """Minimax algorithm implementation"""
    # With alfa - beta prune

    if node.isLeaf or level == 0:
        node.minimax = node.calculate_rate()
        return node.calculate_rate()

    if node.player.nr == 1:
        for child in node.children:
            alfa = max(alfa, minimax(alfa, beta, child, level - 1))
            if beta <= alfa:
                break
        node.minimax = alfa
        return alfa

    else:
        for child in node.children:
            beta = min(beta, minimax(alfa, beta, child, level - 1))
            if beta <= alfa:
                break
        node.minimax = beta
        return beta


