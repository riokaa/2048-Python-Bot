#searches player moves to the given depth, returning the best move and score
def playerSearch(array, depth, ply):

    best_score = -1
    best_move = 'down'  #best move by default, always replaced unless no others are available
    pv = [0 for x in range(0, ply + 1)]
    moves = ['left', 'right', 'up', 'down']

    if (depth <= 0):
        return (best_move, evaluateBoard(array), 'end')

    #search each move
    for move in moves:

        score = -1

        #make move
        (new_board, move_score) = makeMove(array, move)

        #if move is not successful
        if (move_score == -1):
            continue

        else:  #call computer_search function
            (score, pv_temp) = computerSearch(new_board, best_score, depth - 1, ply + 1)

        #Update best score, move and pv
        if (score > best_score):
            best_score = score
            best_move = move
            pv[0] = move
            pv[1:] = pv_temp[::]

    #Return best move and score
    return (best_move, best_score, pv)


#searches all computer moves, returning the minimum score found
def computerSearch(array, best_score, depth, ply):

    pv = [0 for x in range(0, ply + 1)]
    if (depth <= 0):
        return (evaluateBoard(array), "X")

    worst_score = 100000000
    total = 0
    moves_made = 0

    #Loop through all squares, make computer move if empty
    for sq in range(0, 16):

        #Continue if square is not empty
        if (array[sq % 4][sq // 4] != 0):
            continue

        #make move
        new_board = makeComputerMove(array, sq)

        #call player_search function
        (temp, score, pv_temp) = playerSearch(new_board, depth - 1, ply + 1)

        #cutoff
        #if(score < best_score):
        #return (score, pv)

        #update average
        total += score
        moves_made += 1

        #update worst score
        if (score < worst_score):
            worst_score = score
            pv[0] = sq
            pv[1:] = pv_temp[::]

    #Adjustment for leaving square 0 or 1 open at any time during search
    if (array[0][0] == 0):
        worst_score *= (1 - 0.1 * depth)

    if (array[1][0] == 0):
        worst_score *= (1 - 0.03 * depth)

    return (worst_score, pv)


#Returns the score of the board
def evaluateBoard(array):

    score = 0
    maximum = 0
    for sq in range(0, 16):
        score += SQUARE_SCORES[array[sq % 4][sq // 4]] * SQUARE_MULTS[sq]
        if (array[sq % 4][sq // 4] > maximum):
            maximum = array[sq % 4][sq // 4]

    #bonus for having highest square in top left
    if (array[0][0] == maximum):
        score *= 1.4

    return score


class Bot:
    def search(self, cells, verbose=False):
        (move, score, pv) = playerSearch(board, 5, 0)

        if verbose:
            print("Move: ", move, " Score: ", score)
            print("PV: ", pv[::], "\n\n")

        (left, score) = makeMove(board, 'left')
        
        if verbose:
            printBoard(left, 'Left')
            print("Move score: ", score)

        return move
