import pygame
from pygame.locals import *


white_pawn = pygame.image.load("Chesspieces\Chess_plt60.png")
dark_pawn = pygame.image.load("Chesspieces\Chess_pdt60.png")
dark_bishop = pygame.image.load("Chesspieces\Chess_bdt60.png")
white_bishop = pygame.image.load("Chesspieces\Chess_blt60.png")
dark_knight = pygame.image.load("Chesspieces\Chess_ndt60.png")
white_knight= pygame.image.load("Chesspieces\Chess_nlt60.png")
dark_rook = pygame.image.load("Chesspieces\Chess_rdt60.png")
white_rook = pygame.image.load("Chesspieces\Chess_rlt60.png")
dark_queen= pygame.image.load("Chesspieces\Chess_qdt60.png")
white_queen = pygame.image.load("Chesspieces\Chess_qlt60.png")
dark_king = pygame.image.load("Chesspieces\Chess_kdt60.png")
white_king = pygame.image.load("Chesspieces\Chess_klt60.png")

class Piece:
    def __init__(self, color, type, image_path):
        self.color = color  # 'white' or 'black'
        self.type = type  # 'pawn'
        self.image = pygame.image.load(image_path)
        self.position = None  # This will be set later
        self.has_moved = False  # Track if the pawn has moved

    def move(self, new_position):
        if self.is_valid_move(new_position):
            self.position = new_position
            self.has_moved = True
        else:
            print("Invalid move")

    def draw(self, screen):
        if self.position is not None:
            x, y = self.position
            screen.blit(self.image, (x * SQUARE_SIZE + BOARD_OFFSET_X, y * SQUARE_SIZE + BOARD_OFFSET_Y))

    def is_valid_move(self, new_position):
        # Placeholder for piece-specific movement logic
        return False

class Pawn(Piece):
    def __init__(self, color, image_path):
        super().__init__(color, image_path)

    def is_valid_move(self, new_position):
        if self.position is None:
            return False
        x, y = self.position
        new_x, new_y = new_position

        if self.color == 'white':
            if y ==  6 and (new_y ==  5 or new_y ==  4) and x == new_x:
                return True
            elif y ==  5 and new_y ==  4 and x == new_x:
                return True
            elif y ==  6 and (new_y ==  5 or new_y ==  4) and (new_x == x -  1 or new_x == x +  1):
                return True
        elif self.color == 'black':
            if y ==  1 and (new_y ==  2 or new_y ==  3) and x == new_x:
                return True
            elif y ==  2 and new_y ==  3 and x == new_x:
                return True
            elif y ==  1 and (new_y ==  2 or new_y ==  3) and (new_x == x -  1 or new_x == x +  1):
                return True
        return False

    def move(self, new_position):
        if self.is_valid_move(new_position):
            self.position = new_position
            self.has_moved = True
        else:
            print("Invalid move")

# Corrected image paths
white_pawn = Pawn('white', 'Chesspieces/Chess_plt60.png')
black_pawn = Pawn('black', 'Chesspieces/Chess_pdt60.png')

# Define colors
lightCol = (255,  255,  255)  # White
darkCol = (0,  0,  0)          # Black

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT =  800,  800
SQUARE_SIZE = WIDTH //  8
BOARD_OFFSET_X = (WIDTH - SQUARE_SIZE *  8) /  2
BOARD_OFFSET_Y = (HEIGHT - SQUARE_SIZE *  8) /  2

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

def draw_square(color, x, y):
    pygame.draw.rect(screen, color, (x * SQUARE_SIZE + BOARD_OFFSET_X, y * SQUARE_SIZE + BOARD_OFFSET_Y, SQUARE_SIZE, SQUARE_SIZE))

def create_graphical_board():
    for file in range(8):
        for rank in range(8):
            is_light_square = (file + rank) %  2 !=  0
            square_colour = lightCol if is_light_square else darkCol
            position = (file, rank)
            draw_square(square_colour, position[0], position[1])


# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.fill((0,  0,  0))  # Clear the screen with black before drawing the board
    create_graphical_board()
    white_pawn.draw(screen)  # Draw the white pawn
    pygame.display.update()

pygame.quit()