import pygame
import sys
import pygame
from constants import WIDTH, HEIGHT, SQUARE_SIZE,first_player,second_player, WHITE, GREY, BLACK
from Game import Game
import Player
import sys

import random

#get coordinates of the select
def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

#based on mode ==> instaniate object of game with needed parameters
def create_game(option, sub_option = None):
    if option == "Human vs Human":
        game = Game(WIN,Player.Player(first_player),Player.Player(second_player))
    elif option == "Computer vs Computer":
        random_number = random.choice([1, 2])
        if random_number == 1:
            game = Game(WIN,Player.Player(first_player, True , "Medium"),Player.Player(second_player, True , "Easy"))  
        else:
            game = Game(WIN,Player.Player(first_player, True , "Easy"),Player.Player(second_player, True , "Medium"))      
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
                run = False
                sys.exit() 
            else:
                res = game.fire(event)
                #based on return value:
                #new game  ==> create game with same option and sub options.
                #main menu ==> return to main screen
                if res == "new game":
                    game = create_game(option, sub_option)
                elif res == "main menu":

                    return 
                #update gui
                game.update()    

FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Gobblet Gobblers')
icon_image = pygame.image.load("brown.png")  # Replace "icon.png" with the path to your image file

resized_icon = pygame.transform.scale(icon_image, (64,64))
# Set the window icon
pygame.display.set_icon(resized_icon)
# Initialize Pygame
pygame.init()

# Set up fonts
font = pygame.font.Font("8-BIT_WONDER.TTF", 18)
font_title = pygame.font.Font("8-BIT_WONDER.TTF", 42)

# Main menu options
options = ["Human vs Human", "Human vs Computer", "Computer vs Computer"]

# Sub-options for Human vs. Computer mode
sub_options = ["Easy", "Medium" ,"Difficult"]

# Current mode and sub-mode
current_mode = None
current_sub_mode = None

def draw_rounded_rect(surface, color, rect, border_radius):
    pygame.draw.rect(surface, color, rect, border_radius=border_radius)
    width, height = rect.size

def draw_menu():
    WIN.fill(GREY)

    # Draw title
    # title_text = font_title.render("Gobblet Gobblers", True, BLACK)


    cover = pygame.image.load("gobblet_rules.png")
    # scaled_image = pygame.transform.scale(cover, (100, 100))
    WIN.blit(cover, ( 200, 0))



    # title_rect = title_text.get_rect(center=(WIDTH // 2, 50))
    # WIN.blit(title_text, title_rect)

    # Draw buttons
    for i, option in enumerate(options):
        button_rect = pygame.Rect(WIDTH // 4, 150 + (i * 80)+80, WIDTH // 2, 60)
        draw_rounded_rect(WIN, BLACK, button_rect, 15)
        text = font.render(option, True, GREY)
        text_rect = text.get_rect(center=button_rect.center)
        WIN.blit(text, text_rect)

    if current_mode == "Human vs Computer":
        for i, sub_option in enumerate(sub_options):
            # button_rect = pygame.Rect(WIDTH // 2.6, 400 + i * 80, WIDTH // 4, 60)
            button_rect = pygame.Rect((WIDTH // 11) + i*(WIDTH // 3.5), 400 + 80, WIDTH // 4, 60)
            draw_rounded_rect(WIN, WHITE, button_rect, 15)
            text = font.render(sub_option, True, GREY)
            text_rect = text.get_rect(center=button_rect.center)
            WIN.blit(text, text_rect)
            
# Game loop
running = True
in_game = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            # Check if an option is clicked
            for i, option in enumerate(options):
                button_rect = pygame.Rect(WIDTH // 4, 150 + (i * 80)+80, WIDTH // 2, 60)
                if button_rect.collidepoint(x, y):
                    current_mode = option
                    if current_mode == "Human vs Human" or current_mode == "Computer vs Computer":
                        run_game(current_mode)
                        current_mode = None
            if current_mode == "Human vs Computer":
                    for i, sub_option in enumerate(sub_options):
                        button_rect = pygame.Rect((WIDTH // 11) + i*(WIDTH // 3.5), 400 + 80, WIDTH // 4, 60)
                        if button_rect.collidepoint(x, y):
                            current_sub_mode = sub_option
                            print(current_sub_mode)
                            run_game(current_mode, current_sub_mode)
                            current_mode = None

    draw_menu()  
    pygame.display.flip()
pygame.quit()
sys.exit()
