class Piece:
    def __init__(self, index=None, size=None, color=None, children=None):
        self.index = index
        self.size = size
        self.color = color
        self.children = children or {}

    def update_index(self, new_index):
        self.index = new_index

    def update_children(self, new_children):
        self.children = new_children

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
