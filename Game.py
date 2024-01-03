import pygame
from Board import *
from constants import BLACK, WHITE, WIDTH, HEIGHT, SQUARE_SIZE, ROWS, COLS,first_player,second_player
class Game:
    
    def __init__(self, win,player1,player2):
        self.selected = None
        self.board = Board(win,player1,player2)
        self.win = win
        self.board.draw(self.win)
        self.winner = None
        
    def update(self):
        pygame.display.update()
        
    def select(self,row,col , win):
        if((col == 0 and self.board.turn=="l")or (col == COLS-1 and self.board.turn=="r")):
            self.board.current_piece(row,col,win)        
        elif(col>0 and col<5):
            self.winner =self.board.add_piece_on_board(row,col,win)
            if self.winner !=None:
                pop_res =self.display_popup(self.winner,win)
                return pop_res
    
    def center_popup(width, height):
        x = (WIDTH - width) // 2
        y = (HEIGHT - height) // 2
        return x, y
        
    
    def display_popup(self,message,win):
        pygame.init()

        popup_open = True
        font = pygame.font.Font("8-BIT_WONDER.TTF", 18)

        while popup_open:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        popup_open = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if play_again_button_rect.collidepoint(event.pos):
                        popup_open = False
                        return "new game"
                    elif main_menu_button_rect.collidepoint(event.pos):
                        popup_open = False
                        return "main menu"

            # Display background color on the main screen
            win.fill(BLACK)

            # Display popup window
            popup_background = pygame.Surface((400, 200))
            popup_background.fill(WHITE)
            popup_rect = popup_background.get_rect(center=(WIDTH // 2, HEIGHT // 2 ))
            win.blit(popup_background, popup_rect)

            # Display popup message
            text = font.render(message.upper(), True, BLACK)
            text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50 ))
            win.blit(text, text_rect)

            # Display buttons
            play_again_button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 0, 200, 40)
            main_menu_button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 50, 200, 40)
            
            
            # Display buttons
            pygame.draw.rect(win, RED, play_again_button_rect)
            play_again_text = font.render("Play Again", True, BLACK)
            play_again_text_rect = play_again_text.get_rect(center=play_again_button_rect.center)
            win.blit(play_again_text, play_again_text_rect)

            pygame.draw.rect(win, RED, main_menu_button_rect)
            main_menu_text = font.render("Main Menu", True, BLACK)
            main_menu_text_rect = main_menu_text.get_rect(center=main_menu_button_rect.center)
            win.blit(main_menu_text, main_menu_text_rect)
            
            

            pygame.display.update()

