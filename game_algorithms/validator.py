def check_game_board(game_init):
    # Validate Reversi (Otello) game rules
    rows_valid_nr = 8
    columns_valid_nr = 8


    # Game board must be 8x8 plate
    if(len(game_init)) != rows_valid_nr:
        return (False, f"Number of rows is not equal {rows_valid_nr}")

    for row in game_init:
        if len(row) != columns_valid_nr:
            return (False, f"Number of coumns is not equal {columns_valid_nr}")


    # valid states are:
    # 0 - for empty field
    # 1 - for player `1`
    # 2 - for player `2`
    states_nr = 0
    for row in game_init:
        for state in row:
            if state == 1:
                states_nr += 1
            elif state == 2:
                states_nr -= 1
            elif state != 0:
                return (False, "Inappropriate state")


    # Number of states with value 1 must be equal number of stater with value 2
    if states_nr != 0:
        return (False, "Number of states are not equal")

    return (True, "")