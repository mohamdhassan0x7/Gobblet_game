import pygame
import sys
import pygame
from constants import WIDTH, HEIGHT, SQUARE_SIZE,first_player,second_player, WHITE, GREY, BLACK
from Game import Game
import Player
import sys

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def create_game(option, sub_option = None):
    if option == "Human vs Human":
        game = Game(WIN,Player.Player(first_player),Player.Player(second_player))
    elif option == "Computer vs Computer":
        game = Game(WIN,Player.Player(first_player, True , "Difficult"),Player.Player(second_player, True , "Difficult"))    
    elif option == "Human vs Computer":
        if sub_option == "Easy":
            game = Game(WIN,Player.Player(first_player),Player.Player(second_player, True))    
        elif sub_option == "Medium":
            game = Game(WIN,Player.Player(first_player),Player.Player(second_player, True, "Medium"))    
        elif sub_option == "Difficult":
            game = Game(WIN,Player.Player(first_player),Player.Player(second_player, True, "Difficult"))
    return game        

def run_game(option, sub_option = None):
    run = True
    clock = pygame.time.Clock()
    game = create_game(option, sub_option)    
    game.update()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #pygame.quit()
                run = False
                sys.exit() 
            else:
                res = game.fire(event)
                # print(res)
                if res == "new game":
                    game = create_game(option, sub_option)
                elif res == "main menu":

                    return 
                game.update()
    #pygame.quit()          
####################################################################
