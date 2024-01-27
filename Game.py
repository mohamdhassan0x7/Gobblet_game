import pygame
from Board import *
from AI import minimax, alpha_beta_pruning, iterative_deepening_alpha_beta_pruning
import Player
import time 
import sys
from constants import BLACK, WHITE, WIDTH, HEIGHT, SQUARE_SIZE, ROWS, COLS, ZERO_Y 
class Game:
    
    def __init__(self, win, player1, player2):
        self.selected = None
        self.board = Board(win, player1, player2)
        self.win = win
        self.board.draw(self.win)
        self.winner = None
        
    def update(self):
        pygame.display.update()

    def select(self,row,col , win):
        if row == -1 and (col == 2 or col == 3):
           res = self.board.draw_Req(self.win)
           
           if res == "Draw":
            self.winner = "Draw"
            pop_res =self.display_popup(self.winner,win)
            return pop_res


        elif((col == 0 and self.board.turn=="l" and self.board.left_player.ai == False) or (col == COLS-1 and self.board.turn=="r" and self.board.right_player.ai == False)):
            self.board.current_piece(row,col,win)        
        elif(col>0 and col<5):
            if  (self.board.turn == "r" and self.board.right_player.ai == False) or (self.board.turn == "l" and self.board.left_player.ai == False):
                self.winner =self.board.add_piece_on_board(row,col,win)    
            if self.winner !=None:
                pop_res =self.display_popup(self.winner,win)
                return pop_res
    
    def get_row_col_from_mouse(self, pos):
        x, y = pos
        row = (y-ZERO_Y) // SQUARE_SIZE
        col = x // SQUARE_SIZE
        return row, col
    
    def fire(self, event):
        if (self.board.turn == "r" and self.board.right_player.ai == True) or (self.board.turn == "l" and self.board.left_player.ai == True):
            self.winner = self.ai_move()
            if self.winner !=None:
                pop_res =self.display_popup(self.winner,self.win)
                return pop_res

        elif (self.board.turn == "r" and self.board.right_player.ai == False) or (self.board.turn == "l" and self.board.left_player.ai == False):
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = self.get_row_col_from_mouse(pos)
                res = self.select(row, col, self.win)
                return res


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
                    sys.exit()
                    # pygame.quit()
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


            # Display popup window
            popup_outline_background = pygame.Surface((400, 200))
            popup_outline_background.fill(GREY)
            popup_outline_rect = popup_outline_background.get_rect(center=((WIDTH // 2)+8, (HEIGHT // 2)+8 ))
            win.blit(popup_outline_background, popup_outline_rect)

            popup_background = pygame.Surface((400, 200))
            popup_background.fill(BLACK)
            popup_rect = popup_background.get_rect(center=(WIDTH // 2, HEIGHT // 2 ))
            win.blit(popup_background, popup_rect)

            # Display popup message
            text = font.render(message.upper(), True, GREY)
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
    def ai_move (self):
        start_time = time.time()
        # pygame.time.delay(500)
        depth = 1

        if self.board.turn == "r" :
            if self.board.right_player.level == "Easy":
                minEval, best_move = minimax(self.board, depth, False)
                # print("EASY")
            elif self.board.right_player.level == "Medium":  
                #use alpha beta pruning  
                minEval, best_move = alpha_beta_pruning(self.board, depth+1, False)
            elif self.board.right_player.level == "Difficult":  
                #use alpha beta pruning  
                minEval, best_move = iterative_deepening_alpha_beta_pruning(self.board, depth+1, False)    
        
        else:
            if self.board.left_player.level == "Easy":
                maxEval, best_move = minimax(self.board, depth, True)
            elif self.board.right_player.level == "Medium":  
                #use alpha beta pruning  
                minEval, best_move = alpha_beta_pruning(self.board, depth+1, False)    
            elif self.board.left_player.level == "Difficult":  
                #use alpha beta pruning  
                maxEval, best_move = iterative_deepening_alpha_beta_pruning(self.board, depth+1, True)

        print("time: ", time.time() - start_time)

        self.board = best_move
        self.board.switch_turn(self.win) 
        self.board.print_board(self.win)
        self.board.draw_deck(self.win)
        
        res = self.board.check_winner(self.board.board)
        if res != 'No Winner':
            if res == self.board.left_player.color:
                    return "left player wins"
            else:
                return "right player wins"
               
           
    
