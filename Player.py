from Piece import Piece

class Player:
    def __init__(self, color):
        self.color = color
        self.stack1 = self.initiate_stack()
        self.stack2 = self.initiate_stack()
        self.stack3 = self.initiate_stack()
        
    def initiate_stack(self):
        return Piece(size=4, color=self.color, children=
            Piece(size=3, color=self.color, children=
                Piece(size=2, color=self.color, children=
                    Piece(size=1, color=self.color),
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
            print('hello')























# Create a player
# player1 = Player(color="white")

# Display information about the player's stacks
# print("Player Information:")

# print(player1.color)

# print(player1.stack1)
# player1.update_stack('stack1')
# print(player1.stack1)
# player1.update_stack('stack1')
# print(player1.stack1)
# player1.update_stack('stack1')
# print(player1.stack1)
# player1.update_stack('stack1')
# print(player1.stack1)


# print(player1.stack2)
# print(player1.stack3)