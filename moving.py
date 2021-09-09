import pygame
import time
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
clock=pygame.time.Clock()
fps=30
#game loop

while not exit_game:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit_game=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                snake_x=snake_x+10

    gamewindow.fill(white)
    #create head of snake

    pygame.draw.rect(gamewindow,black,[snake_x,snake_y,snake_size,snake_size])
    clock.tick(fps)
    pygame.display.update()

pygame.quit()
quit()
