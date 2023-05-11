import pygame, sys

""" Палитра цветов """
JUNE_BUD = (175, 215, 70)
""" Создания окна """
pygame.init()
CELL_SIZE = 40 # размер ячейки
CELL_NUMBER = 20 # количество ячеек
screen = pygame.display.set_mode((CELL_NUMBER * CELL_SIZE, CELL_NUMBER * CELL_SIZE))
clock = pygame.time.Clock()

""" Игровой цикл """
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(JUNE_BUD)
    pygame.display.update()
    clock.tick(60)