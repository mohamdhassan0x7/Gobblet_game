from Piece import Piece
from constants import first_player

class Player:
   def __init__(self, color, ai = False, level = "Easy"):
        self.level = level
        self.ai = ai
        self.color = color
        self.stack1 = self.initiate_stack(0)
        self.stack2 = self.initiate_stack(1)
        self.stack3 = self.initiate_stack(2)
        
    def initiate_stack(self,r):
        col=None
        if self.color == first_player:
            col = 0
        else:
            col = 5
        return      Piece(col = col,row=r,size=4, color=self.color, children=
                    Piece(col = col,row=r,size=3, color=self.color, children=
                    Piece(col = col,row=r,size=2, color=self.color, children=
                    Piece(col = col,row=r,size=1, color=self.color, children=None),
                ),
            ),
        )
    
    def update_stack(self, stack_name):
        if stack_name == "stack1":
            stack = getattr(self, stack_name)
            setattr(self, stack_name, stack.children)
        elif stack_name == "stack2":
            stack = getattr(self, stack_name)
            setattr(self, stack_name, stack.children)
        elif stack_name == "stack3":
            stack = getattr(self, stack_name)
            setattr(self, stack_name, stack.children)
        else:
            print("Invalid stack name")
            return

