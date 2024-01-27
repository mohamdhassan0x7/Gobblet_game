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

####################################################################### Iterative #####################################################

########################################################################################################################################

def alpha_beta_pruning(board, depth, max_player, start_time = None , time_limit= None , alpha = float('-inf'), beta = float('inf')):
    #stop search if time exceeds limit [iterative deepening]
    if  (start_time != None and ((time.time() - start_time) > time_limit)):
        return None, None

    #if goal is found, then return it.
    if board.check_winner(board.board) != 'No Winner':
        return board.SCORE, board

    #evaluate leaf nodes
    if (depth == 0) :
        return board.SCORE, board

    #Maxmizer turn
    if max_player:
        maxEval = float('-inf')
        best_move = None

        #iterate on all valid moves for current state
        for move in board.valid_moves(board , first_player , board.left_player , board.right_player ,True ):
            evaluation = alpha_beta_pruning(move, depth-1, False,start_time , time_limit, alpha, beta)[0]

            #iterative deepening case
            if evaluation == None:
                return None, None
                
            maxEval = max(maxEval, evaluation)
            
            # Alpha Beta Pruning step
            alpha = max(alpha, maxEval)
            if beta <= alpha:
                break
                
            if maxEval == evaluation:
                best_move = move               
        return maxEval, best_move
    
    else:
        minEval = float('inf')
        best_move = None
        
        #iterate on all valid moves for current state
        for move in board.valid_moves(board , second_player , board.left_player , board.right_player ,False ):
            evaluation = alpha_beta_pruning(move, depth-1, True, start_time , time_limit, alpha, beta)[0]

            #iterative deepening case
            if evaluation == None:
                return None, None
                
            minEval = min(minEval, evaluation)
            
            # Alpha Beta Pruning step
            beta = min(beta, minEval)
            if beta <= alpha:
                break
            
            if minEval == evaluation:
                best_move = move             
        return minEval, best_move
