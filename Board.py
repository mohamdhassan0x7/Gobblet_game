from Piece import Piece
import copy

class Board:
    
    def __init__(self):
        self.grid = [[None for _ in range(4)] for _ in range(4)]
        self.left_player = player1
        self.right_player = player2
        self.holding_piece = Piece(0,0,None,0,None)
        self.board = [[None for _ in range(4)] for _ in range(4)]
        self.turn = "l"
        self.holding_position = None
        self.piece_from_board = False

    def draw_squares(self, win):
        win.fill(GREY)
        # Human vs Human mode : Only mode that contains draw button
        if self.left_player.ai == False and self.right_player.ai == False: 
            font = pygame.font.Font("8-BIT_WONDER.TTF", 12)
            drawBtn = pygame.Rect((WIDTH//2)-80, 5, 160, 30)
            pygame.draw.rect(win, (153, 88, 42), drawBtn, border_radius=20)

            if (DrawCase == DrawPressed):
                pygame.draw.rect(win, (111, 29, 27), drawBtn, border_radius=20)
                # the player who requests draw can not accept this draw
                if(self.turn != self.playerReqDraw):
                    drawBtn_text = font.render("ACCEPT DRAW", True, (247, 231, 206))
                else:
                    drawBtn_text = font.render("REQUEST DRAW", True, (247, 231, 206))    
            else:
                drawBtn_text = font.render("REQUEST DRAW", True, (247, 231, 206))        


            drawBtn_text_rect = drawBtn_text.get_rect(center=drawBtn.center)
            win.blit(drawBtn_text, drawBtn_text_rect)
        # draw board tiles 
        for row in range(ROWS):
            for col in range(row % 2, 4, 2):
                pygame.draw.rect(win, RED, ((row+1)*SQUARE_SIZE , col *SQUARE_SIZE + ZERO_Y, SQUARE_SIZE, SQUARE_SIZE))
            for col in range((row+1) % 2, 4, 2):
                pygame.draw.rect(win, WHITE, ((row+1)*SQUARE_SIZE , col *SQUARE_SIZE + ZERO_Y, SQUARE_SIZE, SQUARE_SIZE))
   

    #show selected piece for player[left,right] from deck
   def current_piece(self,row, col, win):
        if self.piece_from_board == True:
            return
        #check for player has clicked on his stack and which stack is clicked on then hold piece from top of this stack
        if((col ==0) and row<3 and self.turn == "l" ):
            if row == 0 and self.left_player.stack1 != None:
                self.holding_piece.copy_piece(self.left_player.stack1)
            elif row == 1 and self.left_player.stack2 != None:
                self.holding_piece.copy_piece(self.left_player.stack2)
            elif row == 2 and self.left_player.stack3 != None:
                self.holding_piece.copy_piece(self.left_player.stack3)
        elif((col == COLS-1) and row<3 and self.turn == "r"):
            if row == 0 and self.right_player.stack1 != None:
                self.holding_piece.copy_piece(self.right_player.stack1)
            elif row == 1 and self.right_player.stack2 != None:
                self.holding_piece.copy_piece(self.right_player.stack2)
            elif row == 2 and self.right_player.stack3 != None:
                self.holding_piece.copy_piece(self.right_player.stack3)
                
        #check if there is holding piece, then draw it
        if self.holding_piece.size != 0:
            self.draw_deck(win)
            self.holding_position = row
            self.holding_piece.draw(win,True)

    def add_piece_on_board(self,row,col,win):    
        #CASE CLICK OUTSIDE THE BOARD
        if row >3 or col-1 >3:
            return

        #check if the player is holding his own piece from the board
        #HOLD PEICE FROM BOARD
        if self.board[row][col-1] != None and self.holding_piece.size ==0 and((self.board[row][col-1].color ==self.left_player.color and self.turn == "l")or(self.board[row][col-1].color ==self.right_player.color and self.turn == "r")) : 
            valid = False
            for r in range (4):
                for c in range (4):
                    if self.board[r][c] == None or (self.board[r][c].color != self.board[row][col-1].color and self.board[r][c].size < self.board[row][col-1].size):
                        valid = True
                        break
                        
            #CASE HOLDING PIECE FROM BOARD AND HAVE NO VALID MOVES (PLAYER LOSE)
            if valid == False:
                self.switch_turn(win)
                if self.turn == 'r':
                    return "right player wins"
                else:
                    return "left player wins" 

            #piece is selected from board, holding piece will contain this piece
            self.piece_from_board = True
            self.holding_piece.copy_piece(self.board[row][col-1])

            #draw holding piece (copy piece)
            self.holding_piece.draw(win, True)

            self.holding_piece = self.board[row][col-1]
            return
        
        #CASE PLAYING FROM BOARD
        if self.piece_from_board == True:
            
            result =self.move_piece((self.holding_piece.row,self.holding_piece.col-1),(row,col-1))
            #if new destination is valid for the piece
            if result == "Placed":
                #remove holding piece
                self.piece_from_board = False
                self.holding_piece = Piece(0,0,None,0,None)
                self.holding_position = None
                self.switch_turn(win)
                #update gui
                self.print_board(win)
                self.draw_deck(win)
            
        #case playing from hand
        if self.piece_from_board== False:
            
            #if there is no holding piece, return
            if self.holding_piece.size == 0:
                return
                
            result = self.place_piece(self.holding_piece,(row,col-1),'hand')
            
            #if new destination is valid for the piece
            if result == "Placed":
                #update stacks
                if self.turn == "l":
                    self.left_player.update_stack("stack"+str(self.holding_position+1))
                elif self.turn == "r":
                    self.right_player.update_stack("stack"+str(self.holding_position+1))
                else:
                    print("Error")
                #remove holding piece from gui
                self.holding_piece.color = BLACK
                self.holding_piece.draw(win,True)
                self.holding_piece = Piece(0,0,None,0,None)
                self.holding_position = None
                self.switch_turn(win)
                #update gui
                self.print_board(win)
                self.draw_deck(win)

        #check if game ends then display result
        if result.endswith('wins') or result == 'Draw':
            self.print_board(win)
            self.draw_deck(win)
            return result  

    def switch_turn(self, win):
        global DrawCase
        if self.turn == "l":
            self.turn = "r"
        else:
            self.turn = "l"
        # in case player 1 requested draw and player 2 didn't accept draw 
        if self.turn == self.playerReqDraw:
            self.playerReqDraw = None
            DrawCase = DrawReleased
            self.print_board(win)
            self.draw_deck(win)
            
    def draw_deck(self, win):
        pygame.draw.rect(win, BLACK, (15, 40, SQUARE_SIZE-30, SQUARE_SIZE*3), border_radius=10)
        pygame.draw.rect(win, BLACK, (5*SQUARE_SIZE + 15, 40, SQUARE_SIZE - 30, SQUARE_SIZE*3), border_radius=10)
    
        # DRAW HOLD PLACE
        if self.turn == "l":
            pygame.draw.rect(win, TURN, (15, SQUARE_SIZE*3 + 70, SQUARE_SIZE-30, SQUARE_SIZE-30), border_radius=10)
            pygame.draw.rect(win, BLACK, (5*SQUARE_SIZE + 15, SQUARE_SIZE*3 + 70, SQUARE_SIZE-30, SQUARE_SIZE-30), border_radius=10)
        else:
            pygame.draw.rect(win, BLACK, (15, SQUARE_SIZE*3 + 70, SQUARE_SIZE-30, SQUARE_SIZE-30), border_radius=10)
            pygame.draw.rect(win, TURN, (5*SQUARE_SIZE + 15, SQUARE_SIZE*3 + 70, SQUARE_SIZE-30, SQUARE_SIZE-30), border_radius=10)
    
        if self.left_player.stack1 is not None:
            self.left_player.stack1.draw(win)
        if self.left_player.stack2 is not None:
            self.left_player.stack2.draw(win)
        if self.left_player.stack3 is not None:
            self.left_player.stack3.draw(win)

        if self.right_player.stack1 is not None:
            self.right_player.stack1.draw(win)
        if self.right_player.stack2 is not None:
            self.right_player.stack2.draw(win)
        if self.right_player.stack3 is not None:
            self.right_player.stack3.draw(win)

    def draw(self, win):
        self.draw_squares(win)            
        self.draw_deck(win)

    def print_board(self, win):
        self.draw_squares(win)
            for row in range(4):
                for col in range(4):
                    if self.board[row][col] is not None:
                        self.board[row][col].draw(win)
    
        self.SCORE = self.evaluate()

    def display_winner_panel(winner,win):
        # Display the winner panel
        font = pygame.font.SysFont("Arial", 50)
        winner_text = font.render(f"Player {winner} wins!", True, WHITE)
        winner_rect = winner_text.get_rect(center=( WIDTH// 2, HEIGHT // 2))

        win.fill(BLACK)
        win.blit(winner_text, winner_rect.topleft)

        pygame.display.flip()

        # Wait for a moment to show the winner panel
        pygame.time.delay(3000)
    
    ########################################################################################################################

    ########################################################################################################################  
    def cal_score(self,color):
        winner = self.check_winner(self.board)
        # whenever find winner move, return high score to make this move
        if winner != 'No Winner':
            if winner == color:
                return 99999999
            else:
                return -99999999  
        score=[1, 1.1, 1.15, 1.17]
        score_row = 0
        score_col = 0
        score_diagonal_R = 0
        score_diagonal_C = 0 

        max_score = 0
        counter_r = 0
        counter_c = 0
        counter_d_r = 0
        counter_d_l = 0
        #ROWS AND COLUMNS
        for row in range(4):
            for col in range(4):
                if self.board[row][col] != None:
                    # if the board has pieces of same color in a row
                    if self.board[row][col].color == color:
                        counter_r+=1
                        # calculating score depends on both size of pieces in row and count of them as well
                        score_row += (counter_r * score[self.board[row][col].size-1])
                        #update max score in case of better move
                        if score_row > max_score:
                            max_score = score_row
                    else:
                        score_row = 0 
                        counter_r = 0   
                else:
                    score_row = 0 
                    counter_r = 0

                if self.board[col][row] != None:
                    # if the board has pieces of same color in a collumn
                    if self.board[col][row].color == color:
                        counter_c+=1
                        # calculating score depends on both size of pieces in column and count of them as well
                        score_col += (counter_c * score[self.board[col][row].size-1])
                        #update max score in case of better move
                        if score_col > max_score:
                            max_score = score_col
                    else:
                        score_col = 0
                        counter_c = 0     
                else:
                    score_col = 0  
                    counter_c = 0            

        #DIAGONAL TO RIGHT
        for col in range(4):
            start_c = col 
            start_r = 0
            for r,c in zip(range(start_r, 4), range(start_c, 4)):
                #FIRST DIAGONAL (ROW 0)
                if self.board[r][c] != None:
                    # if the board has pieces of same color in the main Diagonal
                    if self.board[r][c].color == color and c == r:
                        counter_d_r+=1
                        score_diagonal_R += (counter_d_r*score[self.board[r][c].size-1])
                        if score_diagonal_R > max_score:
                            max_score = score_diagonal_R
                    else:
                        score_diagonal_R = 0  
                        counter_d_r = 0  
                else:
                    score_diagonal_R = 0 
                    counter_d_r = 0

            score_diagonal_C = 0
            score_diagonal_R = 0 
       
       #DIAGONAL TO LEFT
        for col in range(4):
            start_c = col 
            start_r = 3
            for r,c in zip(range(start_r, 0, -1), range(start_c, 4)):
                #FIRST DIAGONAL (ROW 4)
                if self.board[r][c] != None:
                    # if the board has pieces of same color in opposite daigonal
                    if self.board[r][c].color == color and c == 3-r:
                        counter_d_l+=1
                        score_diagonal_R += (counter_d_l*score[self.board[r][c].size-1])
                        if score_diagonal_R > max_score:
                            max_score = score_diagonal_R
                    else:
                        score_diagonal_R = 0 
                        counter_d_l = 0   
                else:
                    score_diagonal_R = 0 
                    counter_d_l = 0

            score_diagonal_C = 0
            score_diagonal_R = 0 

        return max_score

    def evaluate(self):
        #returns the subtraction of left player score and right plaayer score to choose move
        left_score = self.cal_score(self.left_player.color)
        right_score = self.cal_score(self.right_player.color)
        self.SCORE = (left_score - right_score)
        return self.SCORE
    
    def draw_Req(self, win):
        global DrawCase
        #show accept draw to the other player 
        if self.turn != self.playerReqDraw:
            #case first player request draw 
            if DrawCase == DrawReleased:
                DrawCase = DrawPressed
                self.playerReqDraw = self.turn
                self.print_board(win)
                self.draw_deck(win)
                if self.holding_position != None:
                    self.holding_piece.draw(win)
            # case of accepting draw by second player, show popup window
            elif DrawCase == DrawPressed:
                DrawCase = DrawReleased
                self.print_board(win)
                self.draw_deck(win)  
                if self.holding_position != None:
                    self.holding_piece.draw(win)  
                return "Draw"


    def place_piece(self, piece, position, playingPlace):
        row, col = position
        
        existing_piece = self.board[row][col]

        pieceCopy = copy.copy(piece) 
        pieceCopy.update_children(None)

        if existing_piece:
            if (existing_piece.size >= piece.size) or (existing_piece.color == piece.color):
                return "Error"
            if playingPlace != 'board':
                valid = self.check_can_play(self.board , pieceCopy.color , existing_piece)
                #print(valid)
                if valid == 'valid move':
                    self.FirstPlayerMoves = [None for _ in range(6)]
                    self.SecondPlayerMoves = [None for _ in range(6)]
                    pieceCopy.update_children(existing_piece)
                else:
                    return "Error"
            else:
                pieceCopy.update_children(existing_piece)
        self.board[row][col] = pieceCopy
        pieceCopy.update_index(position)            
        if(playingPlace != 'board'):
            self.FirstPlayerMoves = [None for _ in range(6)]
            self.SecondPlayerMoves = [None for _ in range(6)]
            winner = self.check_winner(self.board)
            if winner != 'No Winner':
                if winner == self.left_player.color:
                    return "left player wins"
                else:
                    return "right player wins"
        return "Placed"

   def move_piece(self, start_position, end_position):
        start_row, start_col = start_position
        end_row, end_col = end_position
        piece_to_move = self.board[start_row][start_col]
        pieceChildren = piece_to_move.children
        result = self.place_piece(piece_to_move , end_position ,'board')
        if result == "Error":
            #other options to play or no other options 
            playerLost = self.check_lose(piece_to_move)
            if playerLost != False:
                if playerLost == self.left_player.color:
                    return "right player wins"
                else:
                    return "left player wins" 
            return result    
        elif result == "Placed":
            if pieceChildren:
                self.board[start_row][start_col] = pieceChildren
            else:
                self.board[start_row][start_col] = None
            winner = self.check_winner(self.board)
            
            if winner != 'No Winner':
                if winner == self.left_player.color:
                    return "left player wins"
                else:
                    return "right player wins"
            if piece_to_move.color == first_player:
                if self.FirstPlayerIndex == 6:
                    self.FirstPlayerIndex = 0
                self.FirstPlayerMoves[self.FirstPlayerIndex] = [start_position , end_position]
                self.FirstPlayerIndex += 1
            if piece_to_move.color == second_player:
                if self.SecondPlayerIndex == 6:
                    self.SecondPlayerIndex = 0
                self.SecondPlayerMoves[self.SecondPlayerIndex] = [start_position , end_position]
                self.SecondPlayerIndex += 1
            drawResult = self.check_draw(self.FirstPlayerMoves , self.SecondPlayerMoves)
            #print(drawResult)
            if drawResult:
                return 'Draw'
            return result

    def display_board(self):
        for row in self.grid:
            for cell in row:
                print(cell if cell else "Empty", end="\t")
            print()

    def check_winner(self , board):
        # Check rows
        for row in board:
            if self.check_line(row):
                return row[0].color  

        # Check columns
        for col in range(4):
            column = [board[row][col] for row in range(4)]
            if self.check_line(column):
                return column[0].color  

        # Check diagonals
        main_diagonal = [board[i][i] for i in range(4)]
        anti_diagonal = [board[i][3 - i] for i in range(4)]

        if self.check_line(main_diagonal):
            return main_diagonal[0].color   
        elif self.check_line(anti_diagonal):
            return anti_diagonal[0].color  

        return 'No Winner' 

    def check_line(self , line):
        if None in line:
            return None 
        else:
            first_element = line[0].color 
            return all(element.color == first_element and element is not None for element in line)

    def check_can_play(self , board , color , piece):
        # Check rows
        for row in board:
            if piece in row:
                if self.check_valid(row , color):
                    return 'valid move'  

        # Check columns
        for col in range(4):
            column = [board[row][col] for row in range(4)]
            if piece in column:
                if self.check_valid(column , color):
                    return 'valid move'

        # Check diagonals
        main_diagonal = [board[i][i] for i in range(4)]
        anti_diagonal = [board[i][3 - i] for i in range(4)]

        if piece in main_diagonal:
            if self.check_valid(main_diagonal , color):
                return 'valid move'
        if piece in anti_diagonal:
            if self.check_valid(anti_diagonal , color):
                return 'valid move'

        return 'Not valid move' 

    def check_valid(self , line , color):
        counter = 0
        for element in line:
            if element == None:
                counter +=1 
        if counter >= 2:
            return False
        elif counter == 1:
            index = None
            for element in line:
                if element == None:
                    index = line.index(element) 
            if index != 0 and index !=3:
                return False
            else:
                color = None
                for element in line:
                    if element == None:
                        continue
                    else:
                        if color == None:
                            color = element.color
                        else:
                            if element.color == color:
                                continue
                            else:
                               return False 
                return True
        elif counter == 0:
            colorCounter = 0
            for element in line:
                if element.color != color:
                    colorCounter +=1 
            if colorCounter < 3:
                return False
            elif colorCounter == 3 :
                index = None
                for element in line:
                    if element.color == color:
                        index = line.index(element) 
                if index != 0 and index !=3:
                    return False
                else:
                    return True

    def check_lose(self , piece):
        for row in range(4):
            for col in range(4):
                element = self.grid[row][col]
                if element == None:
                    return False
                if piece.size > element.size:
                    return False
        return True        
    
    def valid_moves( self, Board , color , player1 , player2 , max = None):         
                validMoves = []
                for stackNum in range(3):
                    for row in range(4):
                        for col in range(4):
                            temp_board = copy.deepcopy(Board) 
                            tempFirstPlayerStack = [ temp_board.left_player.stack1, temp_board.left_player.stack2 , temp_board.left_player.stack3]
                            tempSecondPlayerStack = [ temp_board.right_player.stack1 , temp_board.right_player.stack2 , temp_board.right_player.stack3]
                            #color
                            if color == first_player :
                                if stackNum != 0:
                                    if stackNum == 1: 
                                        if tempFirstPlayerStack[stackNum -1] != None and tempFirstPlayerStack[stackNum] != None :
                                            if tempFirstPlayerStack[stackNum].size == tempFirstPlayerStack[stackNum -1].size :
                                                continue
                                    if stackNum == 2: 
                                        if tempFirstPlayerStack[stackNum -1] != None and tempFirstPlayerStack[stackNum] != None:
                                            if tempFirstPlayerStack[stackNum].size == tempFirstPlayerStack[stackNum -1].size:
                                                continue
                                        if tempFirstPlayerStack[stackNum -2] != None and tempFirstPlayerStack[stackNum] != None:
                                            if  tempFirstPlayerStack[stackNum].size == tempFirstPlayerStack[stackNum - 2].size:
                                                continue
                                if tempFirstPlayerStack[stackNum] != None:
                                    result = temp_board.place_piece(tempFirstPlayerStack[stackNum] , (row , col) , 'hand') 
                                else:
                                    continue
                            if color == second_player :
                                if stackNum != 0:
                                    if stackNum == 1: 
                                        if tempSecondPlayerStack[stackNum -1] != None and tempSecondPlayerStack[stackNum] != None :
                                            if tempSecondPlayerStack[stackNum].size == tempSecondPlayerStack[stackNum -1].size :
                                                continue
                                    if stackNum == 2: 
                                        if tempSecondPlayerStack[stackNum -1] != None and tempSecondPlayerStack[stackNum] != None:
                                            if tempSecondPlayerStack[stackNum].size == tempSecondPlayerStack[stackNum -1].size:
                                                continue
                                        if tempSecondPlayerStack[stackNum -2] != None and tempSecondPlayerStack[stackNum] != None:
                                            if  tempSecondPlayerStack[stackNum].size == tempSecondPlayerStack[stackNum - 2].size:
                                                continue
                                if tempSecondPlayerStack[stackNum] != None:
                                    result = temp_board.place_piece(tempSecondPlayerStack[stackNum] , (row , col) , 'hand') 
                                else:
                                    continue
                            if result == "Placed" or result.endswith('wins'):
                                value = stackNum + 1
                                if color == first_player :
                                    temp_board.left_player.update_stack('stack'+ str(value) )
                                if color == second_player :
                                    temp_board.right_player.update_stack('stack' + str(value) )
                                temp_board.evaluate()
                                validMoves.append(temp_board)
                                for row in range(4):
                for col in range(4):
                    temp_board = copy.deepcopy(Board) 
                    if temp_board.board[row][col] != None:
                        if temp_board.board[row][col].color == color:
                            for boardRow in range(4):
                                for boardCol in range(4):
                                    temp_board1 = copy.deepcopy(temp_board) 
                                    if row == boardRow and col == boardCol:
                                        continue
                                    result = temp_board1.move_piece((row , col) , (boardRow , boardCol) )
                                    if result == "Placed" or result.endswith('wins') :
                                        temp_board1.evaluate()
                                        validMoves.append(temp_board1)
                random.shuffle(validMoves)
                if max != None and max == True:
                   validMoves = sorted(validMoves, key=lambda obj: obj.SCORE , reverse=True)
                elif max != None and max == False:
                   validMoves = sorted(validMoves, key=lambda obj: obj.SCORE)
                
                return validMoves

def check_draw(self , player1Array , player2Array):
        if None in player1Array :
            return False
        if None in player2Array :
            return False
        
        firstFlag = False 
        secondFlag = False 
        thirdFlag = False 
        FirstPlayerDraw = False
        for pieceNum in range(2):
            if player1Array[pieceNum][0] == player1Array[pieceNum+2][0] and player1Array[pieceNum][0] == player1Array[pieceNum+4][0] :
                if player1Array[pieceNum][1] == player1Array[pieceNum+2][1] and player1Array[pieceNum][1] == player1Array[pieceNum+4][1] :
                    if pieceNum == 0:
                        firstFlag = True
                    if pieceNum == 1:
                        secondFlag = True
        if player1Array[0][0] == player1Array[1][1] and player1Array[0][1] == player1Array[1][0]:
            if player1Array[2][0] == player1Array[3][1] and player1Array[2][1] == player1Array[3][0]:
                if player1Array[4][0] == player1Array[5][1] and player1Array[4][1] == player1Array[5][0]:
                    thirdFlag = True
        if firstFlag and secondFlag and thirdFlag:
            FirstPlayerDraw = True










# board = Board()

# piece1 = Piece(size=2, color="black")
# piece2 = Piece(size=4, color="black")
# piece3 = Piece(size=1, color="black")
# piece4 = Piece(size=3, color="black")

# result = board.place_piece(piece1, (1, 1))
# print("Current State of the Board:")
# board.display_board()
# print(result)
# print('\n')
# result = board.place_piece(piece2, (1, 1))
# print("Current State of the Board:")
# board.display_board()
# print(result)
# print('\n')
# result = board.place_piece(piece3, (1, 1))
# print("Current State of the Board:")
# board.display_board()
# print(result)

# piece1 = Piece(size=3, color="white")
# piece2 = Piece(size=2, color="black")
# piece3 = Piece(size=1, color="black")

# print("Placing piece3:", board.place_piece(piece3, (0, 0)))
# print("Placing piece1:", board.place_piece(piece1, (1, 1)))
# print("Placing piece2:", board.place_piece(piece2, (2, 2)))
# print("Placing piece2:", board.place_piece(piece4, (3, 3)))

# Display the initial state of the board
# print("\nInitial state of the board:")
# board.display_board()

# result = board.check_winner(board.grid)
# print(result)

# # Move a piece on the board
# print("\nMoving piece1 to (2, 2):", board.move_piece((1, 1), (2, 2)))

# # Display the updated state of the board
# print("\nUpdated state of the board:")
# board.display_board()

# # Move a piece on the board
# print("\nMoving piece1 to (2, 2):", board.move_piece((2, 2), (0, 0)))

# # Display the updated state of the board
# print("\nUpdated state of the board:")
# board.display_board()
