import pygame, sys, random, time

pygame.init()
pygame.font.init()
pygame.mixer.init()



WIDTH = 800
HEIGHT = 600
GRID_SIZE = 50

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
pygame.display.set_icon(pygame.image.load('icon.jpg'))
clock = pygame.time.Clock()

#colors
bg_color = (0,0,0)
snake_color = (0, 255, 0)
food_color = (255, 0, 0)
font_color = (255, 255, 255)

snake = [(50,50)]
snakeX_speed = 0
snakeY_speed = 0

food = pygame.Rect(500, 50, 50, 50)

points = 0

#text in pygame
font_size = 32
font = pygame.font.SysFont('Arial', font_size)
text = font.render(f'Points: {points}', True, font_color, bg_color)
textRect = text.get_rect()
textRect.left = 650

difficulty = 5

#sfx
eat_sound = pygame.mixer.Sound('eat.mp3')
gameover_sound = pygame.mixer.Sound('gameover.mp3')
#bg music
pygame.mixer.music.load('background.mp3')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            #change the speed value of the snake depending on what direction was pressed
            if event.key == pygame.K_UP:
                snakeX_speed = 0
                snakeY_speed = -GRID_SIZE
            if event.key == pygame.K_DOWN:
                snakeX_speed = 0
                snakeY_speed = GRID_SIZE
            if event.key == pygame.K_LEFT:
                snakeX_speed = -GRID_SIZE
                snakeY_speed = 0
            if event.key == pygame.K_RIGHT:
                snakeX_speed = GRID_SIZE
                snakeY_speed = 0

    screen.fill(bg_color)
    screen.blit(text, textRect)
    #deals with snake movement
    head_x, head_y = snake[0] #(50, 50)
    new_head = (head_x + snakeX_speed, head_y + snakeY_speed)
    snake.insert(0, new_head)


    if pygame.Rect(new_head, (GRID_SIZE, GRID_SIZE)).colliderect(food):
        #change the location of food
        eat_sound.play()
        points += 1
        text = font.render(f'Points: {points}', True, font_color, bg_color)
        food.left = random.randrange(0, WIDTH, GRID_SIZE)
        food.top = random.randrange(0, HEIGHT, GRID_SIZE)

    else:
        snake.pop()

    pygame.draw.rect(screen, food_color, food)

    for segment in snake:
        pygame.draw.rect(screen, snake_color, pygame.Rect(segment, (GRID_SIZE, GRID_SIZE)))



    if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
        print("Game over - Hit the boundary")
        pygame.quit()
        sys.exit()

    if new_head in snake[1:]:
        print("Game over - bit itself")
        pygame.quit()
        sys.exit()

    if points > 20:
        difficulty = 60
    elif points > 10:
        difficulty = 30
    else:
        difficulty = 5

    pygame.display.flip()

    clock.tick(difficulty)