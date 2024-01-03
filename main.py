import pygame
from constants import WIDTH, HEIGHT, SQUARE_SIZE, RED,first_player,second_player
from Game import Game
import Player
FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Gobblet Gobblers')

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN,Player.Player(first_player),Player.Player(second_player))
    
    game.update()
    
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                res = game.select(row, col, WIN)
                if res == "new game":
                    game = Game(WIN,Player.Player(first_player),Player.Player(second_player))
                elif res == "main menu":
                    pass
                # print(row, col)
                game.update()
    
    pygame.quit()

main()