import pygame
import random

class Game:
    def __init__(self):
        pygame.init()
        self.width = 800
        self.height = 600
        self.display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Snake Game')
        self.clock = pygame.time.Clock()
        self.running = False
        self.snake_block = 10
        self.snake_speed = 15
        self.snake_list = []
        self.length_of_snake = 1
        self.food_position = self.spawn_food()

    def spawn_food(self):
        return (random.randrange(0, self.width - self.snake_block, self.snake_block),
                random.randrange(0, self.height - self.snake_block, self.snake_block))

    def start(self):
        self.running = True
        self.game_loop()

    def game_loop(self):
        x1 = self.width / 2
        y1 = self.height / 2
        x1_change = 0
        y1_change = 0

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_change = -self.snake_block
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = self.snake_block
                        y1_change = 0
                    elif event.key == pygame.K_UP:
                        y1_change = -self.snake_block
                        x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        y1_change = self.snake_block
                        x1_change = 0

            if x1 >= self.width or x1 < 0 or y1 >= self.height or y1 < 0:
                self.running = False

            x1 += x1_change
            y1 += y1_change

            self.display.fill((50, 153, 213))
            pygame.draw.rect(self.display, (0, 255, 0), [self.food_position[0], self.food_position[1], self.snake_block, self.snake_block])

            snake_head = [x1, y1]
            self.snake_list.append(snake_head)
            if len(self.snake_list) > self.length_of_snake:
                del self.snake_list[0]

            for x in self.snake_list[:-1]:
                if x == snake_head:
                    self.running = False

            for segment in self.snake_list:
                pygame.draw.rect(self.display, (0, 0, 0), [segment[0], segment[1], self.snake_block, self.snake_block])

            if x1 == self.food_position[0] and y1 == self.food_position[1]:
                self.length_of_snake += 1
                self.food_position = self.spawn_food()

            pygame.display.update()
            self.clock.tick(self.snake_speed)

        pygame.quit()