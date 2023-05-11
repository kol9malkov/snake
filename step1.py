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

    def draw_snake(self):
        for block in self.body:
            # создать прямоугольник и нарисовать его
            x_pos = int(block.x * CELL_SIZE)
            y_pos = int(block.y * CELL_SIZE)
            snake_rect = pygame.Rect(x_pos, y_pos, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, BLUE, snake_rect)
    
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

""" Палитра цветов """
JUNE_BUD = (175, 215, 70)
PALE_GREEN = (126, 166, 114)
BLUE = (0, 0, 255)
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
