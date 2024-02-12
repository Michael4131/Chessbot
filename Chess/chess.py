import pygame
from pygame.locals import *

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
    pygame.display.update()

pygame.quit()
