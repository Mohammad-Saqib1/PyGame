import pygame
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

#game loop
while not exit_game:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit_game=True

    gamewindow.fill(white)
    pygame.display.update()

pygame.quit()
quit()
