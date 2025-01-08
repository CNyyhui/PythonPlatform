import pygame
import random

# Initialize Pygame
pygame.init()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)

# Screen dimensions
WIDTH = 300
HEIGHT = 600
BLOCK_SIZE = 30

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tetris')
clock = pygame.time.Clock()

# Tetromino shapes
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1, 1], [1, 0, 0]],  # L
    [[1, 1, 1], [0, 0, 1]],  # J
    [[1, 1, 0], [0, 1, 1]],  # S
    [[0, 1, 1], [1, 1, 0]]   # Z
]

COLORS = [CYAN, YELLOW, PURPLE, ORANGE, BLUE, GREEN, RED]

class Tetromino:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.shape = random.choice(SHAPES)
        self.color = COLORS[SHAPES.index(self.shape)]
        self.rotation = 0

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.shape)
        self.shape = list(zip(*self.shape[::-1]))

    def image(self):
        return [[(self.x + i * BLOCK_SIZE, self.y + j * BLOCK_SIZE)
                 for i, row in enumerate(self.shape[self.rotation]) if row
                 for j, col in enumerate(row) if col]]

class Tetris:
    def __init__(self):
        self.grid = [[0 for _ in range(WIDTH // BLOCK_SIZE)] for _ in range(HEIGHT // BLOCK_SIZE)]
        self.current_piece = Tetromino(WIDTH // 2, 0)
        self.score = 0
        self.game_over = False

    def move(self, dx, dy):
        self.current_piece.x += dx * BLOCK_SIZE
        self.current_piece.y += dy * BLOCK_SIZE
        if self.check_collision():
            self.current_piece.x -= dx * BLOCK_SIZE
            self.current_piece.y -= dy * BLOCK_SIZE
            if dy == 1:
                for x, y in self.current_piece.image()[0]:
                    self.grid[int(y // BLOCK_SIZE)][int(x // BLOCK_SIZE)] = self.current_piece.color
                self.clear_lines()
                self.new_piece()

    def check_collision(self):
        for x, y in self.current_piece.image()[0]:
            if x < 0 or x >= WIDTH or y >= HEIGHT or (y >= 0 and self.grid[int(y // BLOCK_SIZE)][int(x // BLOCK_SIZE)]):
                return True
        return False

    def rotate(self):
        old_rotation = self.current_piece.rotation
        old_shape = self.current_piece.shape
        self.current_piece.rotate()
        if self.check_collision():
            self.current_piece.rotation = old_rotation
            self.current_piece.shape = old_shape

    def clear_lines(self):
        lines_cleared = 0
        for i, row in enumerate(self.grid[::-1]):
            if all(row):
                del self.grid[-(i + 1)]
                self.grid.insert(0, [0 for _ in range(WIDTH // BLOCK_SIZE)])
                lines_cleared += 1
        self.score += lines_cleared ** 2

    def new_piece(self):
        self.current_piece = Tetromino(WIDTH // 2, 0)
        if self.check_collision():
            self.game_over = True

    def draw(self, screen):
        for y, row in enumerate(self.grid):
            for x, val in enumerate(row):
                if val:
                    pygame.draw.rect(screen, val, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
        for x, y in self.current_piece.image()[0]:
            pygame.draw.rect(screen, self.current_piece.color, (x, y, BLOCK_SIZE, BLOCK_SIZE))

def main():
    tetris = Tetris()
    fall_time = 0
    fall_speed = 1000  # ms

    while not tetris.game_over:
        screen.fill(BLACK)
        tetris.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                tetris.game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tetris.move(-1, 0)
                if event.key == pygame.K_RIGHT:
                    tetris.move(1, 0)
                if event.key == pygame.K_DOWN:
                    tetris.move(0, 1)
                if event.key == pygame.K_UP:
                    tetris.rotate()

        # Piece falling logic
        fall_time += clock.get_rawtime()
        if fall_time / 1000 > 1 / fall_speed:
            fall_time = 0
            tetris.move(0, 1)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()