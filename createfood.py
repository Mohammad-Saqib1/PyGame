import pygame
import random
pygame.init()
#colors
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)


#screen l and b
scrn_width=900
scrn_height=600
#create window
gamewindow=pygame.display.set_mode((scrn_width,scrn_height))
pygame.display.set_caption("SnakesBySaqib")
pygame.display.update()
#variables
exit_game=False
game_over=False
snake_x=45
snake_y=55
snake_size=10
velocity_x=0
velocity_y=0
food_x=random.randint(0,scrn_width)
food_y=random.randint(0,scrn_height)
clock=pygame.time.Clock()
fps=30
#game loop

while not exit_game:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit_game=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                velocity_x=10
                velocity_y=0
            if event.key==pygame.K_LEFT:
                velocity_x=-10
                velocity_y=0
            if event.key==pygame.K_UP:
                velocity_y=-10
                velocity_x=0
            if event.key==pygame.K_DOWN:
                velocity_y=10
                velocity_x=0
        
    snake_x=snake_x+velocity_x
    snake_y=snake_y+velocity_y

    gamewindow.fill(white)
    #create head of snake

    pygame.draw.rect(gamewindow,black,[snake_x,snake_y,snake_size,snake_size])
    pygame.draw.rect(gamewindow,red,[food_x,food_y,snake_size,snake_size])
    pygame.display.update()
    clock.tick(fps)
    #create food

pygame.quit()
quit()
