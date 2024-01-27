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

   #show selected piece for player[left,right] from deck
   def current_piece(self,row, col, win):
        if self.piece_from_board == True:
            return
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
        if self.holding_piece.size != 0:
            self.draw_deck(win)
            self.holding_position = row
            self.holding_piece.draw(win,True)

    def add_piece_on_board(self,row,col,win):    
        #CASE CLICK OUTSIDE THE BOARD
        if row >3 or col-1 >3:
            return
        
        #HOLD PEICE FROM BOARD
        #print(row , col-1)
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

            self.piece_from_board = True
            self.holding_piece.copy_piece(self.board[row][col-1])
            self.holding_piece.draw(win, True)
            self.holding_piece = self.board[row][col-1]
            return
        
        #CASE PLAYING FROM BOARD
        if self.piece_from_board == True:
            result =self.move_piece((self.holding_piece.row,self.holding_piece.col-1),(row,col-1))
            if result == "Placed":
                self.piece_from_board = False
                self.holding_piece = Piece(0,0,None,0,None)
                self.holding_position = None
                self.switch_turn(win)
                self.print_board(win)
                self.draw_deck(win)
            
        #case playing from hand
        if self.piece_from_board== False:
            if self.holding_piece.size == 0:
                return
            result = self.place_piece(self.holding_piece,(row,col-1),'hand')
            if result == "Placed":
                if self.turn == "l":
                    self.left_player.update_stack("stack"+str(self.holding_position+1))
                elif self.turn == "r":
                    self.right_player.update_stack("stack"+str(self.holding_position+1))
                else:
                    print("Error")
                self.holding_piece.color = BLACK
                self.holding_piece.draw(win,True)
                self.holding_piece = Piece(0,0,None,0,None)
                self.holding_position = None
                self.switch_turn(win)
                self.print_board(win)
                self.draw_deck(win)

        #check if game ends then display result
        if result.endswith('wins') or result == 'Draw':
            self.print_board(win)
            self.draw_deck(win)
            return result  

    def switch_turn(self, win):
        global DrawCase
        # print(self.turn)
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
      ##################################################################################################        
    
    ##################################################################################################
            
    def draw_squares(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, RED, ((row+1)*SQUARE_SIZE, col *SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            for col in range((row+1) % 2, COLS, 2):
                pygame.draw.rect(win, WHITE, ((row+1)*SQUARE_SIZE, col *SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def print_board(self, win):
        self.draw_squares(win)
        for row in range(4):
            for col in range(4):
                if self.board[row][col] is not None:
                    self.board[row][col].draw(win)

    def draw_deck(self, win):
        pygame.draw.rect(win, BLACK, (0, 0, SQUARE_SIZE, SQUARE_SIZE*4))
        pygame.draw.rect(win, BLACK, (5*SQUARE_SIZE, 0, SQUARE_SIZE, SQUARE_SIZE*4))
        if self.left_player.stack1 !=None:
            self.left_player.stack1.draw(win)
        if self.left_player.stack2 !=None:
            self.left_player.stack2.draw(win)
        if self.left_player.stack3 !=None:
            self.left_player.stack3.draw(win)
        
        if self.right_player.stack1 !=None:
            self.right_player.stack1.draw(win)
        if self.right_player.stack2 !=None:
            self.right_player.stack2.draw(win)
        if self.right_player.stack3 !=None:
            self.right_player.stack3.draw(win)

    def draw(self, win):
        self.draw_squares(win)
        self.draw_deck(win)

        
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
        

    def place_piece(self, piece, position, playingPlace):
        row, col = position
        existing_piece = self.grid[row][col]

        pieceCopy = copy.copy(piece) 
        pieceCopy.update_children(None)

        if existing_piece:
            if existing_piece.size >= piece.size:
                return "Error"
            if playingPlace != 'board':
                valid = self.check_can_play(self.grid , pieceCopy.color , existing_piece)
                print(valid)
                if valid == 'valid move':
                    pieceCopy.update_children(existing_piece)
                else:
                    return "Error"
            else:
                pieceCopy.update_children(existing_piece)
        self.grid[row][col] = pieceCopy
        pieceCopy.update_index(position)
        if(playingPlace != 'board'):
            winner = self.check_winner(self.grid)
            if winner != 'No Winner':
                return winner + ' wins'
        return "Placed"

    def move_piece(self, start_position, end_position):

        start_row, start_col = start_position
        end_row, end_col = end_position

        piece_to_move = self.grid[start_row][start_col]
        pieceChildren = piece_to_move.children
        result = self.place_piece(piece_to_move , end_position ,'board')
        if result == "Error":
            #other options to play or no other options 
            playerLost = self.check_lose(piece_to_move)
            if playerLost:
                print('user Lost')
                return
            return result
        elif result == "Placed":
            if pieceChildren:
                self.grid[start_row][start_col] = pieceChildren
            else:
                self.grid[start_row][start_col] = None
            winner = self.check_winner(self.grid)
            if winner != 'No Winner':
                return '{winner} wins'
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
