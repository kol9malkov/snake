import pygame, sys, random
from pygame.math import Vector2

class Fruit():
    def __init__(self):
        # позиции x и y
        self.x = random.randint(0, CELL_NUMBER - 1)
        self.y = random.randint(0, CELL_NUMBER - 1)
        self.pos = Vector2(self.x, self.y)
    
    def draw_fruit(self):
        # создать прямоугольник и нарисовать его
        fruit_rect = pygame.Rect(int(self.pos.x * CELL_SIZE), int(self.pos.y * CELL_SIZE), CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, RED, fruit_rect)

class Snake():
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]
    
    def draw_snake(self):
        for block in self.body:
            # создать прямоугольник и нарисовать его
            x_pos = int(block.x * CELL_SIZE)
            y_pos = int(block.y * CELL_SIZE)
            snake_rect = pygame.Rect(x_pos, y_pos, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, BLUE, snake_rect)

""" Палитра цветов """
JUNE_BUD = (175, 215, 70)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
""" Создания окна """
pygame.init()
CELL_SIZE = 40 # размер ячейки
CELL_NUMBER = 20 # количество ячеек
screen = pygame.display.set_mode((CELL_NUMBER * CELL_SIZE, CELL_NUMBER * CELL_SIZE))
clock = pygame.time.Clock()
""" Создание объектов """
fruit = Fruit()
snake = Snake()
""" Игровой цикл """
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(JUNE_BUD)
    fruit.draw_fruit()
    snake.draw_snake()
    pygame.display.update()
    clock.tick(60)
