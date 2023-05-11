import pygame, sys, random
from pygame.math import Vector2

class Fruit():
    def __init__(self):
        # позиции x и y
        self.randomize()
    
    def draw_fruit(self):
        # создать прямоугольник и нарисовать его
        fruit_rect = pygame.Rect(int(self.pos.x * CELL_SIZE), int(self.pos.y * CELL_SIZE), CELL_SIZE, CELL_SIZE)
        # pygame.draw.rect(screen, PALE_GREEN, fruit_rect)
        screen.blit(apple, fruit_rect)

    def randomize(self):
        self.x = random.randint(0, CELL_NUMBER - 1)
        self.y = random.randint(0, CELL_NUMBER - 1)
        self.pos = Vector2(self.x, self.y)

class Snake():
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1, 0)
        self.new_block = False

        self.head_up = pygame.image.load("images/head_up.png").convert_alpha()
        self.head_down = pygame.image.load("images/head_down.png").convert_alpha()
        self.head_right = pygame.image.load("images/head_right.png").convert_alpha()
        self.head_left = pygame.image.load("images/head_left.png").convert_alpha()

        self.tail_up = pygame.image.load("images/tail_up.png").convert_alpha()
        self.tail_down = pygame.image.load("images/tail_down.png").convert_alpha()
        self.tail_right = pygame.image.load("images/tail_right.png").convert_alpha()
        self.tail_left = pygame.image.load("images/tail_left.png").convert_alpha()

        self.body_vertical = pygame.image.load("images/body_vertical.png").convert_alpha()
        self.body_horizontal = pygame.image.load("images/body_horizontal.png").convert_alpha()

        self.body_tr = pygame.image.load("images/body_tr.png").convert_alpha()
        self.body_tl = pygame.image.load("images/body_tl.png").convert_alpha()
        self.body_br = pygame.image.load("images/body_br.png").convert_alpha()
        self.body_bl = pygame.image.load("images/body_bl.png").convert_alpha()

    def draw_snake(self):
        # обновление направления
        self.update_head_graphics()
        self.update_tail_graphics()

        for index, block in enumerate(self.body):
            # 1. нужна позиция прямоугольника
            x_pos = int(block.x * CELL_SIZE)
            y_pos = int(block.y * CELL_SIZE)
            snake_rect = pygame.Rect(x_pos, y_pos, CELL_SIZE, CELL_SIZE)
            
            # 2. в каком направление движение (смотрит змея)
            if index == 0:
                screen.blit(self.head, snake_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, snake_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index-1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical, snake_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal, snake_rect)
                else:
                    if (previous_block.x == -1 and next_block.y == -1) or (previous_block.y == -1 and next_block.x == -1):
                        screen.blit(self.body_tl, snake_rect)
                    elif (previous_block.x == -1 and next_block.y == 1) or (previous_block.y == 1 and next_block.x == -1):
                        screen.blit(self.body_bl, snake_rect)
                    elif (previous_block.x == 1 and next_block.y == -1) or (previous_block.y == -1 and next_block.x == 1):
                        screen.blit(self.body_tr, snake_rect)
                    elif (previous_block.x == 1 and next_block.y == 1) or (previous_block.y == 1 and next_block.x == 1):
                        screen.blit(self.body_br, snake_rect)

    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1, 0): self.head = self.head_left
        elif head_relation == Vector2(-1, 0): self.head = self.head_right
        elif head_relation == Vector2(0, 1): self.head = self.head_up
        elif head_relation == Vector2(0, -1): self.head = self.head_down

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1, 0): self.tail = self.tail_left
        elif tail_relation == Vector2(-1, 0): self.tail = self.tail_right
        elif tail_relation == Vector2(0, 1): self.tail = self.tail_up
        elif tail_relation == Vector2(0, -1): self.tail = self.tail_down

    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

class Main():
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()
    
    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            # обновить положение фрукта
            self.fruit.randomize()
            # увеличить змею
            self.snake.add_block()
    
    def check_fail(self):
        # змея за пределами экрана
        if not 0 <= self.snake.body[0].x < CELL_NUMBER:
            self.game_over()
        if not 0 <= self.snake.body[0].y < CELL_NUMBER:
            self.game_over()
        # не касается саму себя
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        pygame.quit()
        sys.exit()

    def draw_grass(self):
        for j in range(CELL_NUMBER):
            if j % 2 == 0:
                for i in range(CELL_NUMBER):
                    if i % 2 == 0:
                        grass_rect = pygame.Rect(i * CELL_SIZE, j * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                        pygame.draw.rect(screen, DARK_GREEN, grass_rect)
            else:
                for i in range(CELL_NUMBER):
                    if i % 2 != 0:
                        grass_rect = pygame.Rect(i * CELL_SIZE, j * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                        pygame.draw.rect(screen, DARK_GREEN, grass_rect)

""" Палитра цветов """
JUNE_BUD = (175, 215, 70)
PALE_GREEN = (126, 166, 114)
BLUE = (0, 0, 255)
DARK_GREEN = (167, 209, 61)
""" Создания окна """
pygame.init()
CELL_SIZE = 40 # размер ячейки
CELL_NUMBER = 20 # количество ячеек
screen = pygame.display.set_mode((CELL_NUMBER * CELL_SIZE, CELL_NUMBER * CELL_SIZE))
clock = pygame.time.Clock()
""" загрузка файлов """
apple = pygame.image.load("images/apple.png").convert_alpha()
""" гланвый объект """
main_game = Main()
""" Таймер срабатывания движения """
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)
""" Игровой цикл """
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)

    screen.fill(JUNE_BUD)
    main_game.draw()
    pygame.display.update()
    clock.tick(60)
