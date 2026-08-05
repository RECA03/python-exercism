def gamestate(board):

    #convert the rows to lists
    for i, row in enumerate(board):
        board[i] = list(row)
    
    #count how many Xs and 0s
    X_counter, O_counter = 0, 0
    for row in board:
        X_counter += row.count("X")
        O_counter += row.count("O")
    
    moves_made = X_counter + O_counter

    if X_counter - O_counter > 1:
        raise ValueError("Wrong turn order: X went twice")
    if O_counter > X_counter:
        raise ValueError("Wrong turn order: O started")
    
    #Crossed combinations (row, col)
    all_combos = [[(0,0),(1,1),(2,2)],[(2,0),(1,1),(0,2)],
                    [(0,0),(0,1),(0,2)],[(1,0),(1,1),(1,2)],[(2,0),(2,1),(2,2)],
                    [(0,0),(1,0),(2,0)],[(0,1),(1,1),(2,1)],[(0,2),(1,2),(2,2)]]
    
    #evaluate combos
    x_wins = 0
    o_wins = 0
    for combo in all_combos:
        r1, c1 = combo[0]
        r2, c2 = combo[1]
        r3, c3 = combo[2]

        if board[r1][c1] == board[r2][c2] == board[r3][c3] and board[r1][c1]:
            if board[r1][c1] == "X":
                x_wins += 1
            elif board[r1][c1] == "O":
                o_wins += 1
        
    #evaluate board state
    if x_wins > 0 and o_wins > 0:
        raise ValueError("Impossible board: game should have ended after the game was won")
    if x_wins > 0:
        # If X won, X must have made 1 more move than O (game ends immediately on X's win)
        if X_counter <= O_counter:
            raise ValueError("Impossible board: game should have ended after the game was won")
        return "win"
    if o_wins > 0:
        # If O won, X and O must have an equal number of moves
        if X_counter != O_counter:
            raise ValueError("Impossible board: game should have ended after the game was won")
        return "win"
    if moves_made == 9:
        return "draw"
        
    return "ongoing"