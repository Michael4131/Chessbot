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
        # Draw the piece at its current position on the screen
        if self.position is not None:
            x, y = self.position
            screen.blit(self.image, (x * SQUARE_SIZE + BOARD_OFFSET_X, y * SQUARE_SIZE + BOARD_OFFSET_Y))

    def is_valid_move(self, new_position):
        # Implement logic to check if the move is valid for a pawn
        if self.position is None:
            return False
        x, y = self.position
        new_x, new_y = new_position
        if self.color == 'white':
            if y ==  6 and (new_y ==  4 or new_y ==  5) and x == new_x:
                return True
            elif y ==  5 and new_y ==  4 and x == new_x:
                return True
        elif self.color == 'black':
            if y ==  1 and (new_y ==  3 or new_y ==  2) and x == new_x:
                return True
            elif y ==  2 and new_y ==  3 and x == new_x:
                return True
        return False

class Pawn(Piece):
    def __init__(self, color, 'pawn', image_path):
        super().__init__(color, 'pawn', image_path)
    
    def is_valid_move(self, position):
        if self.position is None:
            return False
        x,y = self.position
        new_x, new_y = new_position

        if self.color == 'white':
            # White pawns can move forward one square
            if y ==  6 and new_y ==  5 and x == new_x:
                return True
            # White pawns can move forward two squares on their first move
            elif y ==  6 and new_y ==  4 and x == new_x:
                return True
            # White pawns can capture diagonally
            elif y ==  6 and (new_y ==  5 or new_y ==  4) and (new_x == x -  1 or new_x == x +  1):
                return True
        elif self.color == 'black':
            # Black pawns can move forward one square
            if y ==  1 and new_y ==  2 and x == new_x:
                return True
            # Black pawns can move forward two squares on their first move
            elif y ==  1 and new_y ==  3 and x == new_x:
                return True
            # Black pawns can capture diagonally
            elif y ==  1 and (new_y ==  2 or new_y ==  3) and (new_x == x -  1 or new_x == x +  1):
                return True
        return False

        pass
    
    def get_valid_move():
        pass

    def move(self, new_position):
        if self.is_valid_move(new_position):
            self.position = new_position
            self.has_moved = True
        else:
            print("Invalid move")



white_pawn = Pawn('white', 'Chesspieces\Chess_plt60.png')
black_pawn = Pawn('black', 'Chesspieces\Chesspdt60.png')