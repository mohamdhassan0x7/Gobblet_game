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
            self.holding_piece.draw(win)
    
    def add_piece_on_board(self,row,col,win):    
        if self.board[row][col-1] != None and self.holding_piece.size ==0 and((self.board[row][col-1].color ==self.left_player.color and self.turn == "l")or(self.board[row][col-1].color ==self.right_player.color and self.turn == "r")) : 
            self.piece_from_board = True
            self.holding_piece.copy_piece(self.board[row][col-1])
            self.holding_piece.draw(win)
            self.holding_piece = self.board[row][col-1]
            # print(self.holding_piece.row,self.holding_piece.col)
            # self.board[row][col-1] = None
            return
        
        if self.piece_from_board == True:
            
            result =self.move_piece((self.holding_piece.row,self.holding_piece.col-1),(row,col-1))
            print(self.board)
            if result == "Placed":
                self.piece_from_board = False
                # self.holding_piece.color = BLACK
                # self.holding_piece.draw(win)
                self.holding_piece = Piece(0,0,None,0,None)
                self.holding_position = None
                self.switch_turn()
                self.print_board(win)
                self.draw_deck(win)
                
        #case playing from hand
        if self.piece_from_board== False:
            if self.holding_piece.size == 0:
                return
            # print(row,col-1)
            result = self.place_piece(self.holding_piece,(row,col-1),'hand')
            if result == "Placed":
                if self.turn == "l":
                    self.left_player.update_stack("stack"+str(self.holding_position+1))
                elif self.turn == "r":
                    self.right_player.update_stack("stack"+str(self.holding_position+1))
                else:
                    print("Error")
                self.holding_piece.color = BLACK
                self.holding_piece.draw(win)
                self.holding_piece = Piece(0,0,None,0,None)
                self.holding_position = None
                self.switch_turn()
                self.print_board(win)
                self.draw_deck(win)
        
        if result.endswith('wins'):
            self.print_board(win)
            self.draw_deck(win)
            return result

    def switch_turn(self):
        if self.turn == "l":
            self.turn = "r"
        else:
            self.turn = "l"
            
    ############################################################################################
        

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
