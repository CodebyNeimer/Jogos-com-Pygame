# Modulos necessarios
import pygame as pg
from pygame.locals import *
import random
from time import sleep
# Inicilizador de tudo
pg.init()

def on_grid():
    x = random.randint(0,590)
    y = random.randint(0,590)
    return (x//10 * 10, y//10 * 10)

def collision_apple(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

def collision_wall_x(snake, x):
    return (snake[0][0] == 0 - 10) or (snake[0][0] == x + 10)

def collision_wall_y(snake, y):
    return (snake[0][1] == 0 - 10) or (snake[0][1] == y + 10)
    
def collision_snake(snake):
    if any(bloco == snake[0] for bloco in snake[1:]):
        return True
    return False

# VARIAVEIS NO ESCOPO GLOBAL
x = 600
y = 600
screen = pg.display.set_mode((x, y))
pg.display.set_caption('SNAKE BY NEIMER')
snake_speed = 20
clock = pg.time.Clock()
# Cores
preto = 0,0,0
vermelho = 255,0,0
# Snake
snake = [(200,200), (210,200),(220,200)]
snake_skin = pg.Surface((10,10))
snake_skin.fill((255,255,255))
# Movimentação
my_direction = 'LEFT'
# apple
apple = pg.Surface((10,10))
apple.fill((255,0,0))
apple_pos = on_grid()
score = 0

def show_score():
    my_font = pg.font.SysFont("None", 30)
    my_text = my_font.render('Score: ' + str(score), True, (0,0,255))
    screen.blit(my_text, (5,5))

def mensagem():
    font_style = pg.font.SysFont("None",25)
    msg = font_style.render("Você Perdeu, Gostaria de tentar novamente? [Y] or [N]", True, (255,0,0))
    screen.blit(msg, (65,100))
    return msg

# Loop do jogo
def gameloop():
    
    global apple_pos, score  
    
    game_over = False
    run = False
    change = ''
    my_direction = 'LEFT'
    score = 0
    snake = [[200,200], [210,200], [220,200]]

    while game_over == False:

        while run == True:
            screen.fill(preto)
            mensagem()
            pg.display.update()
            
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_n:
                        run = False
                        game_over = True
                    elif event.key == pg.K_y:
                        gameloop()
                    
       
        screen.fill(preto)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_over = True
        
        # Comandos de movimento SNAKE:

            elif event.type == KEYDOWN:    
                if event.key == K_UP:
                    change = 'UP'
                elif event.key == K_DOWN:
                    change = 'DOWN'
                elif event.key == K_RIGHT:
                    change = 'RIGHT'
                elif event.key == K_LEFT:
                    change = 'LEFT'
        

        # Validação da posição da SNAKE:

        if my_direction == 'LEFT':
            snake[0] = (snake[0][0] - 10, snake[0][1])

        if my_direction == 'UP':
            snake[0] = (snake[0][0], snake[0][1] - 10)
            
        if my_direction == 'DOWN':
            snake[0] = (snake[0][0], snake[0][1] + 10)

        if my_direction == 'RIGHT':
            snake[0] = (snake[0][0] + 10, snake[0][1])
        
        # Update Snake Position:

        if change == 'LEFT' and my_direction != 'RIGHT':
            my_direction = change
        if change == 'RIGHT' and my_direction != 'LEFT':
            my_direction = change
        if change == 'UP' and my_direction != 'DOWN':
            my_direction = change
        if change == 'DOWN' and my_direction != 'UP':
            my_direction = change
        
        ##############################################
        
        if collision_wall_x(snake, x):
            run = True
                
        if collision_wall_y(snake, y):
            run = True

        if collision_apple(snake[0], apple_pos):
            apple_pos = on_grid()
            snake.append((0,0))
            score += 5
        
        if collision_snake(snake):
            run = True    
        
        for i in range(len(snake) -1, 0, -1):
            snake[i] = (snake[i-1][0], snake[i-1][1])
        
        screen.blit(apple,apple_pos)

        for pos in snake:
            screen.blit(snake_skin, pos)   
        
        clock.tick(snake_speed)
        show_score()
        pg.display.update()

gameloop()
pg.quit()
quit()


 

