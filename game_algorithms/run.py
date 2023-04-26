import time

from game_algorithms.reversi import start_game

# EXAMPLES

# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0
# 0 0 0 1 2 0 0 0
# 0 0 0 2 1 0 0 0
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0
# END

# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0
# 0 0 1 2 0 0 0 0
# 0 0 0 1 2 0 0 0
# 0 0 0 2 1 0 0 0
# 0 0 0 0 2 1 0 0
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0
# END

# 0 0 0 0 0 0 0 0
# 0 0 0 1 1 1 0 0
# 0 2 2 2 2 1 0 0
# 0 0 2 2 2 2 1 0
# 0 0 0 2 1 0 1 0
# 0 0 0 0 2 1 0 0
# 0 0 0 0 1 1 2 0
# 0 0 0 0 0 1 0 0
# END

if __name__ == '__main__':
    start_time = time.time()
    start_game(verbose=False, alfa_beta_prune=True)
    end_time = time.time()

    print(f"Time elapsed: {end_time-start_time}")