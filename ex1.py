from Piece import Piece
from Board import Board
from Player import Player
import copy

# Create a board
board = Board()

# Create players
player1 = Player(color="white")
player2 = Player(color="black")

# Display initial state of the board
print("Initial state of the board:")
board.display_board()

# Place initial pieces on the board from player1's stacks
# for row in range(1):
#     for col in range(4):
#         result = board.place_piece(player1.stack1, (row, col), 'hand')
#         # print(result)
#         if result == "Placed":
#             player1.update_stack('stack1')
#         if result == 'black wins' or  result == 'white wins':
#             # print(result)
#             break
        
# Place initial pieces on the board from player2's stacks
# for row in range(3, 4):
#     for col in range(4):
#         result = board.place_piece(player2.stack1, (row, col))
#         if result == "Placed":
#             player2.update_stack(stack_name="stack1")
#         if result == 'black wins' or  result == 'white wins':
#             print(result)
#             break
        
# board.move_piece((0, 1), (0, 3))
# piece1 = Piece(size=1, color="white")
# piece2 = Piece(size=2, color="white")
# piece3 = Piece(size=3, color="white")
# result = board.place_piece(piece1, (0, 0) , 'hand')
# result = board.place_piece(piece2, (0, 1) , 'hand')
# result = board.place_piece(piece3, (0, 2) , 'hand')
# piece4 = Piece(size=4, color="black")
# result = board.place_piece(piece4, (0, 3) , 'hand')
# piece5 = Piece(size=2, color="white")
# piece6 = Piece(size=3, color="white")
# result = board.place_piece(piece5, (1, 3) , 'hand')
# result = board.place_piece(piece6, (2, 3) , 'hand')
# piece7 = Piece(size=4, color="black")
# result = board.place_piece(piece7, (2, 3) , 'hand')

# piece2 = Piece(size=4, color="black")
# result = board.place_piece(piece2, (0, 2) , 'hand')
# piece3 = Piece(size=4, color="black")
# result = board.place_piece(piece3, (0, 3) , 'hand')

# for row in range(4):
#     for col in range(4):
#         if (row == 3 and col == 3) or (row == 3 and col == 2):
#             continue
#         piece4 = Piece(size=4, color="black")
#         result = board.place_piece(piece4, (row, col) , 'hand')
# piece6 = Piece(size=1, color="white")
# result = board.place_piece(piece6, (3, 3) , 'hand')
# result = board.move_piece((3, 3), (0, 0))
# print(result)

# board.move_piece((3, 2), (2, 2))

# board.place_piece(player2.stack2, (0, 1))

# board.move_piece((0, 0), (0, 1))
# piece1 = Piece(size=1, color="black")
# result = board.place_piece(piece1, (0, 0))

# board.move_piece((0, 2), (0, 3))
# board.move_piece((0, 1), (0, 3))


# Display the updated state of the board
print("\nUpdated state of the board:")
board.display_board()