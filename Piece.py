from constants import RED, WHITE, SQUARE_SIZE, GREY , BLACK,first_player,second_player
import pygame

class Piece:
    PADDING = 15
    OUTLINE = 2
    def __init__(self,row,col, color, size, children=None):
        self.index = index
        self.size = size
        self.color = color
        self.x = 0
        self.y = 0
        self.calc_pos()
        self.size = size
        self.row = row
        self.col = col
        self.children = children or None

    def update_index(self, new_index):
        self.row, self.col = new_index
        self.col +=1
        self.calc_pos()
    def update_children(self, new_children):
        self.children = new_children
    def draw(self,win):
        if(self.size == 0):
            radius=self.OUTLINE=0
        else:
            radius = SQUARE_SIZE//(6-self.size) - self.PADDING
        pygame.draw.circle(win,BLACK, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2
    
    def copy_piece(self, piece):
        self.row = 3
        if piece.color == first_player:
            self.col = 0
        else:
            self.col = 5
        # self.col = piece.col
        self.color = piece.color
        self.size = piece.size
        self.children = piece.children
        self.calc_pos()
        return self
    
    def __str__(self):
        return f"Piece(index={self.index}, size={self.size}, color={self.color} , children={self.children})"
























  
    
# Create a piece
# piece1 = Piece(size=3, color="white")
# piece2 = Piece(size=2, color="black")

# print(piece1)

# Display information about the piece
# new_index = (2, 2)
# piece1.update_index(new_index)
# piece1.update_children(piece2)

# print("Piece Information:")
# print(piece1)
# print(piece2)
