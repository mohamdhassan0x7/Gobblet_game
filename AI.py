from constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE, GREY, BLACK ,first_player,second_player
def minimax(board, depth, max_player):
    if board.check_winner(board.board) != 'No Winner':
        return board.SCORE, board
    if depth == 0 :
        return board.SCORE, board
    if max_player:
        maxEval = float('-inf')
        best_move = None
        for move in board.valid_moves(board , first_player , board.left_player , board.right_player):
            evaluation = minimax(move, depth-1, False)[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                best_move = move
        return maxEval, best_move
    
    else:
        minEval = float('inf')
        best_move = None
        for move in board.valid_moves(board , second_player , board.left_player , board.right_player ):
            evaluation = minimax(move, depth-1, True)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = move
        return minEval, best_move
