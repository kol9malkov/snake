import pygame, sys, random
from pygame.math import Vector2

class Fruit():
    def __init__(self):
        # позиции x и y
        self.x = random.randint(0, CELL_NUMBER - 1)
        self.y = random.randint(0, CELL_NUMBER - 1)
        self.pos = Vector2(self.x, self.y)
    
    # отрисовка квадрата
    def draw_fruit(self):
        x_pos = int(self.pos.x * CELL_SIZE)
        y_pos = int(self.pos.y * CELL_SIZE)
        fruit_rect = pygame.Rect(x_pos, y_pos, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, RED, fruit_rect)

""" Палитра цветов """
JUNE_BUD = (175, 215, 70)
RED = (255, 0, 0)
""" Создания окна """
pygame.init()
CELL_SIZE = 40 # размер ячейки
CELL_NUMBER = 20 # количество ячеек
screen = pygame.display.set_mode((CELL_NUMBER * CELL_SIZE, CELL_NUMBER * CELL_SIZE))
clock = pygame.time.Clock()
""" Создание объектов """
fruit = Fruit()
""" Игровой цикл """
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(JUNE_BUD)
    # отрисовка объектов
    fruit.draw_fruit()
    pygame.display.update()
    clock.tick(60)
