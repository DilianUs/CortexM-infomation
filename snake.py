import random
import pygame

# Inicialización de Pygame
pygame.init()
clock = pygame.time.Clock()

# Configuración de la ventana del juego
window_width = 500
window_height = 500
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

# Configuración de los colores
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Configuración de la serpiente
snake_block_size = 10
snake_speed = 15
font_style = pygame.font.SysFont(None, 30)

def start_the_game():
    gameLoop()

def close_the_game():
    pygame.quit()
    quit()

def display_menu():
    menu_font = pygame.font.SysFont(None, 50)
    menu_title = menu_font.render("Snake Game", True, black)
    menu_start = menu_font.render("Start", True, black)
    menu_quit = menu_font.render("Quit", True, black)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if 150 <= mouse_pos[0] <= 350 and 200 <= mouse_pos[1] <= 250:
                    start_the_game()
                elif 150 <= mouse_pos[0] <= 350 and 300 <= mouse_pos[1] <= 350:
                    close_the_game()

        window.fill(white)
        window.blit(menu_title, (150, 100))
        pygame.draw.rect(window, red, (150, 200, 200, 50))
        window.blit(menu_start, (200, 210))
        pygame.draw.rect(window, red, (150, 300, 200, 50))
        window.blit(menu_quit, (220, 310))
        pygame.display.update()

def message(msg, color):
    msg = font_style.render(msg, True, color)
    window.blit(msg, [window_width / 6, window_height / 3])

def gameLoop():
    game_over = False
    game_close = False

    x1 = window_width / 2
    y1 = window_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, window_width - snake_block_size) / 10.0) * 10.0
    foody = round(random.randrange(0, window_height - snake_block_size) / 10.0) * 10.0

    score = 0

    while not game_over:

        while game_close == True:
            window.fill(white)
            message("Has perdido! Presiona Q para salir o C para jugar de nuevo", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block_size
                    x1_change = 0

        if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        window.fill(white)
        pygame.draw.rect(window, red, [foodx, foody, snake_block_size, snake_block_size])

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        for x in snake_List:
            pygame.draw.rect(window, black, [x[0], x[1], snake_block_size, snake_block_size])

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            score += 1
            print("Comiste la comida!")
            foodx = round(random.randrange(0, window_width - snake_block_size) / 10.0) * 10.0
            foody = round(random.randrange(0, window_height - snake_block_size) / 10.0) * 10.0
            Length_of_snake += 1

        font = pygame.font.SysFont(None, 25)
        text = font.render("Puntuación: " + str(score), True, black)
        text_rect = text.get_rect()
        text_rect.center = (window_width // 2, 10)
        window.blit(text, text_rect)

        clock.tick(snake_speed)

    pygame.quit()
    quit()

display_menu()

